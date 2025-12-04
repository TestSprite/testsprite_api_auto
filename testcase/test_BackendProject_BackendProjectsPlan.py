import allure
import requests


#功能名称
@allure.feature("BackendProject")
# 子功能名称
@allure.story("BackendProject项目测试计划")
# 用例命名
@allure.title("BackendProject项目测试计划获取成功")
class Test_BackendProject():
    def test_BackendProject_BackendProjectsPlan(self,login):
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend/eda43a69-e707-4c3a-b43a-22b5a17513c9/plan"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.post(url,headers=headers).text
        print(response)
        assert "项目接口" in response
    