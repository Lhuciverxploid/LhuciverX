import os
import requests
from bs4 import BeautifulSoup
from termcolor import colored
from time import sleep
from texttable import Texttable
import pyfiglet

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def get_social_media_profile(username, platform):
    search_query = f"{platform} {username}"
    url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        profile_urls = [a["href"] for a in soup.find_all("a", href=True) if platform in a["href"]]
        if profile_urls:
            profile_url = profile_urls[0]
            status = colored("Found", "green")
        else:
            profile_url = 'N/A'
            status = colored("Not Found", "red")
        return f"{platform.capitalize()}: {status} {profile_url}"
    else:
        return f"{platform.capitalize()}: Not Found"

def get_social_media_profiles(username):
    platforms = [
        "Facebook",
        "Twitter",
        "Instagram",
        "LinkedIn",
        "YouTube",
        "WhatsApp",
        "TikTok",
        "Capcut",
        "Spotify",
        "GitHub",
        "Pinterest",
    ]

    results = {}
    for platform in platforms:
        result = get_social_media_profile(username, platform)
        results[platform] = result

    return results

def main_menu():
    clear_screen()
    title = pyfiglet.figlet_format("Grey Hat OSINT")
    print(colored(title, "blue"))
    print("Disclaimer: Harap digunakan dengan etika. Jangan digunakan untuk aktivitas ilegal atau melanggar hukum.\n")
    print("Pilih opsi:")
    print("1. Cari Profil Media Sosial")
    print("0. Keluar")
    choice = input("Masukkan nomor opsi: ")
    return choice

def display_results(results):
    table = Texttable()
    table.add_row(["Platform", "Status", "Profile URL"])
    for platform, result in results.items():
        platform_name, status, profile_url = result.split(' ')
        table.add_row([platform_name, status, profile_url])
    print(table.draw())
    print("\n1. Kembali ke Menu Utama")
    print("0. Keluar")

def display_loading():
    for i in range(4):
        sleep(0.5)
        print("Mencari...")
        sleep(0.5)
        clear_screen()
    print("Mencari...")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            clear_screen()
            print("Cari Profil Media Sosial")
            print("Masukkan username yang ingin dicari di media sosial:")
            username = input()
            display_loading()
            results = get_social_media_profiles(username)
            while True:
                clear_screen()
                display_results(results)
                back_choice = input("Masukkan nomor opsi: ")
                if back_choice == '1':
                    break
                elif back_choice == '0':
                    clear_screen()
                    print("Terima kasih telah menggunakan Grey Hat Hacker OSINT Tool.")
                    return
                else:
                    print("Opsi tidak valid. Silakan pilih opsi yang sesuai.")
        elif choice == '0':
            clear_screen()
            print("Terima kasih telah menggunakan Grey Hat Hacker OSINT Tool.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih opsi yang sesuai.")

if __name__ == "__main__":
    main()
