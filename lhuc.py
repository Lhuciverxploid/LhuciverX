import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import re
from termcolor import colored
import subprocess
import webbrowser
import curses
import time
import json
from twilio.rest import Client

# Fungsi untuk menampilkan animasi selamat datang
def show_welcome_animation(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Sembunyikan kursor
    stdscr.refresh()
    height, width = stdscr.getmaxyx()

    welcome_text = "Selamat datang di Tools LhuciverX"
    author_text = "Dikembangkan oleh Lhuciver"
    api_text = "Yang di bantu oleh asisten support"

    welcome_y = height // 2
    welcome_x = width // 2 - len(welcome_text) // 2
    author_y = welcome_y + 1
    author_x = width // 2 - len(author_text) // 2
    api_y = author_y + 1
    api_x = width // 2 - len(api_text) // 2

    stdscr.addstr(welcome_y, welcome_x, welcome_text)
    stdscr.addstr(author_y, author_x, author_text)
    stdscr.addstr(api_y, api_x, api_text)

    stdscr.refresh()
    time.sleep(3)

    # Munculkan menu utama
    stdscr.clear()
    stdscr.refresh()
    
# Fungsi untuk menghasilkan User-Agent secara acak
def generate_random_user_agents(count):
    ua = UserAgent()
    user_agents = [ua.random for _ in range(count)]
    return user_agents

# Fungsi untuk menampilkan User-Agent yang dihasilkan dan menyimpannya ke dalam file
def display_and_save_user_agents(user_agents):
    for idx, user_agent in enumerate(user_agents, start=1):
        print(f"{idx}. {user_agent}")

    # Menyimpan User-Agent ke dalam file
    save_user_agents_to_file(user_agents)

# Fungsi untuk menyimpan User-Agent ke dalam file
def save_user_agents_to_file(user_agent_list):
    with open("user_agents.txt", "a") as file:  # Menggunakan mode "a" untuk append
        for user_agent in user_agent_list:
            file.write(user_agent + "\n")
    print("User-Agent telah disimpan ke dalam file user_agents.txt")

# Fungsi untuk menghasilkan daftar proxy IP
def generate_proxy_list(count):
    proxy_list = []
    url = "https://www.proxy-list.download/HTTPS"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')
        for row in rows[1:count+1]:
            columns = row.find_all('td')
            ip = columns[0].text
            port = columns[1].text
            proxy = f"{ip}:{port}"
            proxy_list.append(proxy)
    return proxy_list

# Fungsi untuk menampilkan daftar proxy IP yang dihasilkan dan menyimpannya ke dalam file
def display_and_save_proxies(proxy_list):
    for idx, proxy in enumerate(proxy_list, start=1):
        print(f"{idx}. {proxy}")

    # Menyimpan proxy IP ke dalam file
    save_proxy_to_file(proxy_list)

# Fungsi untuk menyimpan proxy IP ke dalam file
def save_proxy_to_file(proxy_list):
    with open("proxy_ips.txt", "a") as file:  # Menggunakan mode "a" untuk append
        for proxy in proxy_list:
            file.write(proxy + "\n")
    print("Proxy IP telah disimpan ke dalam file proxy_ips.txt")

# Fungsi untuk menghasilkan daftar proxy IP secara acak
def generate_random_proxy(count):
    proxy_ips = generate_proxy_list(count)
    random_proxies = random.sample(proxy_ips, count)
    return random_proxies

# Fungsi untuk menampilkan informasi geolokasi IP
def show_ip_geolocation(ip):
    # Validasi alamat IP menggunakan ekspresi reguler
    if not re.match(r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", ip):
        print("Maaf, alamat IP tidak valid. Mohon masukkan dengan benar.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if 'loc' in data:
                print("\n╭─────── Geolocation IP Address ───────╮")
                print(f"│ IP Address: {data['ip']}")
                print(f"│ City: {data.get('city', 'N/A')}")
                print(f"│ Region: {data.get('region', 'N/A')}")
                print(f"│ Country: {data.get('country', 'N/A')}")
                print(f"│ Location: {data.get('loc', 'N/A')}")
                print(f"│ Organization: {data.get('org', 'N/A')}")
                print(f"│ Timezone: {data.get('timezone', 'N/A')}")
                print(f"│ Postal: {data.get('postal', 'N/A')}")
                print(f"│ ASN: {data.get('asn', 'N/A')}")
                print("╰───────────────────────────────────────╯")

                # Buka Google Maps dengan lokasi IP
                location = data.get('loc', '0,0')
                maps_url = f"https://www.google.com/maps?q={location}"
                webbrowser.open_new_tab(maps_url)
            else:
                print("Tidak dapat mengambil informasi geolokasi untuk IP ini.")
        else:
            print(f"Terjadi masalah saat mengambil data geolokasi. Kode status: {response.status_code}")

        input("\nTekan Enter untuk melanjutkan...")
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil data geolokasi: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")

# Fungsi untuk menampilkan animasi ketikan teks
def draw_typing_animation(stdscr):
    # Teks animasi yang akan ditampilkan
    animation_text = "Selamat datang di Tools LhuciverX"

    stdscr.clear()
    curses.curs_set(0)
    stdscr.refresh()
    height, width = stdscr.getmaxyx()

    # Tengah-tengahkan teks animasi di layar
    welcome_y = height // 2
    welcome_x = width // 2 - len(animation_text) // 2

    # Loop melalui karakter dalam teks animasi dan menampilkannya satu per satu
    for i in range(1, len(animation_text) + 3):
        stdscr.addstr(welcome_y, welcome_x, animation_text[:i], curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.10)

    stdscr.getch()
    show_welcome_animation(stdscr)  # Menampilkan animasi selamat datang

# Fungsi untuk memeriksa URL dengan Google Safe Browsing API
def check_url_with_google_safe_browsing(url):
    api_key = "AIzaSyDeZ3Z53qxbUtu6tf5ERojfeUQLJ4GLUv4"  # Ganti dengan API key Anda

    url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    request_data = {
        "client": {
            "clientId": "your-client-id",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    try:
        response = requests.post(url, json=request_data)
        if response.status_code == 200:
            data = response.json()
            if 'matches' in data:
                return "URL ini terdeteksi sebagai berbahaya."
            else:
                return "URL ini tidak terdeteksi sebagai berbahaya."
        else:
            return "Terjadi masalah saat memeriksa URL."
    except requests.exceptions.RequestException as e:
        return f"Gagal memeriksa URL: {str(e)}"

# Fungsi untuk memindai file dengan antivirus
def scan_file_for_viruses(file_path):
    try:
        command = ["clamscan", "-i", file_path]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Terjadi kesalahan saat memindai file {file_path}.")

    input("\nTekan Enter untuk melanjutkan...")

# Fungsi untuk menghasilkan daftar proxy IP secara acak
def generate_random_proxy(count):
    proxy_ips = generate_proxy_list(count)
    random_proxies = random.sample(proxy_ips, count)
    return random_proxies
    
# Fungsi untuk mengunduh file dari URL menggunakan wget
def download_file_with_wget(url, output_directory):
    command = ["wget", url, "-P", output_directory]
    try:
        subprocess.run(command, check=True)
        print(f"File dari {url} berhasil diunduh ke {output_directory}")
    except subprocess.CalledProcessError:
        print(f"Terjadi kesalahan saat mengunduh dari {url}")

# Teks banner
banner = """
   __   _                   _                    __  __
  / /  | |__   _   _   ___ (_)__   __  ___  _ __ \ \/ /
 / /   | '_ \ | | | | / __|| |\ \ / / / _ \| '__| \  / 
/ /___ | | | || |_| || (__ | | \ V / |  __/| |    /  \ 
\____/ |_| |_| \__,_| \___||_|  \_/   \___||_|   /_/\_\
                                                       
Yt        : https://youtube.com/@Lhuciver?si=R4ParqpiLPmRNDTF
Github    : https://github.com/Lhuciverxploid
          : https://github.com/maou9990
"""

# Teks menu
menu_items = [
    "[1] Generate User-Agent", "[2] Generate Proxy IP", "[3] Show IP Geolocation",
    "[4] Check URL in Blacklist", "[5] Scan File for Viruses", "[6] Download File with wget",
    "[7] Exit"
]

# Mencari lebar maksimum menu
menu_width = max(len(item) for item in menu_items)

# Mewarnai menu dan membagi menjadi dua baris
menu_items = [colored(item.ljust(menu_width), "blue") for item in menu_items]
menu_items_first_row = menu_items[:4]
menu_items_second_row = menu_items[4:]

# Membuat banner2
banner2 = f"""
   {menu_items_first_row[0]} {menu_items_first_row[2]}
   {menu_items_first_row[1]} {menu_items_first_row[3]}

   {menu_items_second_row[0]} {menu_items_second_row[2]}
   {menu_items_second_row[1]} {menu_items_second_row[3]}
"""

# Menampilkan animasi masuk dan menu
if __name__ == "__main__":
    curses.wrapper(draw_typing_animation)
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(banner)
        print(banner2)
        pilihan = input("pilih salah satu > ")

        if pilihan == "1":
            jumlah_user_agent = int(input("Masukkan jumlah User-Agent yang ingin Anda buat: "))
            user_agents = generate_random_user_agents(jumlah_user_agent)
            display_and_save_user_agents(user_agents)
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            jumlah_proxy = int(input("Masukkan jumlah proxy IP yang ingin Anda buat (maksimal 25): "))
            if jumlah_proxy <= 25:
                proxy_list = generate_random_proxy(jumlah_proxy)
                display_and_save_proxies(proxy_list)
                input("\nTekan Enter untuk melanjutkan...")
            else:
                print("Jumlah proxy yang diminta melebihi batas (maksimal 25).")
                input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "3":
            ip = input("Masukkan alamat IP yang ingin Anda periksa: ")
            show_ip_geolocation(ip)

        elif pilihan == "4":
            url = input("Masukkan URL yang ingin Anda periksa: ")
            result = check_url_with_google_safe_browsing(url)
            print(result)
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "5":
            file_path = input("Masukkan path ke file yang ingin Anda periksa: ")
            scan_file_for_viruses(file_path)
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "6":
            url_to_download = input("Masukkan URL file yang ingin Anda unduh: ")
            output_dir = input("Masukkan direktori tempat Anda ingin menyimpan file yang diunduh (contoh: /home/user/downloads/): ")
            download_file_with_wget(url_to_download, output_directory)
            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "7":
            exit()