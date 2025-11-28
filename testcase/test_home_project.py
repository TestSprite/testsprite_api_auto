import allure
import requests

#用例名称：Home项目获取成功
#功能名称
@allure.feature("Home模块")
# 子功能名称
@allure.story("Home模块项目列表")
# 用例命名
@allure.title("Home模块项目列表获取成功")
class Test_Home():
    def test_login_correct(self,login):
        url = "https://api.testsprite.com/project"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "my-project" in response
    