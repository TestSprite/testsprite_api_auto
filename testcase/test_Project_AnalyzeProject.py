import allure
import requests


#功能名称
@allure.feature("Project")
# 子功能名称
@allure.story("Project分析功能")
# 用例命名
@allure.title("Project分析项目成功")
class Test_Project():
    def test_Project_AnalyzeProject(self,login):
        url = "https://api.testsprite.com/project/23ce2cc9-2f37-4a55-b125-1311f58080fb/analyze"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        response = requests.post(url,headers=headers).text
        print(response)
        assert "Project2" in response and "Analyzing" in response
    