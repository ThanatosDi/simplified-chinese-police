import os
from abc import ABCMeta, abstractmethod


class LanguageABC(metaclass=ABCMeta):

    def ignore_files(self, path: str) -> list:
        """取得 .comment-ignore 檔案內容，此為忽略檔案清單

        Args:
            path (str): 專案路徑

        Returns:
            list: 忽略檔案清單
        """
        ignore_file_path = os.path.join(path, ".comment-ignore")
        if not os.path.exists(ignore_file_path):
            return []
        with open(f'{ignore_file_path}', 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    @abstractmethod
    def files(self, path: str, include_dir: list = ['tests', 'app']): ...

    @abstractmethod
    def comments(self, file) -> list: ...
