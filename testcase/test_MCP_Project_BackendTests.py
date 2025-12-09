import allure
import requests


#功能名称
@allure.feature("MCP")
# 子功能名称
@allure.story("MCP的Backend项目下的用例")
# 用例命名
@allure.title("MCP的Backend项目下的用例获取成功")
class Test_MCP():
    def test_MCP_Project_BackendTests(self,login):
        url = "https://api.testsprite.com/mcp/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend-tests"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "" in response
    