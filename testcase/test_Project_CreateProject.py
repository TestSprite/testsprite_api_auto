import allure
import requests


#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Projectt创建功能")
# 用例命名
@allure.title("Project创建新项目成功")
class Test_Project():
    def test_project(self,login):
        url = "https://api.testsprite.com/project"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"name":"Project1"}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "Project1" in response
    