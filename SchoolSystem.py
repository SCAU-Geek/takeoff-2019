
import requests
import request
import time
import re;
import json
import webbrowser
headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'app': 'PCWEB',
        'Connection': 'keep-alive',
        'Content-Length': '90',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie':'',
        'Host': 'jwxt.scau.edu.cn',
        'KAPTCHA-KEY-GENERATOR-REDIS': 'securityKaptchaRedisServiceAdapter',
        'locale': 'zh_CN',
        'Origin': 'http://jwxt.scau.edu.cn',
        'Referer': 'http://jwxt.scau.edu.cn/Njw2017/login.html',
        'Simulated-By': '',
        'TOKEN': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'userAgent': '',
        'userRoleCode': '',
        'X-Requested-With': 'XMLHttpRequest'
}
#后期如果发现问题就加上Cookie  token=; SESSION=cba3ff03-67e8-47fc-bf21-47276cfb5ecc
def Postime():
    url = 'http://jwxt.scau.edu.cn/secService/login'
    userCode = input('请输入账号：')
    password = input('请输入密码：')

    data = {
        'userCode': userCode, 'password': password, 'kaptcha': "testa", 'userCodeType': "account"
    }
    dumpJsonData = json.dumps(data)
    res = requests.post(url, data=dumpJsonData, headers=headers)

    CookieJar = requests.utils.dict_from_cookiejar(res.cookies)
    Cookie = 'token='+CookieJar['token']+';SESSION='+CookieJar['SESSION']
    headers['Cookie'] = Cookie
    return res.json()["data"]['token']

def GetTable(token):
    headers['TOKEN'] = token#加上刚获取的Token
    Tabel_Url = 'http://jwxt.scau.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchClassXskbList?resourceCode=XSMH0311&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchClassXskbList'
    Tabel_Personal_Url = 'http://jwxt.scau.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchOneXskbList?resourceCode=XSMH0701&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchOneXskbList'
    data = {
        'jczy013id': "2019-2020-1",
        'pkgl002id': "",
        'sfck': "1",
        'zt': "2",
    }
    dumpJsonData = json.dumps(data)
    res = requests.post(Tabel_Personal_Url, data=dumpJsonData, headers=headers)
    #print(res.text)
    return res.text

def GetDetail(Content):#用于打印课程名字，测试用
    pattern = re.compile('"kc_name":"(.*?)"')
    text = re.findall(pattern, Content)
    for eachclass in text:
        print(eachclass)
    #print(text)






Pattern_FindPiece = re.compile('{(.*?)}')
Pattern_FindName = re.compile('"kc_name":"(.*?)"')
Pattern_FindClassRoom = re.compile('"js_name":"(.*?)"')
Pattern_FindTeacher = re.compile('"teachernames":"(.*?)"')
Pattern_FindTime = re.compile('"pksj":"(.*?)"')
Pattern_FindWeek = re.compile('"pkzcmx":"(.*?)"')



def Collect_Data(Content):
    Data_List = []
    ClassElement = re.findall(Pattern_FindPiece, Content)
    #print(ClassElement)
    for Element in ClassElement:
        Data_Piece = []
        ClassName = re.findall(Pattern_FindName, Element)
        ClassRoom = re.findall(Pattern_FindClassRoom, Element)
        Teacher = re.findall(Pattern_FindTeacher, Element)
        Time = re.findall(Pattern_FindTime, Element)
        Week = re.findall(Pattern_FindWeek, Element)

        TimeDetail = "星期" + str(int(int(Time[0]) / 10000)) + "的第" + str(int(int(Time[0]) % 10000 / 100)) + "节到" + str(
            int(int(Time[0]) % 100)) + "节"

        if int(Time[0])<1000000:
            Day = int(int(Time[0]) / 10000)
            Start_Time = int(int(Time[0]) % 10000 / 100)
            End_Time = int(int(Time[0]) % 100)
        else:
            Day = int(int(Time[0]) / 1000000)
            Start_Time = int(int(Time[0]) % 100000 / 1000)
            End_Time = int(int(Time[0]) % 100)


        Time_List = []
        Time_List.append(Day)
        Time_List.append(Start_Time)
        Time_List.append(End_Time)

        Week_Ava = re.findall('\d+', Week[0])
        #print(ClassName, ClassRoom, Teacher, TimeDetail, Week_Ava)

        Data_Piece.append(ClassName[0])#0

        if len(ClassRoom) != 0:#1
            Data_Piece.append(ClassRoom[0])
        else:
            Data_Piece.append("")

        if len(Teacher) != 0:#2
            Data_Piece.append(Teacher[0])
        else:
            Data_Piece.append("")

        Data_Piece.append(Time_List)#3
        Data_Piece.append(Week_Ava)#4

        Data_List.append(Data_Piece)
    return Data_List

def Read_Tabel(Data_List):
    for Element in Data_List:
        if '1' in Element[4]:
            print(Element)

def DoFile(Content_Json):
    Sub_Pattern = re.compile("var classes = (.*?);")
    File = open('ClassTabel_Base.HTML','r',encoding='UTF-8')
    Sub_Content = re.sub(Sub_Pattern,"var classes = "+str(Content_Json)+";",File.read())
    #print(Sub_Content)
    File.close()
    File = open('ClassTabel.HTML','w',encoding='UTF-8')
    File.write(Sub_Content)
    File.close()

def MakeJson(Data_List):
    Content = "["
    for Element in Data_List:
        Ele_Content = "[\"" + Element[0] + "\"," + "\"" + Element[1] + "\"," + "\"" + Element[2] + "\"" + ","
        i = 0;
        if len(Ele_Content[3]) != 0:
            Ele_Content += "" + str(Element[3][0]) + ","
            Ele_Content += "[" + str(Element[3][1]) + "," + str(Element[3][2]) + ""

        Ele_Content += "],"

        Ele_Content += "["

        for Week in Element[4]:
            # print(str(Week))
            Ele_Content += "" + Week + ""
            if Week != Element[4][len(Element[4]) - 1]:
                Ele_Content += ','

        Ele_Content += "]]"
        if Element != Data_List[len(Data_List) - 1]:
            Ele_Content += ',\n'
        # print(Ele_Content)
        Content += Ele_Content
    Content += ']'
    return Content

Token = Postime()
AllContent = GetTable(Token)
#GetDetail(AllContent)

Data_List = Collect_Data(AllContent)
File_Write = open('Data.txt','w')

Content = MakeJson(Data_List)
File_Write.write(str(Content))
File_Write.close()
DoFile(Content)
webbrowser.open('ClassTabel.HTML')