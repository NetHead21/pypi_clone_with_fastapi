from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    hash_password: str
    id: int = 1
    profile_image_url: str = ""
    created_date: datetime = None
    last_login: datetime = None
