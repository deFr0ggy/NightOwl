import json
import sys
import os
import re
import colorama
import requests
import socket
import extract_msg
from colorama import Fore, Style
from requests.models import HTTPBasicAuth
colorama.init(autoreset=True)

global count

c_path = os.getcwd()

AbusedIPDB_API = "ENTER YOUR API KEY HERE"

def fileChecker():

    if sys.argv[1].endswith('.msg'):
        msgGrabber(sys.argv[1])
    elif sys.argv[1].endswith('.eml'):
        baseGrabber()
    else:
        print(Fore.RED + "The file is in " + sys.argv[1].split(".")[-1] + " format: " + sys.argv[1])

def msgGrabber(file):

    try:
        print(Fore.CYAN + "[+] File Name: " + file + "\n")
        with extract_msg.openMsg(file) as messageFile:
            print(Fore.GREEN + "[+] From: " + Fore.RESET + str(messageFile.sender))
            print(Fore.GREEN + "[+] To: " + Fore.RESET + str(messageFile.to))
            print(Fore.GREEN + "[+] Subject: " + Fore.RESET  + str(messageFile.subject))
            print(Fore.GREEN + "[+] CC: " + Fore.RESET  + str(messageFile.cc))
            print(Fore.GREEN + "[+] BCC: " + Fore.RESET  + str(messageFile.bcc))
            print(Fore.GREEN + "[+] Email Time: " + Fore.RESET  + str(messageFile.receivedTime))
            if len(messageFile.attachments) > 0:
                print(Fore.GREEN + "[+] Attachment Found - Saving in current directory!\n\n")
                for attachment in messageFile.attachments:
                     attachmentName = attachment.getFilename()
                     print(Fore.CYAN + attachmentName + "\n")
                     attachment.save(customPath= c_path)
            else:
                print(Fore.GREEN + "[+] No Attachments Observed")
            messageBody = str(messageFile.body)
            trucatedBody = messageBody.replace('\r', ' ')
            print(Fore.GREEN + "[+] Email Body\n\n" + Fore.YELLOW + trucatedBody)
            msgIPGrabber(trucatedBody)
            msgEmailGrabber(trucatedBody)
            msgURLGrabber(trucatedBody)
            messageFile.close()
    except:
        print("Something Went Wrong!")


def msgIPGrabber(bodyWell):

        IP = [] 
        IP_COUNT = 0
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',bodyWell)
        
        try:
            if regex is not None:
                for match in regex:
                    if match not in IP:
                        IP.append(match)
                        IP_COUNT += 1
                        print("\n" + str(IP_COUNT) + Fore.Green + " - IP Address: " + match)
        except:
            print("Something Goes Wrong In Grabbing MSG IPs")

def msgEmailGrabber(emailBody):
        
        EMAIL = [] 
        regex = re.findall(r'[\w\.-]+@[\w\.-]+', emailBody)
        
        try:
            if regex is not None:
                print(Fore.GREEN + "[+] Emails Observed In Email Body\n")
                for match in regex:
                    if match not in EMAIL:
                        EMAIL.append(match)
                        print(match)
            print("\n")
        except:
            print("Something Goes Wrong In Grabbing MSG Emails")

def msgURLGrabber(urlFile):

        try:
            print(Fore.GREEN + "[+] URLs Observed\n\n") 
            URL = [] 
            regex = re.findall(r'(http(.*)?://\S+)',urlFile)
            if regex is not None:
                for match in regex:
                    urlFound = str(match)
                    urlFound = re.sub("[(\']", "", urlFound)
                    urlFound = re.sub(">", "", urlFound)
                    urlFound = re.sub("<", "", urlFound)
                    print(urlFound.strip())
        except:
            print("Something Goes Wrong In MSG URL")

def baseGrabber():

    try: 
        print(Fore.BLUE + "-"*50)
        print(Fore.BLUE + "Printing Details You Should Care About!")
        print(Fore.BLUE + "-"*50 + "\n")
        count = 0
        with open(sys.argv[1], "r", encoding="utf-8") as sample:
            for line in sample:
                if line.startswith("From: "):
                    print(Fore.RED + line)
                if line.startswith("To: "):
                    print(Fore.YELLOW + line)   
                if line.startswith("Subject: "):
                    print(Fore.GREEN + line)
                if line.startswith("Date: "):
                    print(Fore.RED + line) 
                if line.startswith("Message-ID: "):
                    print(Fore.GREEN + line)
                if line.startswith("Return-Path:"):
                    print(Fore.YELLOW + line)
                if line.startswith("Return-To:"):
                    print(Fore.GREEN + line)
                if line.startswith("List-Unsubscribe:"):
                    print(Fore.YELLOW + line)
                if line.startswith("Message Body: "):
                    print(Fore.GREEN + line)
                if line.startswith("Received: "):
                    count += 1

        print("+> Total HOPS Count: " + str(count) + "\n")
        emailGrabber()
    except Exception:
        print("Something Went Wrong!")
        exit

def ipGrabber():
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "Printing The Unique IP Addresses Only!")
    print(Fore.BLUE + "-"*50)
    
    try:
        fileOpen = open(sys.argv[1],'r', encoding='utf-8')
        readText = fileOpen.read()
        IP = [] 
        IP_COUNT = 0
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',readText)
        if regex is not None:
            for match in regex:
                if match not in IP:
                    IP.append(match)
                    IP_COUNT += 1
                    print("\n" + str(IP_COUNT) + Fore.YELLOW + " - IP Address: " + match)
    
        urlGrabber()
    except:
        print("Something Went Wrong!")
        exit

def emailGrabber():
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "Butchering Emails!")
    print(Fore.BLUE + "-"*50)

    try:
        fileOpen = open(sys.argv[1],'r', encoding='utf-8')
        readText = fileOpen.read()
        EMAIL = [] 
        regex = re.findall(r'[\w\.-]+@[\w\.-]+', readText)
        if regex is not None:
            for match in regex:
                if match not in EMAIL:
                    EMAIL.append(match)
                    print(Fore.YELLOW + match + "\n")

        ipGrabber()
    except:
        print("Something Went Wrong!")
        exit

def urlGrabber():
    print("\n")
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "Butchering All The URLs!")
    print(Fore.BLUE + "-"*50 + "\n")
    
    try:
        fileOpen = open(sys.argv[1],'r', encoding='utf-8')
        readText = fileOpen.read()
        print(re.search("(?P<url>https?://[^\s]+)", readText).group("url"))  
        URL = [] 

        regex = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]',readText)
        if regex is not None:
            for match in regex:
                if match not in URL:
                    URL.append(match)
                    
        if not URL:
            print(Fore.GREEN + "There were no URLs Found!")
        else:
            print("\n" + Fore.YELLOW + match)
            IP_ADDR = socket.gethostbyname(match)
            print("\n" + "Domain: " + match + "\n" + "IP Address: "+ IP_ADDR)
        
        xHunter()
    
    except:
        print("Something Went Wrong!")
        exit

def embeddedContents():
    print("\n")
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "Checking If There Is Are Any Embedded Contents")
    print(Fore.BLUE + "-"*50)
    contents = []

    try:
        with open(sys.argv[1],'r', encoding='utf-8') as sample:
            for line in sample:
                if line.startswith("Content-Type:"):
                    print(Fore.YELLOW + line)
                if line.startswith("<!DOCTYPE") or line.startswith("<html>") or line.startswith("<meta"):
                    contents.append(line)
                    for line in sample:
                        contents.append(line)
        if not contents:
            print(Fore.GREEN + "There Were No Embedded Contents Found")
        else:
            print(Fore.BLUE + "\n" + "-"*50)
            conscent = input("HTML Contents Found - Do you want to save it? [Y/N]: ")
            print(Fore.BLUE + "-"*50)
            if conscent == "y" or conscent == "Y":
                outfile = input("Provide File Name: ")
                htmlData = open(outfile, "w")
                htmlData.write("".join(contents).strip("\n"))
                htmlData.close
                print("\n")
                print(Fore.BLUE + "-"*50)
                print(Fore.GREEN + "The HTML File is extracted: " + outfile)
                print(Fore.BLUE + "-"*50)
            else:
                exit
    except:
        print("Something Went Wrong!")
        exit

def xHunter():
    print("\n")
    print(Fore.BLUE + "-"*50)
    print(Fore.BLUE + "Printing All The Headers Which Were Added During The Email Travel")
    print(Fore.BLUE + "-"*50 + "\n")

    try:
        with open(sys.argv[1],'r', encoding='utf-8') as sample:
            for line in sample:
                if line.startswith("X-"):
                    print(Fore.YELLOW + line)
    except:
        print("Something Went Wrong!")
        exit
    
    embeddedContents()

    print(Fore.BLUE + "-"*50 + "\n")

def abusedIP(ip):

    print("\n" + Fore.MAGENTA + "ABUSEDIPDB Response!" + "\n")

    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '365'
    }

    headers = {
        'Accept': 'application/json',
        'Key': AbusedIPDB_API
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))

def whoisit(domain):
    print("\n"+ Fore.BLUE +"*"*50)
    print("WHOIS Information - " + domain)
    print("\n"+ Fore.BLUE +"*"*50)
    os.system('whois '+domain)
    print("\n"+ Fore.BLUE +"*"*50+"\n")
   
def banner():

    banner = """
    
██████   █████  ███           █████       █████          ███████                    ████ 
░░██████ ░░███  ░░░           ░░███       ░░███         ███░░░░░███                 ░░███ 
 ░███░███ ░███  ████   ███████ ░███████   ███████      ███     ░░███ █████ ███ █████ ░███ 
 ░███░░███░███ ░░███  ███░░███ ░███░░███ ░░░███░      ░███      ░███░░███ ░███░░███  ░███ 
 ░███ ░░██████  ░███ ░███ ░███ ░███ ░███   ░███       ░███      ░███ ░███ ░███ ░███  ░███ 
 ░███  ░░█████  ░███ ░███ ░███ ░███ ░███   ░███ ███   ░░███     ███  ░░███████████   ░███ 
 █████  ░░█████ █████░░███████ ████ █████  ░░█████     ░░░███████░    ░░████░████    █████
░░░░░    ░░░░░ ░░░░░  ░░░░░███░░░░ ░░░░░    ░░░░░        ░░░░░░░       ░░░░ ░░░░    ░░░░░ 
                      ███ ░███                                                            
                     ░░██████                                                             
                      ░░░░░░                                                              


    OFFLINE PHISHING EMAIL BUTCHER
    Coded by Kamran Saifullah - Frog Man v1.0
    -----------------------------------------
    Usage: ./NightOwl.py <Mices>
    -----------------------------------------
    LinkedIn: https://www.linkedin.com/in/kamransaifullah/
    GitHub: https://github.com/deFr0ggy
    Twitter: https://twitter.com/deFr0ggy
    """

    print(Fore.GREEN + banner + "\n")

def main():

    banner()

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print(Fore.YELLOW + "Invalid number of arguments provided!")
    else:
        fileChecker()

if __name__ == "__main__":
    main()
