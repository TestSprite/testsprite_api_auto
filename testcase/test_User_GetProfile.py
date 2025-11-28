import allure
import requests

#用例名称：个人中心个人信息获取成功
#功能名称
@allure.feature("个人中心模块")
# 子功能名称
@allure.story("个人中心模块个人信息")
# 用例命名
@allure.title("个人中心模块个人信息获取成功")
class Test_Profile():
    def test_User_GetProfile(self,login):
        url = "https://api.testsprite.com/user/me"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "15213337472@163.com" in response
    