import json

import allure
import requests

#用例名称：个人中心个人信息获取成功
#功能名称
@allure.feature("个人中心模块")
# 子功能名称
@allure.story("个人中心模块个人信息")
# 用例命名
@allure.title("个人中心模块apikey新建成功")
class Test_APIKeys():
    def test_User_GenerateAPIKey(self,login):
        url = "https://api.testsprite.com/user/me/apikey"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        data={"name":"test2"}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "test2" in response
        re=json.loads(response)
        #清洗数据
        #删除成功
        url1="https://api.testsprite.com/user/me/apikey/"+re["apiKey"]
        response1=requests.delete(url1, headers=headers).text
        print(response1)
        re1=json.loads(response1)
        assert re1['success']==True
    