import os
import re


class PHP:
    PHP_BLOCK_COMMENT = re.compile(r'/\*\*.+?\*/', re.DOTALL)
    PHP_ONE_LINE_COMMENT = re.compile(r"//.*")

    def __init__(self): ...

    def __ignore_files(self, path: str) -> list:
        ignore_file_path = os.path.join(path, ".comment-ignore")
        if not os.path.exists(ignore_file_path):
            return []
        with open(f'{ignore_file_path}', 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    def files(self, path: str, include_dir: list = ['tests', 'app']) -> list:
        """取得所有 PHP 檔案

        Args:
            path (str): 專案路徑
            include_dir (list, optional): 要掃描的資料夾. Defaults to ['tests', 'app'].

        Returns:
            list: PHP 檔案清單
        """
        ignore = self.__ignore_files(path)
        files = []
        for dir in include_dir:
            for root, _, filenames in os.walk(os.path.join(path, dir)):
                for filename in filenames:
                    if filename.endswith('.php') and filename not in ignore:
                        files.append(os.path.join(root, filename))
        return files

    def comments(self, file) -> list:
        comment = []
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        block_comments = re.findall(self.PHP_BLOCK_COMMENT, content)
        for block_comment in block_comments:
            comment += block_comment.split('\n')
        one_line_comments = re.findall(self.PHP_ONE_LINE_COMMENT, content)
        return comment + one_line_comments
