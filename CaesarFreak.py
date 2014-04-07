#!/usr/bin/python
'''
Title: CaesarFreak
Author: Osanda Malith Jayathissa (@OsandaMalith)
Purpose: Just made this for fun after learning about ciphers in our IST Class
License:

	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
import sys

def encode():
	msg = str(raw_input("[+] Enter your msg: "))
	while True:
		key = int(raw_input("[+] Enter your Key: "))		
		if (key > 26):
			print ('[!] Enter a key between 0 and 26')
		else:
			break
	trans = ''
	msg = msg.upper()
	for char in msg:
	    if char in LETTERS:
	        
	        num = LETTERS.find(char)
	        num += key 
	        if num >= len(LETTERS):
	            num -= len(LETTERS)
	        try:    
	        	trans +=LETTERS[num]
	        except IndexError:
				print '[!] Enter a smaller key'
				sys.exit(0)
	    else:
	        trans += char
	print ('[*] Encrypted text: %s'  %(trans))

def decode():
	msg = str(raw_input("[+] Enter your msg: "))
	while True:
		key = int(raw_input("[+] Enter your Key: "))		
		if (key > 26):
			print ('[!] Enter a key between 0 and 26')
		else:
			break		

	trans = ''
	msg = msg.upper()
	for char in msg:
	    if char in LETTERS:
	        
	        num = LETTERS.find(char)
	        num -= key 
	        if num < 0:
	            num += len(LETTERS)
	        try:    
	        	trans +=LETTERS[num]
	        except IndexError:
				print '[!] Enter a smaller key'
				sys.exit(0)
	    
	print ('[*] Encrypted text: %s'  %(trans))


def crack():
	msg = str(raw_input("[+] Enter your msg: "))		
	msg = msg.upper()
	for key in range(len(LETTERS)):
	    translated = ''
	    for symbol in msg:
	        if symbol in LETTERS:
	            num = LETTERS.find(symbol) 
	            num = num - key
	            if num < 0:
	                num = num + len(LETTERS)
	            translated = translated + LETTERS[num]
	        else:
	            translated = translated + symbol
	    print('[*] Key ~%d: %s' % (key, translated))

def main():
	try:
		print('''

  .g8"""bgd                                          
.dP'     `M                                          
dM'       ` ,6"Yb.  .gP"Ya  ,pP"Ybd  ,6"Yb.  `7Mb,od8
MM         8)   MM ,M'   Yb 8I   `" 8)   MM    MM' "'
MM.         ,pm9MM 8M"""""" `YMMMa.  ,pm9MM    MM    
`Mb.     ,'8M   MM YM.    , L.   I8 8M   MM    MM    
  `"bmmmd' `Moo9^Yo.`Mbmmd' M9mmmP' `Moo9^Yo..JMML.  

		`7MM"""YMM                         `7MM      
		  MM    `7                           MM      
		  MM   d `7Mb,od8 .gP"Ya   ,6"Yb.    MM  ,MP'
		  MM""MM   MM' "',M'   Yb 8)   MM    MM ;Y   
		  MM   Y   MM    8M""""""  ,pm9MM    MM;Mm   
		  MM       MM    YM.    , 8M   MM    MM `Mb. 
		.JMML.   .JMML.   `Mbmmd' `Moo9^Yo..JMML. YA.    

[~] Title: CaesarFreak
[~] Author: Osanda Malith Jayathissa (@OsandaMalith)
[~] Description: A small tool to make and break the Caesar cipher                                                 
			''')
		
		while True:
			try:
				choice = int(raw_input("[?] Choose an Option \
					\n1. Encode\n2. Decode\n3. Crack\n4. Exit\n" ))
			except ValueError:
				print '[!] Enter Only a Number'
				continue
		
			if choice == 1:
				encode()
				break
			if choice == 2:
				decode()
				break
			if choice == 3:
				crack()
				break
			if choice == 4:
				sys.exit(0)
			else:
				print '[!] Invalid Choice'

	except (KeyboardInterrupt):
		print '[!] Ctrl + C detected\n[!] Exiting'
		sys.exit(0)
	except (EOFError):
		print '[!] Ctrl + D detected\n[!] Exiting'
		sys.exit(0)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == "__main__": 
	main()	
