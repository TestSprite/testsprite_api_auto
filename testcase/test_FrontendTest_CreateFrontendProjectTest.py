import allure
import requests

#功能名称
@allure.feature("FrontendTest")
# 子功能名称
@allure.story("FrontendTest创建测试用例")
# 用例命名
@allure.title("FrontendTest创建测试用例成功")
class Test_FrontendTest():
    def test_FrontendTest_CreateFrontendProjectTest(self,login):
        url = "https://api.testsprite.com/project/db855290-6404-4a40-8a70-78e4ea7259e5/frontend/ee4fea89-dfc6-44ca-99d7-83bb82177a3c/test"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"title":"UI自动化用例","description":"Test UI","priority":"High","custom":False}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "UI自动化用例" in response
    