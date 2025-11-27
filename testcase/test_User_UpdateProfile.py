import allure
import requests

#用例名称：个人中心个人信息获取成功
#功能名称
@allure.feature("个人中心模块")
# 子功能名称
@allure.story("个人中心模块个人信息")
# 用例命名
@allure.title("个人中心模块个人信息更新成功")
class Test_Profile():
    def test_User_UpdateProfile(self):
        url = "https://api.testsprite.com/user/me"
        headers={"Authorization":"Bearer eyJraWQiOiJZdVdzbm9zcXNVS09nNnNGUGRkZjE1M0J3cVQ5Z2V6dnR3YitPcFwvVU1vST0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhNGY4NjQ2OC01MDYxLTcwMDktZGMyYS1mZGQ4MzJlNzVkNGUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV81b2ozQnYzT2IiLCJjbGllbnRfaWQiOiI1anZtZWpjc2NsYXN2dW9tczI4YXR0ZTBlbiIsIm9yaWdpbl9qdGkiOiJkZWY1MjlkYS04MDEwLTQxOGMtYjY1NC1hOWNjZWU4YjE3MzMiLCJldmVudF9pZCI6IjYyMmUxOTZmLWE3OWMtNDEzMC05NDRlLWZkN2QyN2MyN2Y4ZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NjQyNDUzNDEsImV4cCI6MTc2NDI1MzM0NCwiaWF0IjoxNzY0MjQ5NzQ0LCJqdGkiOiJiYWM5NDdjYi0zMGU2LTQwMGQtYTg5NS0yNDdmM2QwNTNiMjYiLCJ1c2VybmFtZSI6ImE0Zjg2NDY4LTUwNjEtNzAwOS1kYzJhLWZkZDgzMmU3NWQ0ZSJ9.jkgweZ4K91eTsJRlpcDTTZ7Uq3Fy9HFKJpLJ4L1xq34hF7HFSZEa6wjJ6-MNVqX6kTs64Nc2ERrXuTpy3stgqeS_FXCJwprwiMk0CT1Z-zi6S47WH5owtVaNG-aJrsctsB4i1j0hw5AOi8QEloe--V4zl_tFZn97j4mjIvNZGlW0jY2ZdxkBYrppcgFok8vAGXYhCv4WPCVzDmHynQBmgemJiIh2OwphQZdS78DTxbqJuF1T4HJx3lUGVdxZZL-mevDK13Z0TQCZanBxpSPqBpVYyQTWm9c6_7KbQHmgFTcxhkXF5PqlgGr-g931y29-wZi3FdNbei8iTtZRsazGRQ"}
        data={"firstName":"wan","lastName":"li","company":"testsprite"}
        response = requests.put(url,headers=headers,json=data).text
        print(response)
        assert "wan" in response
    