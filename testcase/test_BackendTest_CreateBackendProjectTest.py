import allure
import requests

#功能名称
@allure.feature("BackendTest")
# 子功能名称
@allure.story("BackendTest创建测试用例")
# 用例命名
@allure.title("BackendTest创建测试用例成功")
class Test_BackendTest():
    def test_BackendTest_CreateBackendProjectTest(self,login):
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend/eda43a69-e707-4c3a-b43a-22b5a17513c9/test"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"title":"Create Project with Valid Data","description":"Test the API by creating a project using valid and complete data, expecting a successful response with appropriate project details in the response.","category":"Basic Functional Tests","priority":"High","custom":False}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "Create Project with Valid Data" in response
    