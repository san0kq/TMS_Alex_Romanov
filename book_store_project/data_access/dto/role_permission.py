from dataclasses import dataclass


@dataclass
class RolePermissionDTO:
    role_id: int
    permission_id: int
