import allure
import requests


#功能名称
@allure.feature("MCP")
# 子功能名称
@allure.story("MCP生成标准prd文档的用例")
# 用例命名
@allure.title("MCP生成标准prd文档的用例执行成功")
class Test_MCP():
    def test_MCP_GenerateStandardPRD(self,login):
        url = "https://api.testsprite.com/mcp/common/generate-prd"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.post(url,headers=headers).text
        print(response)
        assert "" in response
    