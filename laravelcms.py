import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style


def screen_clear():
    _ = os.system('clear')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def laravelcheck (mk1337):
    if "://" in mk1337:
      mk1337 = mk1337
    else:
      mk1337 = "http://" + mk1337
    mk1337 = mk1337.replace('\n', '').replace('\r', '')
    url = mk1337 + "/.env"
    check = requests.get(url, headers=headers, timeout=3)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"Laravel {gr}OK{res} => {mk1337}\n")
            mrigel = open("Laravel.txt", "a")
            mrigel.write(f'{mk1337}\n')
        else:
            print(f"{red}Not{res} Laravel => {mk1337}\n")
    except:
        pass
def wpcheck (mk1337):
    if "://" in mk1337:
      mk1337 = mk1337
    else:
      mk1337 = "http://" + mk1337
    mk1337 = mk1337.replace('\n', '').replace('\r', '')
    url = mk1337 + "/wp-content/"
    check = requests.get(url, headers=headers, timeout=3)
    try:
        if check.status_code == 200:
            print(f"Wordpress {gr}OK{res} => {mk1337}\n")
            mrigel = open("Wordpress.txt", "a")
            mrigel.write(f'{mk1337}\n')
        else:
            print(f"{red}Not{res} Wordpress => {mk1337}\n")
    except:
        pass


def filter(mk1337):
    try:
       laravelcheck(mk1337)
       wpcheck(mk1337)
    except:
       pass


def main():
    print(f'''    
                 {red} oooo          .o    .oooo.     .oooo.    ooooooooo {res}
                  {yl}`888        o888  .dP""Y88b  .dP""Y88b  d"""""""8' {res}
{gr}ooo. .oo.  .oo.    888  oooo   888        ]8P'       ]8P'       .8'  {res}
{red}`888P"Y88bP"Y88b   888 .8P'    888      <88b.      <88b.       .8'   {res}
 {yl}888   888   888   888888.     888       `88b.      `88b.     .8'    {res}
 {gr}888   888   888   888 `88b.   888  o.   .88P  o.   .88P     .8'     {res}
{wh}o888o o888o o888o o888o o888o o888o `8bd88P'   `8bd88P'     .8'           {res}

                            {red}MataKucing {res}
                {bl}CMS Laravel And Wordpress Check Filter{res}
          {wh}Noniod7 - Cubjrnet7 - AlifAlexis - Valdy - Rizal
    {yl}Lumajang Team Security - Lumajang Hack Team - Cukimay Cyber Team
    
                {red}Blog {wh}: {bl}bloglumajangteamsec.my.id
                {red}Github {wh}: {bl}github.com/MataKucing-OFC
                {red}Youtube {wh}: {bl}youtube.com/c/MataKucing-OFC
    ''')
    list = input(f"{red}List > {gr}:{res} ")
    mk1337 = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(filter, mk1337)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass
       
if __name__ == '__main__':
    screen_clear()
    main()
