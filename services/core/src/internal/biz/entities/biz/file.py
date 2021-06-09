from abc import ABC, abstractmethod
from typing import Optional


class File(ABC):

    def __init__(self,
                 full_url: Optional[str] = None,
                 short_url: Optional[str] = None,
                 prefix_url: Optional[str] = None,
                 optional_url: Optional[str] = None) -> None:
        self.optional_url = optional_url
        self.prefix_url = prefix_url
        self.short_url = short_url
        self.full_url = full_url

    def get_full_url(self) -> str:
        if not self.full_url:
            self._create_full_url()
        return self.full_url

    def create_short_link_from_optional(self) -> None:
        if not self.prefix_url:
            self._create_prefix_url()

        if self.prefix_url and self.optional_url and self.prefix_url in self.optional_url:
            self.short_url = self.optional_url.replace(self.prefix_url + '/', '')
        else:
            self.short_url = self.optional_url

    def _create_full_url(self) -> None:
        if not self.prefix_url:
            self._create_prefix_url()

        if self.short_url:
            self.full_url = self.prefix_url + '/' + self.short_url

    @abstractmethod
    def _create_prefix_url(self) -> None:
        pass
