from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net:443"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        href = self._get_upload_link(disk_file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)