from data_access import SqliteGateway


def gateway_provider():
    return SqliteGateway(db_name='book_store.db')
