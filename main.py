import requests, random, string
class TIKTOK():
    def __init__(self):
        self.login()
    def login(self):
        username = input("[ + ] username: ")
        password = input("[ + ] password: ")
        time = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now").text
        url = f"https://api2.musical.ly/passport/user/login/?mix_mode=1&username={username}&email=&mobile=&account=&password={password}&captcha=&ts={time}&app_type=normal&app_language=en&manifest_version_code={time}&_rticket={time}083&iid=7025497424882616069&channel=googleplay&language=en&fp=&device_type=ART-L29&resolution=720*1491&openudid={''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}&update_version_code={time}&sys_region=GB&os_api=29&is_my_cn=0&timezone_name=Asia/Amman&dpi=320&carrier_region=JO&ac=wifi&device_id=7019232418121516549&mcc_mnc=41601&timezone_offset=7200&os_version=10&version_code=770&carrier_region_v2=416&app_name=musical_ly&version_name=7.7.0&device_brand=HUAWEI&ssmix=a&build_number=7.7.0&device_platform=android&region=US&aid=1233&as={''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=22))}&cp={''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=22))}&mas={''.join(random.choices(string.ascii_lowercase + string.digits, k=54))}"
        head = {
            "Host": "api2.musical.ly",
            "Connection": "keep-alive", 
            "Content-Length": "127",
            "Accept-Encoding": 'gzip',
            "sdk-version": '1',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-SS-TC": '0',
            "X-SS-RS": '0',
            "User-Agent": f'com.zhiliaoapp.musically/{time} (Linux; U; Android 10; en_GB; ART-L29; Build/HUAWEIART-L29; Cronet/58.0.2991.0)'
        }
        data = {
            "password": password,
            "mix_mode": "1",
            "username": username
        }
        req = requests.post(url, headers=head, data=data)
        #print(req.text)
        if "has_password" in req.text:
            print(f"[ + ] {req.cookies.get('sessionid')} ",end="")
            input()
            exit()
        else:
            print(f"[ - ] {req.text} ", end="")
            input()
            exit()
TIKTOK()
