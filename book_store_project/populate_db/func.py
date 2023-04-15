from db_connector import DBPopulate


def start(db_name: str, count: str) -> None:
    db_populate = DBPopulate(db_name=db_name, count=count)
    db_populate()
    print('Record completed successfully.')
