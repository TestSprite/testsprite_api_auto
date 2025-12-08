import allure
import requests


#功能名称
@allure.feature("BackendProject")
# 子功能名称
@allure.story("FrontendProject项目下的接口自动化测试用例")
# 用例命名
@allure.title("FrontendProject项目下的接口自动化测试用例获取成功")
class Test_FrontendProject():
    def test_FrontendProject_ListFrontendProjects(self,login):
        url = "https://api.testsprite.com/project/db855290-6404-4a40-8a70-78e4ea7259e5/frontend"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "https://www.testsprite.com/dashboard/mcp/tests" in response
    