from typing import Optional


class LogRequest:
    def __init__(self, method: str, url: str, status_code: int, process_time: int, ip: str, headers: str,
                 body: Optional[str], query_params: str, error_msg: str,) -> None:
        self.error_msg = error_msg
        self.query_params = query_params
        self.body = body
        self.headers = headers
        self.ip = ip
        self.process_time = process_time
        self.status_code = status_code
        self.url = url
        self.method = method
