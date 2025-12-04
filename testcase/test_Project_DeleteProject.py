import allure
import requests


#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Project删除功能")
# 用例命名
@allure.title("Project删除项目成功")
class Test_Project():
    def test_Project_UpdateProject(self,login):
        url = "https://api.testsprite.com/project/ddaa910e-8f97-4846-acdc-8c7723cbcbb4"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.delete(url,headers=headers).text
        print(response)
        assert "ddaa910e-8f97-4846-acdc-8c7723cbcbb4" in response
    