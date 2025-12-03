import json

import allure
import requests

#功能名称
@allure.feature("BackendTest")
# 子功能名称
@allure.story("BackendTest生成代码")
# 用例命名
@allure.title("BackendTest生成代码成功")
class Test_BackendTest():
    def test_BackendTest_GenerateBackendTestCode(self,login):
        #先创建用例，在生成代码
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend/eda43a69-e707-4c3a-b43a-22b5a17513c9/test"
        token = login
        headers = {"Authorization": f"Bearer {token}"}
        data = {"title": "Create Project with Valid Data",
                "description": "Test the API by creating a project using valid and complete data, expecting a successful response with appropriate project details in the response.",
                "category": "Basic Functional Tests", "priority": "High", "custom": False}
        response = requests.post(url, headers=headers, json=data).text
        re=json.loads(response)
        projectId=re['projectId']
        backendProjectId = re['backendProjectId']
        testId=re['id']
        url1 = "https://api.testsprite.com/project/"+projectId+"/backend/"+backendProjectId+"/test/"+testId+"/code"
        data={}
        response = requests.post(url1,headers=headers,json=data).text
        print(response)
        assert "Create Project with Valid Data" in response
    