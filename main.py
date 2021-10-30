import requests
class TIKTOK():
    def __init__(self):
        self.login()
    def login(self):
        username = input("[ + ] username: ")
        password = input("[ + ] password: ")
        time = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now").text
        url = f"https://api2.musical.ly/passport/user/login/?ts={time}&app_type=normal&app_language=en&manifest_version_code=2018101602&_rticket=1635625566105&iid=7024958041209456390&channel=googleplay&language=en&fp=&device_type=ART-L29&resolution=720*1491&openudid=5da894062bfc39fa&update_version_code=2018101602&sys_region=GB&os_api=29&is_my_cn=0&timezone_name=Asia%2FAmman&dpi=320&carrier_region=JO&ac=wifi&device_id=7019232418121516549&mcc_mnc=41601&timezone_offset=7200&os_version=10&version_code=872&carrier_region_v2=416&app_name=musical_ly&version_name=8.7.2&device_brand=HUAWEI&ssmix=a&pass-region=1&build_number=8.7.2&device_platform=android&region=US&aid=1233&as=a1060aa7fe1591dacd4355&cp=af581767e9dd79a6e1KuSy&mas=01452bdabfb685155cecc940323eb78e3dacaccc2c26c686268c9c"
        head = {
            "Host": "api2.musical.ly",
            "Connection": "keep-alive", 
            "Content-Length": "127",
            "Cookie": '$Version="1"; store-country-code="jo";$Path="/";$Domain="musical.ly"; store-idc="alisg";$Path="/";$Domain="musical.ly"; odin_tt="f5f35d83bc3377b6552b0613c4089eee04eb4b2cacf2d24b48567e4b710f0fd6fbdcd9dec769a02f7eabc5a24aa78fabd7261a319dad737a4af6e25fa752e395a97e099c2a739e64f681372dc01fdf94";$Path="/";$Domain=".musical.ly"; ttreq="1$127cd24da3f12f3c5ffaa16823dd403f2c54dca9";$Path="/";$Domain="musical.ly"; install_id="7024958041209456390";$Path="/";$Domain="musical.ly"',
            "Accept-Encoding": 'gzip',
            "sdk-version": '1',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-SS-TC": '0',
            "X-SS-RS": '0',
            "User-Agent": 'com.zhiliaoapp.musically/2018101602 (Linux; U; Android 10; en_GB; ART-L29; Build/HUAWEIART-L29; Cronet/58.0.2991.0)'
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