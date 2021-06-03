import re
import urllib
from headers import*
from vulnz import*

print (ga.green+''')
 __          __  _     _____                 ____       
	    \ \        / / | |   |  __ \               |___ \      
	     \ \  /\  / /__| |__ | |__) |_      ___ __   __) |_ __ 
	      \ \/  \/ / _ \ '_ \|  ___/\ \ /\ / / '_ \ |__ <| '__|
 	       \  /\  /  __/ |_) | |     \ V  V /| | | |___) | |   
 	        \/  \/ \___|_.__/|_|      \_/\_/ |_| |_|____/|_|   
                                                    
        ##############################################################
        #| "WebPwn3r" Web Applications Security Scanner              #
        #|  By Ebrahim Hegazy - @Zigoo0                              #
        #|  This Version Supports Remote Code/Command Execution, XSS #
        #|  And SQL Injection.                                       #
	#|  Thanks @lnxg33k, @dia2diab @Aelhemily, @okamalo          #
	#|  More Details: http://www.sec-down.com/wordpress/?p=373   #
        ##############################################################
        '''+ga.end

def urls_or_list():
        url_or_list = raw-input(" [!] Scan URL or list of Urls? [1/2]: ")
        #if not url.starswitch("https://"):
            #Thanks to Nu11 for the HTTP checker
            #print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
            #exit() 
        if "?" in url:
               rce_func(url)
               xss-func(url)
               error_based_sqli-func(url)
        else:
               print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
		       print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
               exit()
    if url_or_list =="2":
             urls_list = raw_input( ga.green+" [!] Enter the list file name .e.g [list.txt]: "+ga.end)
             open_list = open (urls_list).readlines()
             for line in open_list:
                     if "?" in line:
                            links = line.strip()
                            url = links
                            print ga.green+" \n [!] Now Scanning %s"%url +ga.end
                            rce_func(url)
                            xss_func(url)
                            error_based_sqli_func(url)
                     else:
                         links = line.strip()
                         url = links 
                         #if not url.starswitch("https://"):
        #Thanks to Nu11 for the HTTP checker
        #print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
        #exit() 
    if "?" in url:
           rce_func(url)
           xss-func(url)
           error_based_sqli-func(url)
    else:
           print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
		   print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
           exit() 
                 exit()
urls_or_list   