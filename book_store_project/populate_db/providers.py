from data_access import SqliteGateway


def gateway_provider(db_name: str) -> SqliteGateway:
    return SqliteGateway(db_name=db_name)
