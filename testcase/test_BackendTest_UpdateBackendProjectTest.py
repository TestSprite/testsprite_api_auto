import allure
import requests

#功能名称
@allure.feature("BackendTest")
# 子功能名称
@allure.story("BackendTest更新测试用例")
# 用例命名
@allure.title("BackendTest更新测试用例成功")
class Test_BackendTest():
    def test_BackendTest_UpdateBackendProjectTest(self,login):
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend/eda43a69-e707-4c3a-b43a-22b5a17513c9/test/34fa6f6c-2d41-426a-ac01-c0a279a4ee92"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"title":"Create Project with Valid Data","description":"TestAPI","category":"Basic Functional Tests","priority":"Medium","custom":False}
        response = requests.put(url,headers=headers,json=data).text
        print(response)
        assert "Medium" in response
    