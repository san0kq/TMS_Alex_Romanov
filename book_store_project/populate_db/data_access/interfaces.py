from typing import Protocol, Any


class DBGatewayProtocol(Protocol):
    connection: Any
    cursor: Any


class CreateRecordProtocol(Protocol):
    def create(self, data: object) -> None:
        raise NotImplementedError
