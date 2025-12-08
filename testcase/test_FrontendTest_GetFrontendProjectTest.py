import allure
import requests

#功能名称
@allure.feature("FrontendTest")
# 子功能名称
@allure.story("FrontendTest查看测试用例")
# 用例命名
@allure.title("FrontendTest查看测试用例成功")
class Test_FrontendTest():
    def test_FrontendTest_GetFrontendProjectTest(self,login):
        url = "https://api.testsprite.com/project/db855290-6404-4a40-8a70-78e4ea7259e5/frontend/ee4fea89-dfc6-44ca-99d7-83bb82177a3c/test/4c54acad-d409-4ad2-9e6a-601a7ad28f90"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "UI自动化用例" in response
    