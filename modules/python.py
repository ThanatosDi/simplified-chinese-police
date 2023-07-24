import os
import re

from .languageABC import LanguageABC


class Python(LanguageABC):
    PYTHON_BLOCK_COMMENT = re.compile(r'([\'\"])\1\1(.*?)\1{3}', re.DOTALL)
    PYTHON_ONE_LINE_COMMENT = re.compile(r"#.*")

    def __init__(self): ...

    def ignore_files(self, path: str) -> list:
        return super().ignore_files(path)

    def files(self, path: str, include_dir: list = ['tests', 'app']):
        """取得所有 PHP 檔案

        Args:
            path (str): 專案路徑
            include_dir (list, optional): 要掃描的資料夾. Defaults to ['tests', 'app'].

        Returns:
            list: PHP 檔案清單
        """
        ignore = self.ignore_files(path)
        files = []
        for dir in include_dir:
            for root, _, filenames in os.walk(os.path.join(path, dir)):
                for filename in filenames:
                    if filename.endswith('.py') and filename not in ignore:
                        files.append(os.path.join(root, filename))
        return files

    def comments(self, file) -> list:
        comment = []
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        block_comments = re.findall(self.PYTHON_BLOCK_COMMENT, content)
        for block_comment in block_comments:
            comment += ''.join(block_comment).split('\n')
        one_line_comments = re.findall(self.PYTHON_ONE_LINE_COMMENT, content)
        return list(filter(None, comment + one_line_comments))
