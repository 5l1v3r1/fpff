import time,os,re,random,sys,options,os,requests,io
try:
    from colorama import *
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
except ImportError as e:
    print "Your Error ~> {}".format(e)
    os.time(1.5)
    print "Installing the colorama module please w8\nWhen finished Restart this script . . . "
    l = "sudo apt install python-colorama"
    w = "pip install colorama"
    os.system([l,w][os.name=="nt"])
class FakePage:
    def __init__(self):
        pass

    def run(self):
        files = ["text.txt","file.txt","UserPass.txt","log.txt","user.txt","users.txt","pass.txt","password.txt","user-login.txt",
        "users-login.txt","user-pass.txt","login.txt","logins.txt","test.txt","test1.txt","test2.txt","test3.txt","test4.txt","test5.txt","ist.txt","logs/logs.txt","passwords.txt","log-123.txt","logs-123.txt",
        "user-123.txt","users-123.txt","password-123.txt","passwords-123.txt","123.txt","user/123.txt","test/123.txt","xml.txt","test1/123.txt","test2/123.txt","test3/123.txt","test/xml.txt","test1/xml.txt","test/ist.txt","test/log-123.txt","test1/log-123.txt","test2/log-123.txt","test3/log-123.txt","test4/log-123.txt","test5/log-123.txt","test/logs-123.txt",
        "log.php","user.php","users.php","pass.php","password.php","user-login.php","users-login.php","user-pass.php","login.php","logins.php","test.php","test1.php","test2.php","test3.php","ist.php","logs.php","passwords.php","log-123.php","logs-123.php","user-123.php","users-123.php","password-123.php","passwords-123.php","123.php","user/123.php",
        "test/123.php","xml.php","test1/123.php","test2/123.php","test/xml.php","test1/xml.php","test/ist.php","test1/ist.php","test/log-123.php"]
        try:
            url = sys.argv[1]
        except:
            options.clear()
            options.print_logo()
            print r + "------------------------------------"
            print y + "[" + r + "-" + y + "] " + g + "python fpff.py url\n" + y + "[" + r + "+" + y + "] " + w + "Example ~> " + g + "python fpff.py https://iraniancoders.ir"
            sys.exit()
        options.clear()
        options.print_logo()
        try:
            req = requests.get(url + "/", timeout=3)
        except:
            print y + "[" + r + "-" + y + "] " + g + "Unknown Url"
            sys.exit()
        print y + "[" + r + "!" + y + "] " + g + "Checking Connection  " + b + str(url)
        time.sleep(1)
        if req.status_code == 200:
            print y + "[" + r + "+" + y + "] " + g + "Done Connected !"
            print y + "[" + r + "*" + y + "] " + g + "Started at " + r + "[" + b + time.ctime() + r + "]"
        else:
            print y + "[" + r + "-" + y + "] " + g + "Website is down ...\nOr Check your internet Connection !"
            sys.exit()
        print m + "-----------------------------------------"
        for n in files:
            _url = str(url) + "/" + n
            open = requests.get(_url)
            if open.status_code == 200:
                print y + "[" + r + "+" + y + "] " + g + url + "/" + n + b + " Founded !"
                print res
                user_input = raw_input(r + "Continue ? [y/n] >>> ")
                if user_input == "y":
                    pass
                elif user_input == "n":
                    print b + "Done !"
                    sys.exit()
            elif open.status_code == 404:
                print y + "[" + r + "-" + y + "] " + g + url + "/" + n + b + " 404 Not Found ..."
            elif open.status_code == 403:
                print y + "[" + r + "!" + y + "] " + g + url + "/" + n + b + "Forbidden file ..."
            elif open.status_code == 500:
                print y + "[" + r + "!" + y + "] " + g + url + "/" + n + b + "error 500 external server error"
            else:
                pass




fpff = FakePage()
try:
    fpff.run()
except KeyboardInterrupt as g:
    print b + "\nNice Too meet yoU <3"
    time.sleep(1)
    print "GoodeBye ;)"
