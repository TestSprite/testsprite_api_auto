import allure
import requests

#用例名称：Home项目获取成功
#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Project获取项目信息功能")
# 用例命名
@allure.title("Project获取项目信息成功")
class Test_Project():
    def test_Project_GetProject(self,login):
        url = "https://api.testsprite.com/project/23ce2cc9-2f37-4a55-b125-1311f58080fb"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "Project2" in response
    