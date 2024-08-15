import os
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests
from os import system as none
b="\033[1;34m"#----------𝗯𝗹𝘂𝗲
bl="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄
w="\033[1;37m"#----------𝘄𝗵𝗶𝘁𝗲 {𝗲𝗻𝗱}
try:
    import phonenumbers
except ImportError:
    os.system('pip install phonenumbers')
    import phonenumbers
from phonenumbers import carrier, geocoder, timezone

logo = f'''{r}
 _   _ _   ____  _________ ___________   _____ _   _ ______ _____ 
| \ | | | | |  \/  || ___ \  ___| ___ \ |_   _| \ | ||  ___|  _  |
|  \| | | | | .  . || |_/ / |__ | |_/ /   | | |  \| || |_  | | | |
| . ` | | | | |\/| || ___ \  __||    /    | | | . ` ||  _| | | | |
| |\  | |_| | |  | || |_/ / |___| |\ \   _| |_| |\  || |   \ \_/ /
\_| \_/\___/\_|  |_/\____/\____/\_| \_|  \___/\_| \_/\_|    \___/ 

              {g}|| Coded By : Team Cicada3301 ||
'''

url = "https://your-suyaib.xyz/TrueCaller.php"
key = 'suyaib'

def fetch_name_from_api(phone_number):
    """API থেকে নাম সংগ্রহের জন্য ফাংশন"""
    params = {'number': phone_number, 'key': key}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                name_value = item.get("name", "N/A")
                return f"{r}[{w}+{r}] {w}Name                 : {name_value}"
        else:
            return f"{r}[{w}+{r}] {w}Name                 : Not Found"
    except requests.RequestException:
        return f"{r}[{w}+{r}] {w}Name                 : Not Found{w}"

def clr():
    os.system('clear')

def number():
    clr()
    print(logo)
    user_phone = input("\n\n\n<\\\> ENTER YOUR NUMBER : ")
    name_output = fetch_name_from_api(user_phone)

    default_region = "ID"
    
    try:
        parsed_number = phonenumbers.parse(user_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)
        
        print(f"{p}\n========== SHOW INFORMATION PHONE NUMBERS ==========")
        print(name_output)
        print(f"{r}[{w}+{r}] {w}Location             : {location}")
        print(f"{r}[{w}+{r}] {w}Region Code          : {region_code}")
        print(f"{r}[{w}+{r}] {w}Timezone             : {timezoneF}")
        print(f"{r}[{w}+{r}] {w}Operator             : {jenis_provider}")
        print(f"{r}[{w}+{r}] {w}Valid number         : {is_valid_number}")
        print(f"{r}[{w}+{r}] {w}Possible number      : {is_possible_number}")
        print(f"{r}[{w}+{r}] {w}International format : {formatted_number}")
        print(f"{r}[{w}+{r}] {w}Mobile format        : {formatted_number_for_mobile}")
        print(f"{r}[{w}+{r}] {w}Original number      : {parsed_number.national_number}")
        print(f"{r}[{w}+{r}] {w}E.164 format         : {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"{r}[{w}+{r}] {w}Country code         : {parsed_number.country_code}")
        print(f"{r}[{w}+{r}] {w}Local number         : {parsed_number.national_number}")
        
        number_type_str = "unknown"
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            number_type_str = "This is a mobile number"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            number_type_str = "This is a fixed-line number"
        print(f"{r}[{w}+{r}] {w}Type                 : {number_type_str}")
        
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing number: {e}")

if __name__ == "__main__":
    none('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n'+' '+'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'t'+'.'+'m'+'e'+'/'+'D'+'a'+'r'+'k'+'T'+'e'+'a'+'m'+'T'+'e'+'r'+'m'+'u'+'x'+'E'+'x'+'p'+'l'+'o'+'r'+'a'+'t'+'i'+'o'+'n')
    number()

    