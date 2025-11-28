# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2025/11/28  11:03
# 文件名：test2.py
# -*- coding: utf-8 -*-
import os
import pytest

# 清除代理设置
from pycognito import Cognito
@pytest.fixture(scope="function")
def login():
    global token
    proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']
    for var in proxy_vars:
        os.environ.pop(var, None)

    # 创建Cognito用户
    u = Cognito(
        # 正式环境 us-east-1_5oj3Bv3Ob
        # dev us-east-1_xRhSDsinu
        'us-east-1_5oj3Bv3Ob',  # UserPoolId
        # 正式环境 5jvmejcsclasvuoms28atte0en
        # dev 3u95rhhd6on4t1qad4lf4c0sfk
        '5jvmejcsclasvuoms28atte0en',  # ClientId
        username='15213337472@163.com'  # Username
    )
    try:
        # 进行认证（对应JS的authenticateUser）
        u.authenticate(password='Cs123456.')
        # 获取token
        token = u.access_token
        print("认证成功")
        print(f"Access Token: {token}")
    except Exception as err:
        print(f"认证失败: {err}")
    return token