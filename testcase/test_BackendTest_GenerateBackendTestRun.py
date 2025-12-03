import json
import time

import allure
import requests

#功能名称
@allure.feature("BackendTest")
# 子功能名称
@allure.story("BackendTest执行用例")
# 用例命名
@allure.title("BackendTest执行用例成功")
class Test_BackendTest():
    def test_BackendTest_GenerateBackendTestRun(self,login):
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend/eda43a69-e707-4c3a-b43a-22b5a17513c9/test/3fa04a6e-85df-4f33-8f82-aa8ef43fb389/run"
        token=login
        headers = {"Authorization": f"Bearer {token}"}
        data={}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "Executing" in response
    