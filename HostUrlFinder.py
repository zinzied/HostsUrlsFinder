import sys
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import re
import os
import colorama
from colorama import Fore, Style
from urllib.parse import urlparse
import time

colorama.init()

LIGHTRED = '\033[91m'
YL = '\033[33m'
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Create ASCII art for each part of the text
ascii_art_part1 = pyfiglet.figlet_format("Host")
ascii_art_part2 = pyfiglet.figlet_format("Url")
ascii_art_part3 = pyfiglet.figlet_format("Finder")

# Define the banner function
def banner():
    '''
    Display the banner or header information
    '''
    print(Fore.BLUE + ascii_art_part1)
    print(Fore.LIGHTRED_EX + ascii_art_part2)
    print(Fore.GREEN + ascii_art_part3)
    print(LIGHTRED + " >>>>>>>>>>>>>>>>>>>>>>>>By Zinzied  \n")
    print(Fore.YELLOW + "[ JS ] " + Fore.CYAN + "[ PHP ]" + Fore.MAGENTA + "[ IMG ]" + YL + "[ HTML ]" + Fore.GREEN + "[ HOST ]\n")

def usage():
    '''
    Show the usage of the app
    '''
    scr = os.path.basename(sys.argv[0])
    banner()
    print(Fore.CYAN + f"python {scr} URL")

def start(argv):
    if len(argv) < 1:
        usage()
        sys.exit()
    url = argv[0]
    o = urlparse(url)
    if o.scheme not in ['http', 'https', 'ftp']:
        banner()
        print(Fore.RED + "[!] Please check your URL. It should start with http://, https://, or ftp://")
        sys.exit(0)
    banner()
    report(url)

def searchLinks(url):
    '''
    Search for all the URLs with http:// or https:// regex and all the <a href=""> tags
    '''
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = urllib.request.Request(url, headers=headers)
        website = urllib.request.urlopen(req)
        html = website.read()
        soup = BeautifulSoup(html, 'lxml')
        # Use re.findall to get all the links with http:// or https:// URL
        mylinks = []

        # Find all the href links in <a> tags
        for link in soup.find_all('a', href=True):
            mylinks.append(link['href'])
        # Remove the redundant links
        k = list(dict.fromkeys(mylinks))
        return k
    except urllib.error.URLError as e:
        print(Fore.RED + f"[!] Failed to open URL: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"[!] An unexpected error occurred: {str(e)}")
        sys.exit(1)

def report(url):
    '''
    Show the final results with the extension of the URL
    '''
    js_ = 0
    PHP_ = 0
    IMG = 0
    hosts = 0
    html = 0
    links = searchLinks(url)
    with open("report.txt", "w", encoding="utf-8") as file:  # Specify UTF-8 encoding here
        for link in links:
            if 'js' in link:
                print(Fore.YELLOW + "[{time}] -[ JS ] - {mylink}".format(mylink=link, time=time.strftime("%H:%M:%S")))
                file.write("[{time}] -[ JS ] - {mylink}\n".format(mylink=link, time=time.strftime("%H:%M:%S")))
                js_ += 1
            elif 'php' in link:
                print(Fore.CYAN + "[{time}] -[ PHP ] - {mylink}".format(mylink=link, time=time.strftime("%H:%M:%S")))
                file.write("[{time}] -[ PHP ] - {mylink}\n".format(mylink=link, time=time.strftime("%H:%M:%S")))
                PHP_ += 1
            elif 'jpg' in link or 'png' in link or 'jpeg' in link:
                print(Fore.MAGENTA + "[{time}] -[ IMG ] - {mylink}".format(mylink=link, time=time.strftime("%H:%M:%S")))
                file.write("[{time}] -[ IMG ] - {mylink}\n".format(mylink=link, time=time.strftime("%H:%M:%S")))
                IMG += 1
            elif 'html' in link:
                print(YL + "[{time}] -[ HTML ] - {mylink}".format(mylink=link, time=time.strftime("%H:%M:%S")))
                file.write("[{time}] -[ HTML ] - {mylink}\n".format(mylink=link, time=time.strftime("%H:%M:%S")))
                html += 1
            else:
                print(Fore.GREEN + "[{time}] - [ host ] - {mylink}".format(mylink=link, time=time.strftime("%H:%M:%S")))
                file.write("[{time}] - [ host ] - {mylink}\n".format(mylink=link, time=time.strftime("%H:%M:%S")))
                hosts += 1
        print(">>>>>>>>>>>>>>> Report <<<<<<<<<<<<<<<<<<")
        print(Fore.WHITE + " URL => " + url)
        print(Fore.WHITE + "[TOTAL] => [ JS = {js} ] - [ PHP = {php} ] - [ IMG = {img} ] - [ HTML = {html} ] - [ HOSTs = {hosts} ]".format(js=js_, php=PHP_, img=IMG, hosts=hosts, html=html))
        file.write(">>>>>>>>>>>>>>> Report <<<<<<<<<<<<<<<<<<\n")
        file.write(" URL => " + url + "\n")
        file.write("[TOTAL] => [ JS = {js} ] - [ PHP = {php} ] - [ IMG = {img} ] - [ HTML = {html} ] - [ HOSTs = {hosts} ]\n".format(js=js_, php=PHP_, img=IMG, hosts=hosts, html=html))

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting... :)")
        sys.exit(0)