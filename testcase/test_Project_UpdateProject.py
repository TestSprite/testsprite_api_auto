import allure
import requests


#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Project更新功能")
# 用例命名
@allure.title("Project更新项目成功")
class Test_Project():
    def test_Project_UpdateProject(self,login):
        url = "https://api.testsprite.com/project/23ce2cc9-2f37-4a55-b125-1311f58080fb"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"name":"Project2"}
        response = requests.put(url,headers=headers,json=data).text
        print(response)
        assert "Project2" in response
    