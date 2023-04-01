import json
import csv
import openpyxl
import xml.etree.ElementTree as Et
from xml.dom import minidom
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from decouple import config
from typing import Any

from TMS_Alex_Romanov.rand_gen import RandGen, RandWord
from data import db_provider, DB_NAME, DB_TYPE


class Code:
    def __init__(self) -> None:
        with open('code.json') as file:
            self.json_load = json.load(file)

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        self.code_exists()

    def code_exists(self) -> None:
        if self.json_load['code'] is None:
            code = RandGen(RandWord).generate()
            print(f'Hello. Your code phrase is "{code}", please remember it.')
            self.json_load['code'] = code
            with open('code.json', 'w') as file:
                json.dump(self.json_load, file)

    def code_check(self) -> bool:
        code = input('Please enter your code phrase: ')
        if code != self.json_load['code']:
            return False
        return True


class AESCryptoMixin:
    def __init__(self) -> None:
        self.key = config('KEY').encode('utf-8')
        self.iv = config('IV').encode('utf-8')

    def encrypt(self, password: str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(pad(password.encode(), AES.block_size))
        return base64.b64encode(ciphertext).decode()

    def decrypt(self, ciphertext: str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        password = unpad(cipher.decrypt(base64.b64decode(ciphertext)),
                         AES.block_size)
        return password.decode()


class PasswordManager(AESCryptoMixin):
    def __init__(self) -> None:
        self.pass_db = db_provider(data_name=DB_NAME, data_type=DB_TYPE)
        self.code = Code()
        super().__init__()

    @property
    def identifier(self) -> str:
        return self._identifier

    @identifier.setter
    def identifier(self, value: str) -> None:
        if len(value) == 0:
            raise ValueError('The identifier cannot be an empty string.')
        self._identifier = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if value is not None and len(value) == 0:
            raise ValueError('The password cannot be an empty string.')
        self._password = value

    def add_new_password(self) -> None:
        record = {self.identifier: self.encrypt(self.password)}
        self.pass_db.create(record=record)

    def get_identifiers_list(self) -> str:
        result = []
        for data in self.pass_db.list():
            result.append(data[0])
        if len(result) == 0:
            return "You don't have any saved passwords yet."
        return ' | '.join(result)

    def get_password(self) -> str:
        self.pass_db.identifier_exists(identifier=self.identifier)
        if self.code.code_check():
            data = self.pass_db.read()
            return self.decrypt(data[self.identifier])
        else:
            return 'The code phrase is incorrect. Access denied.'

    def delete_password(self) -> str:
        self.pass_db.identifier_exists(identifier=self.identifier)
        if self.code.code_check():
            self.pass_db.delete(identifier=self.identifier)
            return f'The password for "{self.identifier}" has been deleted.'
        else:
            return 'The code phrase is incorrect. Access denied.'


class ExportPasswords(AESCryptoMixin):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.pass_db = db_provider(data_name=DB_NAME, data_type=DB_TYPE)
        self.code = Code()
        super().__init__()

    def __call__(self, *args: Any, **kwargs: Any) -> str:
        if self.code.code_check():
            file_format = self.file_name.split('.')[1]
            if file_format == 'txt':
                self.export_txt()
            elif file_format == 'csv':
                self.export_csv()
            elif file_format in ('xlsx', 'xlsm', 'xlts', 'xltm'):
                self.export_excel()
            elif file_format == 'xml':
                self.export_xml()
            return f'The file "{self.file_name}" has been generated.'
        else:
            return 'The code phrase is incorrect. Access denied.'

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if len(value) == 0:
            raise ValueError('The filename cannot be an empty string.')
        if len(value.split('.')) != 2:
            raise ValueError('There should be one dot "." in the filename, '
                             'which separates its name and format.')
        file_name, file_format = value.split('.')
        if file_format not in ('txt', 'csv', 'xlsx',
                               'xlsm', 'xlts', 'xltm', 'xml'):
            raise ValueError('This extension is not supported. '
                             'Supported extensions: csv, xlsx, xlsm, '
                             'xlts, xltm, xml, txt.')
        if not re.match(r'^[a-zA-Z0-9_-]+$', file_name):
            raise ValueError('Invalid file name. The name should only contain'
                             ' characters: a-z, A-Z, 0-9, -, and _')

        self._file_name = value

    def export_txt(self) -> None:
        with open(self.file_name, 'w') as file:
            for identifier, password in self.pass_db.list():
                file.write(identifier + ' - ' + self.decrypt(password) + '\n')

    def export_csv(self) -> None:
        with open(self.file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Identifier', 'Password'])
            for identifier, password in self.pass_db.list():
                writer.writerow([identifier, self.decrypt(password)])

    def export_excel(self) -> None:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.append(['Identifier', 'Password'])
        for identifier, password in self.pass_db.list():
            worksheet.append([identifier, self.decrypt(password)])
        workbook.save(self.file_name)

    def export_xml(self) -> None:
        root = Et.Element('Passwords')
        for identifier, password in self.pass_db.list():
            pas = Et.SubElement(root, 'password')
            pas.set('identifier', identifier)
            value = Et.SubElement(pas, 'value')
            value.text = self.decrypt(password)

        xml = minidom.parseString(Et.tostring(root)).toprettyxml(indent="  ")
        with open(self.file_name, 'w') as file:
            file.write(xml)
