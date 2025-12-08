import allure
import requests


#功能名称
@allure.feature("FrontendProject")
# 子功能名称
@allure.story("FrontendProject项目创建功能")
# 用例命名
@allure.title("FrontendProject创建成功")
class Test_FrontendProject():
    def test_FrontendProject_CreateFrontendProjects(self,login):
        url = "https://api.testsprite.com/project/db855290-6404-4a40-8a70-78e4ea7259e5/frontend"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"name":"项目UI界面功能","url":"https://www.testsprite.com/dashboard","instruction":"通过UI自动化脚本测试dashboard模块的功能","username":"15213337472@163.com","password":"Cs123456."}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "项目UI界面功能" in response
    