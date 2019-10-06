import requests
import json
import datetime
"""
功能：获取当周课表
@return json
@param user  字符串  用户名
@param passwd 字符串 用户密码
"""


def getData(user, passwd):
    week = int(datetime.datetime.now().strftime("%W")) - int(
        datetime.datetime(2019, 8, 30).strftime("%W"))
    url1 = 'http://jwxt.scau.edu.cn/secService/login'
    url2 = "http://jwxt.scau.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchOneXskbList?resourceCode=XSMH0701&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchOneXskbList"
    s = requests.session()
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'jwxt.scau.edu.cn',
        'Accept': 'application/json, text/plain, */*',
        'app': 'PCWEB',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://jwxt.scau.edu.cn',
        'KAPTCHA-KEY-GENERATOR-REDIS': 'securityKaptchaRedisServiceAdapter'
    }
    data1 = {
        "userCode": user,
        "password": passwd,
        "kaptcha": "testa",
        "userCodeType": "account"
    }
    data2 = {
        "jczy013id": "2019-2020-1",
        "pkgl002id": "W13414710000WH",
        "zt": "2",
        "pkzc": str(week)
    }
    res = s.post(url=url1, headers=headers, data=json.dumps(data1))
    loginInfo = res.json()
    headers["TOKEN"] = loginInfo["data"]["token"]
    res2 = s.post(url=url2, headers=headers, data=json.dumps(data2))
    # print(res2.text)
    s.close()
    return res2.json()


"""
功能：获取明天课表
@return json
@param data  数组  课表数据
@param week 数字 明天日期(星期几)
"""


def getNextData(data, week):
    course = []
    for e in data:
        if e['pksjmx'][0] == str(week):
            element = {}
            element['time'] = e['pksjshow']
            element['name'] = e['kc_name']
            element['teacher'] = e['teachernames']
            element['position'] = e['js_name_1']
            course.append(element)
    return course


def getNextCourse(user, passwd):
    weekDay = datetime.datetime.now().weekday() + 1
    data = getData(user, passwd)
    return getNextData(data["data"], weekDay)


if __name__ == "__main__":
    print(getNextCourse("55", "55"))