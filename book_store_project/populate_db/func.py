from TMS_Alex_Romanov.book_store_project.populate_db.data_access.db_connector import DBPopulate


def start(db_name: str, count: str) -> None:
    db_populate = DBPopulate(db_name=db_name, count=count)
    db_populate()
    print('Record completed successfully.')
