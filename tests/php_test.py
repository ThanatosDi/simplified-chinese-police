from modules.php import PHP


class TestPHP:
    @classmethod
    def setup_class(cls):
        cls.php = PHP()

    def test_php_ignore(self):
        ignore_files = ['ignore.test']
        assert self.php.ignore_files('tests/code') == ignore_files

    def test_php_files(self):
        files = ['tests/code/test.php']
        assert self.php.files('tests/', include_dir=['code']) == files

    def test_php_comments(self):
        comments = ['/**', ' * 多行註解：以下是一個變數的範例', ' * 注意：這是繁體中文的多行註解。',
                    ' */', '// 單行註解：這是一個簡單的 PHP 程式', '// 建構子', '// 這是一個在 class 中的單行註解']
        assert self.php.comments('tests/code/test.php') == comments
