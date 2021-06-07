from src.configs.internal import FILES_LINK
from src.internal.biz.entities.biz.file import File


class Photo(File):

    def _create_prefix_url(self) -> None:
        self.prefix_url = FILES_LINK + '/images'
