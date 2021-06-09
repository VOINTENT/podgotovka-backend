from typing import Optional

from src.configs.internal import FILES_LINK
from src.internal.biz.entities.biz.file import File


class Document(File):

    def __init__(self, full_url: Optional[str] = None, short_url: Optional[str] = None,
                 prefix_url: Optional[str] = None, optional_url: Optional[str] = None,
                 name: Optional[str] = None) -> None:
        super().__init__(full_url, short_url, prefix_url, optional_url)
        self.name = name

    def _create_prefix_url(self) -> None:
        self.prefix_url = FILES_LINK + '/documents'
