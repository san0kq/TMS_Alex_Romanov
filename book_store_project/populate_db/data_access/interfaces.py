from typing import Protocol, Any


class DBGatewayProtocol(Protocol):
    connection: Any
    cursor: Any
