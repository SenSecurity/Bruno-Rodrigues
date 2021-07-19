#!/usr/bin/python
import sys,crypt,re


if len(sys.argv) <=1:
	print "Sintax: python Bruteforce.py <wordlist>"
else:
	
	salt = raw_input("Insert Salt: ")
	crack = raw_input("Insert Hash: ")
	print "\r\n"
	file = open(sys.argv[1])
	for line in file:
		senha = crypt.crypt(line.strip(),salt)
		print "Testing ....",line.strip()
		if (senha == crack):
			print "\r\nPassword Found: ",line.strip()
			break
	
