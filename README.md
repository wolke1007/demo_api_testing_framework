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

## Test Cases

| Test Case Name                    | Test Description                                                                                                                | Test Data                                                                                                    | Expected Result                                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Test GET Request for People Data  | - Verify that the returned HTTP status code matches the expected value.<br>- Verify that the returned JSON format matches the expected schema. | - People ID: 1<br>- Status Code: 200<br>- Schema: Must match the JSON schema named `get_people`             | - HTTP status code should be 200.<br>- The returned JSON format should match the `get_people` schema. |
| Test GET Request for People Data  | - Verify that the returned HTTP status code matches the expected value.<br>- Verify that the returned JSON format matches the expected schema. | - People ID: 10<br>- Status Code: 200<br>- Schema: Must match the JSON schema named `get_people`            | - HTTP status code should be 200.<br>- The returned JSON format should match the `get_people` schema. |
| Test GET Request for People Data  | - Verify that the returned HTTP status code matches the expected value.<br>- Verify that the returned JSON format matches the expected schema. | - People ID: 10000<br>- Status Code: 404<br>- Schema: None                                                    | - HTTP status code should be 404.<br>- No schema validation is required for the JSON format.             |

### Description of Validation Used

1. **HTTP Status Code Validation**:
   - **Purpose**: To ensure that the API responds with the correct HTTP status code based on the input data.
   - **Reason**: Verifying the status code confirms that the API behaves as expected for valid and invalid inputs. For instance, valid people IDs should return a `200 OK` status, while non-existent IDs should return a `404 Not Found`.

2. **JSON Schema Validation**:
   - **Purpose**: To ensure that the JSON response conforms to the expected format as defined by the schema.
   - **Reason**: Validating the JSON schema ensures that the structure and data types of the response are correct. This helps in confirming that the API's output matches the expected design and provides consistency in data representation. For valid IDs, the response must adhere to the `get_people` schema, while for non-existent IDs, schema validation is not required as no JSON body is expected. 

By using these validations, the test cases ensure that the API not only responds with the correct status but also provides data in the expected format, thereby verifying the robustness and reliability of the API.

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


## 測試用例

| 測試用例名稱                | 測試描述                                                                                                                                                           | 測試資料                                                                                                     | 預期結果                                                                                     |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| 測試使用 http GET 取得 people 資料 | - 檢查回傳的 http status code 是否符合預期<br>- 檢查回傳的 json 格式是否符合預期                                                                 | - people id : 1<br>- status code : 200<br>- schema : 需與名為 get_people 的 json schema 一致 | - http status code 應為 200<br>- 回傳的 json 格式應符合 get_people 的 json schema |
| 測試使用 http GET 取得 people 資料 | - 檢查回傳的 http status code 是否符合預期<br>- 檢查回傳的 json 格式是否符合預期                                                                 | - people id : 10<br>- status code : 200<br>- schema : 需與名為 get_people 的 json schema 一致| - http status code 應為 200<br>- 回傳的 json 格式應符合 get_people 的 json schema |
| 測試使用 http GET 取得 people 資料 | - 檢查回傳的 http status code 是否符合預期<br>- 檢查回傳的 json 格式是否符合預期                                                                 | - people id : 10000<br>- status code : 404<br>- schema : 無                                                     | - http status code 應為 404<br>- 回傳的 json 格式無需符合任何 schema                      |

### 說明驗證的部分

**HTTP 狀態碼驗證**：

- **目的**：確保 API 根據輸入資料回應預期的 HTTP 狀態碼。
- **原因**：驗證狀態碼可以確認 API 對於有效和無效的輸入均如預期運作。例如，有效的 people ID 應該返回 200 OK 狀態碼，而不存在的 ID 應返回 404 Not Found 狀態碼。

**JSON Schema 驗證**：

- **目的**：確保 JSON 回應符合由 schema 定義的預期格式。
- **原因**：驗證 JSON schema 可以確保回應的結構和數據類型是正確的。這有助於確認 API 的輸出符合預期的設計，並提供一致的數據表示。   
           對於有效的 ID，回應必須符合 `get_people` schema，而對於不存在的 ID，由於預期沒有 JSON 主體，因此不需要進行 schema 驗證。

通過使用這些驗證，測試用例不僅確保了 API 回應正確的狀態碼，還確保了數據的格式符合預期，從而驗證了 API 的穩健性和可靠性。