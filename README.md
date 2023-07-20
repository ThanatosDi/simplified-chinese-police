![image](https://github.com/ThanatosDi/simplified-chinese-police/assets/12424898/9fa162c8-a1f4-4e4e-a319-0576a69839ac)

- [簡體字警察 simplified-chinese-police](#簡體字警察-simplified-chinese-police)
- [支援語言 Support Language](#支援語言-support-language)
- [使用 Use](#使用-use)
  - [env 設定](#env-設定)
      - [`root-path` (optional)](#root-path-optional)
      - [`dictionary` (optional)](#dictionary-optional)
      - [`include_dir` (optional)](#include_dir-optional)
      - [`code-language` (necessary)](#code-language-necessary)


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
## env 設定
#### `root-path` (optional)
要掃描的專案根目錄與本程式相對位置預設 ../
#### `dictionary` (optional)
自定義字典，除了本專案自有的字典之外額外增加自定義字典，可避免中文的異體字影響  
example: "{\\"稅\\": \\"稅\\"}"
#### `include_dir` (optional)
要掃描的程式資料夾，預設掃描 app/ 及 tests/ 兩個資料夾中的檔案
#### `code-language` (necessary)
欲掃描的程式碼語言，詳細請看 [支援語言 Support Language](#支援語言-support-language)

```yaml
env:
  working-directory: ${{ github.workspace }}/task-1.16.0
  # simplified-chinese-police args.
  root-path: ../
  dictionary: "{\"客\": \"客\"}"
  include_dir: app, tests
  code-language: php

jobs:
  simplified-chinese-police:
    runs-on: self-hosted
    strategy:
      fail-fast: false

    steps:
      - uses: actions/checkout@v3

      - name: simplified-chinese-police
        uses: actions/setup-python@v4
        working-directory: ${{ env.working-directory }}
        run: |
          git clone https://github.com/ThanatosDi/simplified-chinese-police.git simplified-chinese-police
          cd simplified-chinese-police
          pip install -r requirements.txt
          python main.py
          
          

      


```
