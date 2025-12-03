import allure
import requests

#用例名称：Home项目获取成功
#功能名称
@allure.feature("BackendProject")
# 子功能名称
@allure.story("BackendProject项目创建功能")
# 用例命名
@allure.title("BackendProject创建成功")
class Test_BackendProject():
    def test_BackendProject_CreateBackendProjects(self,login):
        url = "https://api.testsprite.com/project/d9f84019-1813-4e24-b6f1-527c344dca82/backend"
        token=login
        headers={"Authorization":f"Bearer {token}"}
        data={"authType":"Bearer token","url":"https://api.testsprite.com/project","credential":"eyJraWQiOiJZdVdzbm9zcXNVS09nNnNGUGRkZjE1M0J3cVQ5Z2V6dnR3YitPcFwvVU1vST0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhNGY4NjQ2OC01MDYxLTcwMDktZGMyYS1mZGQ4MzJlNzVkNGUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV81b2ozQnYzT2IiLCJjbGllbnRfaWQiOiI1anZtZWpjc2NsYXN2dW9tczI4YXR0ZTBlbiIsIm9yaWdpbl9qdGkiOiIzZDU1NTUxOC00ZjZiLTQwNmEtYTIzNi04ZGNiMjhmNmRjYTYiLCJldmVudF9pZCI6ImQxYmU5MWE0LTBlNTItNDA4NS04ZDg1LTY3Nzg2ODQ4MmY2OCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjQzMTk1NzgsImV4cCI6MTc2NDY1Mzg3MiwiaWF0IjoxNzY0NjUwMjcyLCJqdGkiOiI0OThlMzBiOS1mYzU5LTRjMjctOTkzOC00ZjNiNGFlOTNkOGEiLCJ1c2VybmFtZSI6ImE0Zjg2NDY4LTUwNjEtNzAwOS1kYzJhLWZkZDgzMmU3NWQ0ZSJ9.KljTgZpA7He37CwyrotNekSDECrkkZ48BeiUW5gJSy4pEQJKEl9upbljI3QeyJHUBqftWSu9ZqjoQja_bxahuyDhHpbTACA_YF1IARL3W4wkQoRltq5eQUYK9PBz4LIuhiov4F0FNNFamnBv0RcH7zjwsjw2jgAbPoJrX80O7e5ryYETJTZL7afZlpvncC8lJ6rKiBvWF67HvXidXI93vUu1SNu_ifW4Nb9c_w7WK2U_91GhdxDiPk7tO5vaCFCLkt9aZygGaYv-5gZS_uI9Y9Qj70inSaiixuynUZ8hoOPN06H_Y_Hr9B6p_kbkUTxA8Zn0QacGxx_JZ2NOv9dSYg","name":"项目接口","requirements":"","projectId":"d9f84019-1813-4e24-b6f1-527c344dca82"}
        response = requests.post(url,headers=headers,json=data).text
        print(response)
        assert "项目接口" in response
    