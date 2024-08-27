Here is the translated README.md in English:

# API Automation Test Framework Demo

## Introduction
![Demo](doc/demo.gif)  
This is a demo project for API test automation. The project utilizes frameworks such as Pytest, Allure, Requests, and jsonschema.  
The design considers the following scenarios:
- Test cases support asynchronous execution to improve test speed when written asynchronously.
- The jsonschema framework is used to ensure that the returned JSON format is correct.
- Test results are saved using Allure reports.

## Running Tests

To run test cases:

```bash
# Run all tests in the project root directory
pytest
```

```bash
# Run SWAPI tests
pytest -m swapi

# Run EmojiHub tests
pytest -m emojihub
```

To view the report using Allure:
```bash
# Ensure that Allure is installed on your system
# macOS
brew install allure
```

```bash
# Run Allure server to view the report in HTML
allure serve ./allure_report
```

## Project Expansion

1. Add test cases in `testcase/{product_name}`, e.g., `testcase/swapi/test_swapi.py`.
2. Optionally, add JSON schemas in `testcase/{product_name}/schema/schema.py` and `json_res_sample.py`.

---

# API自動化測試框架示範
## 介紹
![Demo](doc/demo.gif)  
這是一個針對 API 測試自動化的示範專案。
專案使用了 Pytest Allure Requests jsonschema 等框架。
設計時考慮了以下場景：
 - 測試用例支援非同步的方式執行，若使用非同步寫法則可以增加執行速度。
 - 使用了 jsonschema 套件來確保 json 回傳的格式正確。
 - 測試結果將利用 Allure 報告保存。

## 執行測試
執行測試用例：

```bash
# 於專案根目錄下 執行全部測試
pytest
```
```bash
# 執行 swapi 測試
pytest -m swapi

# 執行 emojihub 測試
pytest -m emojihub
```

使用 Allure 開啟報告：
```bash
# 確保你的環境已安裝 Allure
# macOS
brew install allure
```
```bash
# 執行 allure server，在 html 上觀看 report
allure serve ./allure_report
```

## 專案擴充
1. 在 testcase/{product_name} 中新增測試用例，例如 testcase/swapi/test_swapi.py
2. 在 testcase/{product_name}/schema/schema.py and json_res_sample.py 中新增 json 的 schema(Optional)
