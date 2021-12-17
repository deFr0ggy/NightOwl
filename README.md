<h4 align="center">Python script to butcher Email Headers</h4>

Every organization receives SPAM, Phishing and Spear Phishing Emails. Whenever such emails are received the first and the foremost actions required is to get the Email Headers which are then shared either with the MSSP currently looking after your security or with the internal Security Analyst. The reason is to find all the required information i.e. to perform Email Forensics in order to find answers like. 

- Who sent the email?
- From where it originated?
- How many people have received the email?
- Does the email contained a phishing link or it contained only plain text?
- Does the email contains any attachments?

These are few of the questions which always come to our mind when any such email is received. Keeping these details in mind I have developed **Email Butcher** to automate the manual procedure to find all possible answers to our questions. 

---

**Email Butcher** is a quick and dirty python script to perform analysis on Email Headers. The script renders all the required information for you to take quick actions rather than going through the headers line by line. **The script does it for you** automatically.

I have developed this script during my day job and I do plan to take it one step further with time. The requirements for the program are as below.

```
1. Python3
2. Colorama
```
## Usage
```
   
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
    Coded by Kamran Saifullah - Frog Man
    -----------------------------------------
    Usage: ./NightOwl.py <Mices>
    -----------------------------------------
    LinkedIn: https://www.linkedin.com/in/kamransaifullah/
    GitHub: https://github.com/deFr0ggy
    Twitter: https://twitter.com/deFr0ggy
    
```
## Installing Dependencies

- pip install -r requirements.txt
- python -m pip install -r requirements.txt

## Butchering Basic Email Headers

These headers include the following.
- TO
- FROM 
- SUBJECT
- DATE

## Hops Count

The script counts for the total number of hops (MTAs/MDAs). Thusm we can calculate the total number of MTAs/MDAs involved since the email generation to its landing in our inbox.

## Butchering IP Addresses

The script then looks for all the IP addresses from the Email Headers and lists them down for analysis. These are the IP addresses which are of MTAs/MDAs, Receivers and any other IP addresses embedded within the email or elsewhere. It hunts for all.

## Butchering Email Addresses

The script looks for all the available email addresses from within the Email Headers and lists them down. This is to check which mail servers, senders, receivers are involved. 

## Butchering URLs

The script also looks for all the available URLs from the email headers and provides us with the information to take quick actions i.e. to get these URLs blocked on Email Gateways, Firewalls etc to prevent infections proactively.

## Butchering HTML Embedded Contents

The script hunts down all the HTML contents if it is present in the Email Headers. It alerts that there is an HTML content present in the email and asks for the output file where it can write that data to for later analysis.

## Listing Down All X-* Headers

These headers provide a wide range of information. Also, these headers gets added to the Email as soon as the email starts to propogate. These can provides us with the information whether the email is a SPAM, Malicious, routed through MS-Exchange etc. Close attention is required for these headers.

---

# To Do 

In ***Phase 2***, I need to add the following functionalities along with revamping the overall code from **Quick & Dirty** to **Quick & More Organized**.

- [ ] Integrate Virustotal
- [ ] Integrate Talos 
- [X] Integrate AbuseIPDB
- [ ] Integrate URLVoid
- [ ] Integrate Phishtank
- [ ] Perform IP lookups
- [ ] Gather Domains/IPs country information.
- [ ] Gather Domains Hosting Information
- [X] Add Support For UTF-8 Encoding Scheme
