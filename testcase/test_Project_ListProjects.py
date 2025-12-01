import allure
import requests

#用例名称：Home项目获取成功
#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Project列表")
# 用例命名
@allure.title("Project列表获取成功")
class Test_Project():
    def test_Project_ListProjects(self,login):
        url = "https://api.testsprite.com/project"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "my-project" in response
    