class File:

    def __init__(self, full_url: str, short_url: str, prefix_url: str, optional_url: str) -> None:
        self.optional_url = optional_url
        self.prefix_url = prefix_url
        self.short_url = short_url
        self.full_url = full_url

    def create_full_url(self) -> None:
        raise NotImplementedError

    def create_prefix_url(self) -> None:
        raise NotImplementedError

    def create_short_link_from_optional(self) -> None:
        if self.prefix_url and self.optional_url and self.prefix_url in self.optional_url:
            self.short_url = self.optional_url.replace(self.prefix_url, '')
        else:
            self.short_url = self.optional_url

    def get_full_url(self) -> str:
        if not self.full_url:
            self.create_full_url()
        return self.full_url
