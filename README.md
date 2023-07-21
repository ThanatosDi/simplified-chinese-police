- [簡體字警察 simplified-chinese-police](#簡體字警察-simplified-chinese-police)
- [支援語言 Support Language](#支援語言-support-language)
- [使用 Use](#使用-use)
  - [with 設定](#with-設定)
      - [`code-path` (necessary)](#code-path-necessary)
      - [`code-language` (necessary)](#code-language-necessary)
      - [`scan-dir` (optional)](#scan-dir-optional)
      - [`custom-dictionary` (necessary)](#custom-dictionary-necessary)
- [Reference](#reference)


# 簡體字警察 simplified-chinese-police
檢查程式碼中的註解是否帶有簡體中文

# 支援語言 Support Language
✅: 支援  
➖: 正在開發  
❌: 不支援  

| 語言   | 支援 |
| ------ | ---- |
| PHP    | ✅    |
| Python | ➖    |

# 使用 Use
## with 設定
#### `code-path` (necessary)
要掃描的專案根目錄與本程式相對位置，預設 ./
#### `code-language` (necessary)
欲掃描的程式碼語言，詳細請看 [支援語言 Support Language](#支援語言-support-language)
#### `scan-dir` (optional)
要掃描的程式資料夾，預設掃描 app/ 及 tests/ 兩個資料夾中的檔案
#### `custom-dictionary` (optional)
自定義字典，除了本專案自有的字典之外額外增加自定義字典，可避免中文的異體字影響  
example: "{'稅': '稅'}"



```yaml

jobs:
  simplified-chinese-police:
    runs-on: self-hosted
    strategy:
      fail-fast: false

    steps:
      - uses: actions/checkout@v3

      - name: simplified-chinese-police
        uses: ThanatosDi/simplified-chinese-police@main
        with:
          code-path: './example-code-path'
          code-language: php
          scan-dir: app, tests
          custom-dictionary: "{'只': '只'}"

```