import json

import allure
import requests

#用例名称：个人中心个人信息获取成功
#功能名称
@allure.feature("授权模块")
# 子功能名称
@allure.story("授权模块重置密码")
# 用例命名
@allure.title("授权模块验证邮箱是否可以重置")
class Test_APIKeys():
    def test_User_APIKeysList(self):
        url = "https://api.testsprite.com/auth/password/canReset?email=15213337472%40163.com"
        response = requests.get(url).text
        print(response)
        re= json.loads(response)
        assert re['canReset'] == True
    