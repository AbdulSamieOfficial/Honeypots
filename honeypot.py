#!/usr/bin/env python3

#Group Members
# *Abdul Samie (19I - 0663)
# *Fatimah Noor (19I - 1967)
# *CS - C
# *Honeypot Project Information Security

#Importing libraries here
import sys
from socket import *
import socket
import logging
import os
import time
import atexit
from termcolor import colored, cprint
import threading
from threading import Thread
from _thread import *

user_dict = 0
server_lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def exit_handler():
    print ('\n[*] Honeypot is shutting down!')
    server_lstnr.close()

def writeLog(clt, data='',user='',pas=''):
	print(user,pas)
	separator = '='*50
	fopen = open('./log.txt', 'a')
#	fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), clt[0], clt[1], data, separator))
	fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n'%(time.ctime(), clt[0], clt[1], data))
	fopen.write('Username is:%s\nPassword is:%s\n\n%s\n'%(user,pas,separator))
#	fopen.write('\nUsername is:%s\nPassword is:%s'%(user,pas),separator)

def storeCommands(user_cmd,ip):
	fopen = open('./log.txt', 'a')
	fopen.write('%s->%s'%(user_cmd,ip))
	fopen.write('\n')

	#fopen.write(''%(),separator)
	fopen.close()


def sendCommands(fromip, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    s.send('IP:' , fromip , ' Port:' , str(port) , ' | ' , message.replace('\r\n', ' '))
    s.close()

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def cat_command(file,inp_cmd,c):
	if('Password.txt' in str(file) and inp_cmd==7):
		data = '966b28d4f5b0a4e5f996dfededdb13d1c98019e7f16c7032c2a96c161c200922\n fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6\n582967534d0f909d196b97f9e6921342777aea87b46fa52df165389db1fb8ccf\n123fd666aa39d376690cfa6570426d3585c188b291bc87acf47b84e3fe822102'
		c.sendall(bytes(data,'utf-8'))


def commandLS(inp_cmd):
	if(inp_cmd==0):
		return 'Desktop\t\tDocuments\t\tDownloads\t\tPictures\t\tPublic\t\tVideos\t\tDatabase'
	elif(inp_cmd==1):
		return 'confidential.rar'
	elif(inp_cmd==2):
		return 'clientinfo.txt'
	elif(inp_cmd==3):
		return 'walpaper.jpeg'
	elif(inp_cmd==4):
		return 'tree.jpeg\tsnip.jpeg'
	elif(inp_cmd==5):
		return ''
	elif(inp_cmd==6):
		return 'transaction.mp4\tvisit.mp4'
	elif(inp_cmd==7):
		return 'Password.txt\tAccount_Database'

def sendCmds(inp_cmd,c):
	if(inp_cmd==0):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami]└─#')
	elif(inp_cmd==1):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Desktop]└─#')
	elif(inp_cmd==2):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Documents]└─#')
	elif(inp_cmd==3):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Downloads]└─#')
	elif(inp_cmd==4):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Pictures]└─#')
	elif(inp_cmd==5):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Public]└─#')
	elif(inp_cmd==6):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Videos]└─#')
	elif(inp_cmd==7):
		cmd_prompt=colored(255, 0, 0, '\n┌──(root💀sami)-[/home/sami/Databse]└─#')
	c.sendall(bytes(cmd_prompt,'utf-8'))
	
def RansomAct(c):
	print("\nRansomware\n")
#	cmd_prompt=colored(141,182,205,'\n\n\n\n\nAlert! Ransomware has Encrypted Your data\n')
	data=cprint('\nHacker', 'blue', attrs=['blink'])
	#cprint()
	#cmd_prompt='\nJames Everleigh', 'blue', attrs=['blink']
#	c.sendall(bytes(cmd_prompt,'utf-8'))
	danger=colored(255,0,0,'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDanger💀\n')
	c.sendall(bytes(danger,'utf-8'))
	cmd_prompt=colored(141,182,205,'Your all activities including IP and Location has been traced. Severe actions would be taken against you and our Organization will not forgive you')
	c.sendall(bytes(cmd_prompt,'utf-8'))
	cmd_prompt=colored(255,0,0,'*** FIA CHIEF ***\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	c.sendall(bytes(cmd_prompt,'utf-8'))
	while True:
		new=1

def cmdTerm(user_cmd,c,user_dict):
	#global user_dict

	if('ls' in str(user_cmd)):

		lsdir=commandLS(user_dict)
		lsdir=colored(141,182,205,lsdir)#lsdir
		c.sendall(bytes(lsdir,'utf-8'))
		sendCmds(0,c)
	elif('cd Desktop' in str(user_cmd)):
		user_dict=1
		sendCmds(1,c)


	elif('cd Documents' in str(user_cmd)):
		user_dict=2
		sendCmds(2,c)

	elif('cd Downloads' in str(user_cmd)):
		user_dict=3
		sendCmds(3,c)

	elif('cd Pictures' in str(user_cmd)):
		user_dict=4
		sendCmds(4,c)

	elif('cd Public' in str(user_cmd)):
		user_dict=5
		sendCmds(5,c)

	elif('cd Videos' in str(user_cmd)):
		user_dict=6
		sendCmds(6,c)

	elif('cd Database' in str(user_cmd)):#redirect to Database user_dict
		user_dict=7
		sendCmds(7,c)#7 shows it's database user_dict
	elif('cat Password.txt' in str(user_cmd)):#redirect to Database user_dict
		user_dict=7
		cat_command('Password.txt',user_dict,c)
		sendCmds(7,c)#7 shows it's database user_dict
	elif('cd Account_Database' in str(user_cmd) and user_dict==7):#redirect to Database user_dict
		user_dict=-1
		RansomAct(c)

	elif('cd ..' in str(user_cmd) or 'cd ~' in str(user_cmd)):#redirect to Database user_dict
		user_dict=0
		sendCmds(0,c)#7 shows it's database user_dict
	elif('whoami' in str(user_cmd) or 'cd ~' in str(user_cmd)):#redirect to Database user_dict
		data=colored(255, 0, 0,'root')
		c.sendall(bytes(data,'utf-8'))		
		sendCmds(user_dict,c)#7 shows it's database user_dict
	elif('install' in str(user_cmd)):
		c.sendall(bytes('E: Could not get lock /var/lib/dpkg/lock - open(11:Resource temporarily unavailable)\n','utf-8'))		
		sendCmds(user_dict,c)

	else:
		c.sendall(bytes('Command not found','utf-8'))
		sendCmds(user_dict,c)

	return user_dict

def charRemove(clt_name):
	clt_list = list(str(clt_name))
	clt_list[0]=''
	clt_list[1]=''
	clt_list[-1]=''
	clt_list[-2]=''
	clt_list[-3]=''
	clt_list[-4]=''
	clt_list[-5]=''

	''.join(clt_list)
	user=""
	for x in clt_list:
		user+=x

	return user

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.0.1'#172.16.38.209    ********Input Your IP address in this field********192.168.43.242
port=23
default_user='sami'
default_pas='Password'

display='Kali login:'
display1='Password:'
RHOST = '192.168.246.152'
RPORT = 9000

atexit.register(exit_handler)
server_lstnr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_lstnr.bind((host, port))

server_lstnr.listen(10)

def threaded_client(c):
	c.sendall(bytes('Kali GNU/Linux Rolling\n','utf-8'))
	c.sendall(bytes('(','utf-8'))
	c.sendall(bytes(host,'utf-8'))
	c.sendall(bytes(') :anonymous\n','utf-8'))

	user_dict=0
	cnt_check=1
	while True:
		c.sendall(bytes(display,'utf-8'))
		#data =
		if(cnt_check==1): 
			c.recv(1024)#unuseful data
			cnt_check=2
		#print()#Username
		clt_name=c.recv(1024)
		c.sendall(bytes(display1,'utf-8'))

		#data = c.recv(1024)
		#print()#clt_pass
		clt_pass=c.recv(1024)
		clt_name=charRemove(clt_name)
		clt_pass=charRemove(clt_pass)

		writeLog(addr,addr,clt_name,clt_pass)



		print(clt_name)
		print(clt_pass)


#		print(str(clt_list))
		#print(clt_list)
#		disallowed_characters = '/r/b/n'
		#for x in range(2,len(clt_name)-2):
			
			#clt_name[x] = clt_name.replace(x, "")
		#s=""
		#for x in range(0,len(clt_name)-2):
		#	print('%c'% clt_name[x])
		#	s[x]=str(clt_name[x])

		#	print('s:',s)

		#for x in range(len(clt_name)-1,len(clt_name)):
		#	clt_name[x]=' '

		#print(str(clt_name))
		#print('%c'%clt_name[0])
		if('admin' in str(clt_name) and 'admin' in str(clt_pass)):#********You can Change Username and Password from here********
			c.sendall(bytes('You are getting in the system.\n','utf-8'))
			sendCmds(0,c)
			#RansomAct()
			#receiving commands from attacker
			user_dict=0
			#RansomAct(c)
			while True:
				user_cmd=c.recv(1024)
				user_cmd=charRemove(user_cmd)
				storeCommands(user_cmd,addr)
				user_dict=cmdTerm(user_cmd,c,user_dict)#second argument for socket


			break
		else:
			c.sendall(bytes('Authentication Failed\n','utf-8'))
	c.close()
	



while True:
#for x in range(1):
	getClt,addr=server_lstnr.accept()
	print("Connection Established with IP Address: ",addr)
	start_new_thread(threaded_client, (getClt, ))

#	start_new_thread(threaded_client, (getClt, ))
#	logdata=c.recv(1024).decode('ascii')#reading data from attacker
	#sendCommands(addr[0],addr)

print("Weldone")
server_lstnr.close()



