import allure
import requests

#用例名称：Home项目获取成功
#功能名称
@allure.feature("MCP")
# 子功能名称
@allure.story("MCP项目下的用例")
# 用例命名
@allure.title("MCP项目下的用例获取成功")
class Test_MCP():
    def test_MCP_Project_ListAllTests(self,login):
        url = "https://api.testsprite.com/mcp/project/d303f946-09cd-4db8-828a-247c787c3659/tests"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "TC009-Blog Article Validation and Error Handling" in response
    