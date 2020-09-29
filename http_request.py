#-*-coding:utf-8-*-
import requests
def http_request(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization':token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)
    else:
        result = requests.post(url, json=data, headers=header)
    # print(result.json())#输出到控制台
    return result.json()#return返回指定得结果

if __name__ == '__main__':

#调用函数

    # 注册
    reg_url="http://120.78.128.25:8766/futureloan/member/register"
    reg_data={'mobile_phone':'18987654321','pwd':'123456789'}
    http_request(reg_url,reg_data)

    # 登录
    login_url="http://120.78.128.25:8766/futureloan/member/login"
    login_data={'mobile_phone':'18987654321','pwd':'123456789'}
    response=http_request(login_url,login_data)
    print('登录的结果是：{}'.format(response))
    # 充值
    token=response['data']['token_info']['token']
    rec_url="http://120.78.128.25:8766/futureloan/member/recharge"
    rec_data={'member_id':'57848','amount':'100'}
    print(http_request(rec_url,rec_data,"Bearer "+token))
