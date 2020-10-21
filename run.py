#-*-coding:utf-8-*-
from read_write_excel import read_data
from http_request import http_request
from read_write_excel import write_data
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

# 函数内的变量 --局部的  函数外的 --全局的
Token=None#全局变量，初始值设置为None
def run(file_name,sheet_name,c1,c2):
    global Token#在这里声明 函数外的Token 和函数内的Token是同一个值
    # 获取到所有的测试数据
    all_case=read_data(file_name,sheet_name)
    print('获取到所有测试数据为：',all_case)

    for test_data in all_case:#在http_request进行请求的时候，判断是否是登录请求
        # if test_data[1]=='登录':#判断两边是否相等 比较运算符
        ip = "http://120.78.128.25:8766"
        response=http_request(ip + test_data[4],eval(test_data[5]),token=Token,method=test_data[3])
        if 'login' in test_data[4]:#成员运算符
            #它就是一个登录的用例
            Token="Bearer "+response['data']['token_info']['token']
        print('最后的结果值：',response)

        #开始写入结果
        write_data(file_name,sheet_name,test_data[0]+1,c1,str(response))

        #进行判断，期望值与实际值是否相等，判断这个用例是否执行通过
        actual={'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print('测试用例执行通过')
            write_data(file_name,sheet_name, test_data[0] + 1, c2, 'PASS')
        else:
            print('测试用例执行不通过')
            write_data(file_name,sheet_name, test_data[0] + 1, c2, 'FAIL')

# 调用函数
# 执行充值的接口
run('test_case_recharge.xlsx','recharge',8,9)

