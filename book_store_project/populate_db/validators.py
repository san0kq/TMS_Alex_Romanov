def parameters_validator(value: list[str]) -> None:
     if len(value) != 4:
          raise ValueError('Invalid parameters. You need to specify the path '
                           'to the database and the number of records. Use '
                           'the keys "-d" and "-n". For example: '
                           'python populate_db -d test.db -n 10.')

def db_name_validator(value: str) -> None:
    if value.isdigit():
         raise ValueError('Database name must be a string.')
    if value.split('.', 1)[1] != 'db':
        raise ValueError('Invalid database name. The file must have '
                         'a .db extension.')

def records_number_validator(value: str) -> None:
    if not value.isdigit():
            raise ValueError('Records number must be a positive integer.')
    elif not 0 < int(value) < 1001:
        raise ValueError('Records number must be an integer in range '
                         '(1, 1000).')
