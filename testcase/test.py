# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2025/11/27  18:10
# 文件名：test.py
from datetime import datetime
import json
import requests
#第一步
url = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_xRhSDsinu"
userinfo = {}
userinfo["AuthFlow"] = "USER_SRP_AUTH"
userinfo["ClientId"]="5jvmejcsclasvuoms28atte0en"
userinfo["AuthParameters"]={"USERNAME":"15213337472@163.com",
                            "SRP_A":"f8f96332d7512818accc853038d8c6148fd62801c3a78e5201b9c50014349539ee8e28fc9f4f8e3b70b15715a228c1244835ebcc729b604c83c77116a1dc8af6ea444647ee5c52fc07cb2e685eecac6488792342ea7d5e9db47a58ebdf5af014d15e284bc8c9b67230640e7decc89cd6188e319d1c9113496657a3be19fc3ae8e09155b400a3bfb5b10c3b8b197d1a6b4059f2de6cf5427b9862b49951adf9c783a55c353e3a6aaaf1563810d72dd4be2b0bbe7d840402a652fe786e19e4742aa35a949fe9fdfb8311e0c063d3ca778f6476f764102e63a87e847c9d3e35504404508318043495c183d0136f85b023cf8fc20023d361cff9edcc6972a4867e9f914860ff76ddb949833dae9f78ec08b2d9c1308cf515c747a530d46997cb31814929d8f1001d2da42571cdf71b2cc0f93198612c6f69b18252189a316f8f7f11965e29f562d38dde8edb9fab470f71a2f11a29fd015d7ad2652a190bdf980d8c9943f494d20f7da722f3bb42759332932318b1bc6585e43fe0ff5dec8bf79d40"}
headers={"Content-Type":"application/x-amz-json-1.1","Amz-Sdk-Invocation-Id":"8826c806-0aea-4806-87f4-ef3dc42df1e3",
         "Amz-Sdk-Request":"attempt=1; max=3","X-Amz-Target":"AWSCognitoIdentityProviderService.InitiateAuth",
         "X-Amz-User-Agent":"aws-amplify/6.15.0 auth/4 framework/2"
         }
data = json.dumps(userinfo)
response = requests.post(url,headers=headers, data=data).text
print(response)
re=json.loads(response)
USERNAME=re['ChallengeParameters']['USERNAME']
print(USERNAME)
PASSWORD_CLAIM_SECRET_BLOCK=re['ChallengeParameters']['SECRET_BLOCK']
print(PASSWORD_CLAIM_SECRET_BLOCK)
#第二步
userinfo1 = {}
userinfo1["ChallengeName"] = "PASSWORD_VERIFIER"
userinfo1["ClientId"]="5jvmejcsclasvuoms28atte0en"
userinfo1["ChallengeResponses"]={"USERNAME":USERNAME,
                            "TIMESTAMP":datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y"),
                            "PASSWORD_CLAIM_SIGNATURE":"H686JW/+GKX0ZS6/kKZyfGPwFY3i9p/GyLKS7iDMzCs=",
                             "PASSWORD_CLAIM_SECRET_BLOCK":PASSWORD_CLAIM_SECRET_BLOCK
                            }
print(userinfo1)
headers1={"Content-Type":"application/x-amz-json-1.1","Amz-Sdk-Invocation-Id":"0c7d5e4a-8e09-4f23-91e7-d18da1549fea",
         "Amz-Sdk-Request":"attempt=1; max=3","X-Amz-Target":"AWSCognitoIdentityProviderService.RespondToAuthChallenge",
         "X-Amz-User-Agent":"aws-amplify/6.15.0 framework/2"
         }
data1 = json.dumps(userinfo1)
response1 = requests.post(url,headers=headers1, data=data1).text
print(response1)



