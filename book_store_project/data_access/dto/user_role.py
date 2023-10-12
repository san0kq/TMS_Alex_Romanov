from dataclasses import dataclass


@dataclass
class UserRoleDTO:
    user_id: int
    role_id: int
