import requests
import json
import datetime
def getData():
    week = int(datetime.datetime.now().strftime("%W")) - int(datetime.datetime(2019, 8, 30).strftime("%W"))
    headers={
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'jwxt.scau.edu.cn',
        'Accept': 'application/json, text/plain, */*',
        'app': 'PCWEB',
        'KAPTCHA-KEY-GENERATOR-REDIS': 'securityKaptchaRedisServiceAdapter',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://jwxt.scau.edu.cn',
        'Cookie' : 'Hm_lvt_6fb0b7f7d88b00392194afa0d655b1b2=1559405886; UM_distinctid=16c3131c137819-015a0d23a7e73e-4d045769-1fa400-16c3131c13824a; SESSION=11ef5284-faf8-410b-87e7-9e34039835e4; token=',
        'Connection' : 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',

           }

    data = {
        'userCode' : '201825010216',
        'password' : 'Jack000920',
        "kaptcha": "testa",
        "userCodeType": "account"
}
    payload = {
        "jczy013id": "2019-2020-1",
        "pkgl002id": "W13414710000WH",
        "zt": "2",
        "pkzc": str(week)
    }
    url = 'http://jwxt.scau.edu.cn/secService/login'
    coureseurl = 'http://jwxt.scau.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchOneXskbList?resourceCode=XSMH0701&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchOneXskbList/'
    session = requests.Session()
    res = session.post(url=url, headers=headers, data=json.dumps(data))

    #print(res.text)
    nei = res.json()
    #print(nei)
    headers["TOKEN"] = nei["data"]["token"]
    response = session.post(url = coureseurl,headers = headers,data = json.dumps(payload))

    #print(response)
    session.close()
    return response.json()

def getCourse(data, week):
    course = []
    for e in data:
        if e['pksjmx'][0] == str(week):
            element = {}
            element['time'] = e['pksjshow']
            element['classname'] = e['kc_name']
            element['teacher'] = e['teachernames']
            element['position'] = e['js_name_1']
            course.append(element)
    return course


def getNextCourse(user, passwd):
    weekDay = (datetime.datetime.now().weekday()+1)%7 + 1
    data = getData()
    return getCourse(data["data"], weekDay)


if __name__ == "__main__":
    print(getNextCourse("55", "55"))