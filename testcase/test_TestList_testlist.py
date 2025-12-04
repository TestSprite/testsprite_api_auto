import allure
import requests


#功能名称
@allure.feature("TestList")
# 子功能名称
@allure.story("TestList项目列表")
# 用例命名
@allure.title("TestList项目列表获取成功")
class Test_TestList():
    def test_TestList_testlist(self,login):
        url = "https://api.testsprite.com/testlist"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "JustForTest" in response and "test1" in response
    