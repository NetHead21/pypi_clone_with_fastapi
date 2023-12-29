from dataclasses import dataclass


@dataclass
class Package:
    package_name: str
    summary: str
    description: str
    home_page: str
    license: str
    author_name: str
    maintainers: list = None

    def __post_init__(self):
        self.id = self.package_name
