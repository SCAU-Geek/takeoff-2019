import requests
import json
import time


def getnextdate():
	ticks = time.time()
	print(ticks)

def getdata(number,password,weeknumber):
	login_url = "http://jwxt.scau.edu.cn/secService/login"
	course_url = "http://jwxt.scau.edu.cn/resService/jwxtpt/v1/xsd/xsdqxxkb_info/searchOneXskbList?resourceCode=XSMH0701&apiCode=jw.xsd.xsdInfo.controller.XsdQxxkbController.searchOneXskbList"

	payloadData ={"userCode":number,"password":password,"kaptcha":"testa","userCodeType":"account"}

	'''登陆头'''
	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Encoding': 'gzip, deflate',
        'app': 'PCWEB',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'jwxt.scau.edu.cn',
        'KAPTCHA-KEY-GENERATOR-REDIS': 'securityKaptchaRedisServiceAdapter',
        'Origin': 'http://jwxt.scau.edu.cn',
        'Referer': 'http://jwxt.scau.edu.cn/Njw2017/login.html',
        'X-Requested-With': 'XMLHttpRequest',
        'cache-control': 'no-cache',  
	}	


	s = requests.session()
	login_response = s.post(login_url , headers = headers , data = json.dumps(payloadData))
	login_session = login_response.cookies.get_dict()['SESSION']

	print(login_session)
	login_response = json.loads(login_response.text)
	token = login_response['data']['token']
	if not token:
		print("密码或学号错误")
		return

	headers['TOKEN']=token
	headers['Cookie'] = f'SESSION={login_session}; token='
	couser_payload = {"jczy013id":"2019-2020-1","pkgl002id":"W13414710000WH","zt":"2","pkzc": weeknumber}
	course_response = s.post(course_url , headers = headers , data = json.dumps(couser_payload))
	#print(course_response.text)
	ddd = json.loads(course_response.text)
	localtime = time.localtime(time.time())
	course = []
	for i in ddd['data']:
		if(int(int(i['pksjmx'][0]))==localtime[6]+2):
			course.append(i)
		#print(i)
	if not course:
		print("明天没有课")
		return
	for i in course:
		print(i['pksjshow'],i['kc_name'],i['js_name_1'])
	return course 	



if __name__ == "__main__":
	'''学号密码以及第几周'''
	number = input("请输入学号")
	password = input("请输入密码")
	week = input("请输入周数")
	getdata(number,password,week)
	