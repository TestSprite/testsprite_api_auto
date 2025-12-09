import allure
import requests


#功能名称
@allure.feature("MCP")
# 子功能名称
@allure.story("MCP生成测试报告的用例")
# 用例命名
@allure.title("MCP生成测试报告的用例执行成功")
class Test_MCP():
    def test_MCP_GenerateTestReport(self,login):
        url = "https://api.testsprite.com/mcp/common/generate-test-report"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.post(url,headers=headers).text
        print(response)
        assert "" in response
    