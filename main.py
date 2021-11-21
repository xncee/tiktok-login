import os
try:
    import requests
except:
    os.system("pip install requests")
    import requests
class TIKTOK():
    def __init__(self):
        email = input("[ + ] Email: ")
        password = input("[ + ] Password: ")
        self.login(email, password)
    def login(self, email, password):
        url = "https://api2.musical.ly/passport/user/login/?mix_mode=1&username=&email=&mobile=&account=&password=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=&iid=7019232418121516549&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*720&openudid=&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=&mas="
        head = {
            "User-Agent": "Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z",
            "Host": "api2.musical.ly",
            "Connection": "keep-alive",
        }
        data = {
            "email": email,
            "password": password
        }
        req = requests.post(url, headers=head, data=data)
        #print(req.text, req.status_code)
        if '"message":"success"' in req.text:
            sessionid = req.json()["data"]["session_key"]
            print(f"[ + ] sessionid -> {sessionid} ", end="")
            input()
            exit()
        else:
            print(f"[ - ] {req.text} ", end="")
            input()
            exit()
TIKTOK()
