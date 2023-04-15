from sys import argv
from func import start

if __name__ == '__main__':
    if argv[1] == '-d' and argv[3] == '-n':
        start(db_name=argv[2], count=argv[4])
    else:
        raise ValueError('You need to specify the path to the database and '
                         'the number of records. Use the keys "-d" and "-n". '
                         'For example: python populate_db -d test.db -n 10.')
