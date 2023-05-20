from data_access import SqliteGateway


def gateway_provider() -> SqliteGateway:
    return SqliteGateway(db_name='book_store.db')
