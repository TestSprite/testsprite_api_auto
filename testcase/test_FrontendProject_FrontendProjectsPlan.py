import allure
import requests


#功能名称
@allure.feature("FrontendProject")
# 子功能名称
@allure.story("FrontendProject项目测试计划")
# 用例命名
@allure.title("FrontendProject项目测试计划获取成功")
class Test_FrontendProject():
    def test_FrontendProject_FrontendProjectsPlan(self,login):
        url = "https://api.testsprite.com/project/db855290-6404-4a40-8a70-78e4ea7259e5/frontend/ee4fea89-dfc6-44ca-99d7-83bb82177a3c/plan"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.post(url,headers=headers).text
        print(response)
        assert "项目UI界面功能" in response
    