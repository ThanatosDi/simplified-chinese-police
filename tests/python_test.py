from modules.python import Python


class TestPython:
    @classmethod
    def setup_class(cls):
        cls.python = Python()

    def test_python_ignore(self):
        ignore_files = ['ignore.test']
        assert self.python.ignore_files('tests/code') == ignore_files

    def test_python_files(self):
        files = ['tests/code/test.py']
        assert self.python.files('tests/', include_dir=['code']) == files

    def test_python_comments(self):
        comments = ["'", '多行註解：以下是一個多行註解的範例', '"', '多行註解：以下是一個多行註解的範例',
                    '# 單行註解：這是一個簡單的 Python 程式', '# 這是一個在 class 中的單行註解']
        assert self.python.comments('tests/code/test.py') == comments
