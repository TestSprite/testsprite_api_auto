import allure
import requests

#用例名称：个人中心个人信息获取成功
#功能名称
@allure.feature("个人中心模块")
# 子功能名称
@allure.story("个人中心模块个人信息")
# 用例命名
@allure.title("个人中心模块个人信息更新成功")
class Test_Profile():
    def test_User_UpdateProfile(self,login):
        url = "https://api.testsprite.com/user/me"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        data={"firstName":"wan","lastName":"li","company":"testsprite"}
        response = requests.put(url,headers=headers,json=data).text
        print(response)
        assert "wan" in response
    