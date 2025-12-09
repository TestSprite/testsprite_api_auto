import allure
import requests


#功能名称
@allure.feature("MCP")
# 子功能名称
@allure.story("MCP的Frontend项目下的用例")
# 用例命名
@allure.title("MCP的Frontend项目下的用例获取成功")
class Test_MCP():
    def test_MCP_Project_FrontendTests(self,login):
        url = "https://api.testsprite.com/mcp/project/d303f946-09cd-4db8-828a-247c787c3659/frontend-tests"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "testStatus" in response
    