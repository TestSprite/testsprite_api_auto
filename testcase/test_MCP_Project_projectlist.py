import allure
import requests

#用例名称：MCP Tests项目获取成功
#功能名称
@allure.feature("MCP Tests模块")
# 子功能名称
@allure.story("MCP Tests项目列表")
# 用例命名
@allure.title("MCP Tests项目列表获取成功")
class Test_MCP():
    def test_MCP_Project_projectlist(self,login):
        url = "https://api.testsprite.com/mcp/project"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "my-project" in response
    