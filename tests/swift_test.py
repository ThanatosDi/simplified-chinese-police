from modules.swift import Swift


class TestSwift:
    @classmethod
    def setup_class(cls):
        cls.swift = Swift()

    def test_swift_ignore(self):
        ignore_files = ['ignore.test']
        assert self.swift.ignore_files('tests/code') == ignore_files

    def test_swift_files(self):
        files = ['tests/code/test.swift']
        assert self.swift.files('tests/', include_dir=['code']) == files

    def test_swift_comments(self):
        comments = ['/**', ' 多行註解範例：', ' 這是一個多行註解的示例。', ' 可以在這裡加入更多的註解內容。', '*/', '// 單行註解：這是一個簡單的 Swift 檔案',
                    '// 使用多行註解來說明這個結構體', '// 創建一個 Person 實例', '// 使用單行註解來做單行說明', '// 輸出：Hello, World!']
        assert self.swift.comments('tests/code/test.swift') == comments
