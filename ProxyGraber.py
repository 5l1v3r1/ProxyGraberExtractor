#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import time, datetime
import sys
try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
except:
	print('pip3 install selenium or pip install selenium')
try:	
	from bs4 import BeautifulSoup
except:	
	print('pip install bs4 or pip3 install bs4')

######################

os.system('clear')

######################

ts = time.time()
dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

#############
# Date #####
#########################################
today = datetime.datetime.today()     ##
t = today.strftime("[%H:%M:%S] - ")  ##
######################################
# Colors

W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'

########################
#   Slow Print        ##
########################
########################################################################

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
        #time.sleep(10./90)

def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./50)
#######################################################################
#############################################################
print(P+' /$$$$$$$')                                
print(P+'| $$__  $$')                                   
print(P+'| $$  \ $$/$$$$$$  /$$$$$$ /$$   /$$/$$   /$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(P+'| $$$$$$$/$$__  $$/$$__  $|  $$ /$$| $$  | $$    $$        Laboratorio Fantasma        $$')
print(P+'| $$____| $$  \__| $$  \ $$\  $$$$/| $$  | $$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')   
print(P+'| $$    | $$     | $$  | $$ >$$  $$| $$  | $$    $$         Coded By > Luth1er         $$')
print(P+'| $$    | $$     |  $$$$$$//$$/\  $|  $$$$$$$    $$          Date: 30/04/2017          $$')
print(P+'|__/    |__/      \______/|__/  \__/\____  $$    $$ I take no responsibilities for the $$')
print(P+'                                    /$$  | $$    $$      use of this program !         $$')
print(P+'                                   |  $$$$$$/    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(P+'                                    \______/ ')
fastprint(B+'                                                        Telegram:'+O+' @DreadPirateRobertt')
fastprint(verde+'                                                            Laboratorio Fantasma')

Scrapper = """ $$$$$$\                                                                
$$  __$$\                                                               
$$ /  \__|$$$$$$$\ $$$$$$\ $$$$$$\  $$$$$$\  $$$$$$\  $$$$$$\  $$$$$$\  
\$$$$$$\ $$  _____$$  __$$\\____$$\$$  __$$\$$  __$$\$$  __$$\$$  __$$\ 
 \____$$\$$ /     $$ |  \__$$$$$$$ $$ /  $$ $$ /  $$ $$$$$$$$ $$ |  \__|
$$\   $$ $$ |     $$ |    $$  __$$ $$ |  $$ $$ |  $$ $$   ____$$ |      
\$$$$$$  \$$$$$$$\$$ |    \$$$$$$$ $$$$$$$  $$$$$$$  \$$$$$$$\$$ |      
 \______/ \_______\__|     \_______$$  ____/$$  ____/ \_______\__|      
                                   $$ |     $$ |                        
                                   $$ |     $$ |                        
                                   \__|     \__|"""


print(verde+Scrapper)
fastprint(B+'Use ProxyCrawl3d.py -h or --help\n')
input(C+'[*] Press Any Key To Continue...')

#############################################################
PhantomJS_Others_OS = """
#############################################################

############
## Ubuntu ##
############
$ sudo apt-get install phantomjs
$ sudo cp /path/to/phantomjs/bin/phantomjs /usr/local/bin/

#################
## Arch Linux ##
###############
$ su pacman -S phantomjs
$ sudo cp /path/to/phantomjs/bin/phantomjs /usr/local/bin/

###############################################################
"""

PhantomJS_Website_Step = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$ How to install PhantomJS $$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
download from phantomjs website the prebuilt package : http://phantomjs.org/download.html 
then open a terminal and go to the Downloads folder;"""
PhantomJS_Packages_Manage = """
[phantasmlab@localhost Desktop]$ sudo mv phantomjs-1.8.1-linux-x86_64.tar.bz2 /usr/local/share/.
[phantasmlab@localhost Desktop]$ cd /usr/local/share/
[phantasmlab@localhost Desktop]$ sudo tar xjf phantomjs-1.8.1-linux-x86_64.tar.bz2
[phantasmlab@localhost Desktop]$ sudo ln -s /usr/local/share/phantomjs-1.8.1-linux-x86_64 /usr/local/share/phantomjs
[phantasmlab@localhost Desktop]$ sudo ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs
#########################################################################################################################
"""


def help():
	print('')
	print(verde+'[*] Instalation Manual\n')
	print(verde+'Python --version: Python 3.6.1\n')
	print(verde+'pip --version: pip 9.0.1 from /usr/lib/python3.6/site-packages (python 3.6)')
	print (P+PhantomJS_Website_Step)
	print (P+PhantomJS_Packages_Manage)
	print('')
	print(B+PhantomJS_Others_OS)
	print(' ')
	sys.exit(1)
try:
	if len(sys.argv) <= 3 and len(sys.argv) >= 2:
		opt = sys.argv[1]
		if opt == '-h' or opt == '--help':
			help()
except Exception as error:
	print(R+'[!] Error : %s' % error)

def Scraping():
	def fastprint(s):
		for c in s + '\n':
			sys.stdout.write(c)
			sys.stdout.flush() # defeat buffering
			time.sleep(1./80)
	global t
	global count
	count = 0
	try:
		driver = webdriver.PhantomJS()
	except:
		print('')
		print(O+PhantomJS_Website_Step)
		print('')
		print(B+PhantomJS_Packages_Manage)
		print('')
		print(P+PhantomJS_Others_OS)
#################
#URL'S_Graber ###
###############################################################################################################
	Brazilian_URL = ['http://www.freeproxylists.net/?c=BR&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0','http://www.freeproxylists.net/?c=BR&page=2']
	Argentina_URL = ['http://www.freeproxylists.net/?c=AR&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	United_States = ['http://www.freeproxylists.net/?c=US&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0','http://www.freeproxylists.net/?c=US&page=2','http://www.freeproxylists.net/?c=US&page=3']
	Mexico = ['http://www.freeproxylists.net/?c=MX&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Italy = ['http://www.freeproxylists.net/?c=IT&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Australia = ['http://www.freeproxylists.net/?c=AU&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Canada = ['http://www.freeproxylists.net/?c=CA&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	China = ['http://www.freeproxylists.net/?c=CN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0','http://www.freeproxylists.net/?c=CN&page=2']
	Russia =['http://www.freeproxylists.net/?c=RU&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0','http://www.freeproxylists.net/?c=RU&page=2','http://www.freeproxylists.net/?c=RU&page=3']
	Portugal = ['http://www.freeproxylists.net/?c=PT&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Spain = ['http://www.freeproxylists.net/?c=ES&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Japan = ['http://www.freeproxylists.net/?c=JP&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	Taiwan = ['http://www.freeproxylists.net/?c=TW&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	India = ['http://www.freeproxylists.net/?c=IN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']
	urls = [Brazilian_URL, United_States, China, Russia, Japan, Portugal, Spain, Mexico, Italy, Australia, Canada, Taiwan, India ]
####################################################################################################################

	for i in range(len(urls)):
		if i == 0:
			print('')
			print(R+t+amarelo+'[*] Brazilian Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Br] - URL Found Scraping: '+G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] Brazilian Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)						
###############################################################################################################
		elif i == 1:
			print('')
			print(R+t+amarelo+'[*] United States Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[US] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
					if 'IPDecode' in str(td[0]):
						print(R+t+P+'[*] United States Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
						time.sleep(0.1)
						fil = open("proxylist-" + dt + ".txt",'a')
						fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
						fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)												
#############################################################################################################
		elif i == 2:
			print('')
			print(R+t+amarelo+'[*] China Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[CHINA] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] China Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()	
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)
###########################################################################################################
		elif i == 3:
			print('')
			print(R+t+amarelo+'[*] Russia Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Russia] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+P+'[*] Russia Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
################################################################################################################
		elif i == 4:
			print('')
			print(R+t+amarelo+'[*] Japan Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Japan] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] Japan Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
###########################################################################################################
		elif i == 5:
			print('')
			print(R+t+amarelo+'[*] Portugal Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Portugal] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+P+'[*] Portugal Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
##############################################################################################################
		elif i == 6:
			print('')
			print(R+t+amarelo+'[*] Spain Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Spain] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] Spain Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
################################################################################################
		elif i == 7:
			print('')
			print(R+t+amarelo+'[*] Mexico Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Mexico] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+P+'[*] Mexico Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
################################################################################################
		elif i == 8:
			print('')
			print(R+t+amarelo+'[*] Italy Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Italy] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] Italy Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
################################################################################################
		elif i == 9:
			print('')
			print(R+t+amarelo+'[*] Australia Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Australia] - URL Found Scraping: ' +G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+P+'[*] Australia Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)							
################################################################################################
		elif i == 10:
			print('')
			print(R+t+amarelo+'[*] Canada Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Canada] - URL Found Scraping: '+G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] Canada Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)
######################################################################################################
		elif i == 11:
			print('')
			print(R+t+amarelo+'[*] Taiwan Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[Taiwan] - URL Found Scraping: '+G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+P+'[*] Taiwan Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)
#################################################################################################
		elif i == 12:
			print('')
			print(R+t+amarelo+'[*] India Proxys....\n')
			for url in urls[i]:
				try:
					driver.get(url)
					data = driver.page_source
					soup = BeautifulSoup(data, 'html.parser')
					query = soup.find_all('tbody')
					tulis = query[1]
					soup = BeautifulSoup(str(tulis), 'html.parser')
					query = soup.find_all('tr')
					print('')
					print(R+t+B+'[India] - URL Found Scraping: '+G+ url,'\n')
					for td in query:
						count = count+1
						td = td.find_all('td')
						if 'IPDecode' in str(td[0]):
							print(R+t+O+'[*] India Proxy Scraping:'+G+str(td[0].text.split(')')[1]+':'+td[1].text))
							time.sleep(0.1)
							fil = open("proxylist-" + dt + ".txt",'a')
							fil.write(str(td[0].text.split(')')[1]+':'+td[1].text+'\n'))
							fil.close()
				except Exception as erro:
					print(R+t+O+'[!] Erro: %s' % erro)
					print(R+t+O+'\n\t [*] Saindo...')
					sys.exit(1)					

################################################################################################
	fastprint ("\n\tProxy-List-" + dt + ".txt")
	print('')
	print (R+t+P+'Proxyes Found > '+O+str(count),'\n')
	print('')
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	driver.close()
	print('')
	input(R+t+B+"[*] Press Any Key To Exit...")
	fastprint('\n [*] Exiting.......')
	print('')
	sys.exit()	
#################################################################################################
try:
	Scraping()
except KeyboardInterrupt:
	print('')
	fastprint(R+t+amarelo+"[*] Saindo....")
