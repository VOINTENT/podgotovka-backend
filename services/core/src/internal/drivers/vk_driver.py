from typing import Tuple

import requests

from src.configs.vk import VK_APP_ID, VK_APP_SECREY_KEY
from src.configs.internal import CURRENT_URL, IS_TEST


class VKApiDriver:
    _url_api = 'https://api.vk.com/method'
    _url_auth = 'https://oauth.vk.com/authorize'
    _url_access_token = 'https://oauth.vk.com/access_token'

    _client_id = VK_APP_ID
    _client_secret = VK_APP_SECREY_KEY
    _display = 'page'
    _redirect_uri = f"{CURRENT_URL}/core/v1/accounts-student/auth/vk"
    _scope_email = 4194304
    _response_type = 'code'
    _version_api = "5.131"

    @classmethod
    async def get_vk_access_token(cls, code: str) -> Tuple[bool, str, str, bool]:
        """
        Args:
            code: temporary code from vk
        Returns:
            tuple: error, access_token, email, deactivate
        """

        error = False
        deactivated = False
        access_token = ""
        email = ""

        if IS_TEST:
            if code == "true1true1true":
                access_token = "AEZAKMI"
                email = "test@test.com"
                return error, access_token, email, deactivated
            else:
                error = True
                return error, access_token, email, deactivated

        url = f"{cls._url_access_token}?" \
              f"client_id={cls._client_id}" \
              f"&client_secret={cls._client_secret}" \
              f"&redirect_uri={cls._redirect_uri}" \
              f"&code={code}"

        response = requests.get(url)

        if response.status_code != 200:
            error = True
            return error, access_token, email, deactivated

        result_json = response.json()

        if 'deactivated' in result_json:
            deactivated = True
            return error, access_token, email, deactivated
        access_token = result_json.get('access_token', "")
        email = result_json.get('email', "")

        return error, access_token, email, deactivated

    @classmethod
    async def get_user_info(cls, access_token: str):
        url = f"{cls._url_api}/users.get?" \
              f"&access_token={access_token}" \
              f"&fields=photo_max_orig" \
              f"&v={cls._version_api}"

        if IS_TEST:
            return {
                'photo_max_orig': 'vk.com/image/link1',
                'first_name': 'account',
                'last_name': 'student',
                'id': 1_000_000
            }

        response = requests.get(url)

        if response.status_code != 200:
            print(response.text)
            raise TypeError

        result_json = response.json()

        return result_json['response'][0]
