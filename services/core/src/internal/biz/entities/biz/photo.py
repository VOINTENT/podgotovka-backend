from src.configs.internal import FILES_LINK
from src.internal.biz.entities.biz.file import File


class Photo(File):

    def create_prefix_url(self) -> None:
        self.prefix_url = FILES_LINK + '/images'

    def create_full_url(self) -> None:
        if not self.prefix_url:
            self.create_prefix_url()

        if self.short_url:
            self.full_url = self.prefix_url + '/' + self.short_url

    def create_short_link_from_optional(self) -> None:
        if not self.prefix_url:
            self.create_prefix_url()

        if self.prefix_url and self.optional_url and self.prefix_url in self.optional_url:
            self.short_url = self.optional_url.replace(self.prefix_url + '/', '')
        else:
            self.short_url = self.optional_url
