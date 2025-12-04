import allure
import requests


#功能名称
@allure.feature("BackendProject")
# 子功能名称
@allure.story("BackendProject项目下的接口自动化测试用例")
# 用例命名
@allure.title("BackendProject项目下的接口自动化测试用例获取成功")
class Test_BackendProject():
    def test_BackendProject_ListBackendProjects(self,login):
        url = "https://api.testsprite.com/project/87968c69-23fc-4098-a02e-fbc4920a3349/backend"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.get(url,headers=headers).text
        print(response)
        assert "Functional Tests" in response
    