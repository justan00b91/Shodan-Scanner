import shodan 
import sys
import os

key = sys.argv[1]

api = shodan.Shodan(key)

print(" _____________")
print("< SHODAN TIME >")
print(" -------------")
print("        \   ^__^")
print("         \  (oo)\_______")
print("            (__)\       )\/"+"\\")
print("                ||----w |")
print("                ||     ||")


def main():
	print ("1.Get IP")
	print ("2.Scan queries")
	print ("3.Scan Host")
	print ("0 Exit")
	choice = int(input("SHODAN>"))
	if choice == 1:
		getIP()
	elif choice == 2:
		scan()
	elif choice == 3:
		spec_Host()
	else:
		sys.exit() 

def getIP():
	addr = os.system('shodan myip')
	print (addr)
	print ("="*40)
	main()

def spec_Host():
	hostname = input('Enter Host IP Address:')
	detail = api.host(hostname)
	print ("IP:\t%s"%(detail['ip_str']))
	print ("Hostnames:\t")
	for i in detail["hostnames"]:
		print (str(i)+" ")
	print ("City:\t%s"%(detail["city"]))
	print ("Organisation:\t%s"%(detail["org"]))
	print ("Operating System:\t%s"%(detail["os"]))
	print ("Ports:\n")
	for i in detail['data']:
		print ("Port:\t%s"%str(i['port']))
	print ("="*40)
	main()

def scan():
	search = input("Input Query to be searched:")
	result = api.search(search)
	print ("MATCHES-->")
	for i in result['matches']:
		print (i['ip_str']+'\t'+str(i['port'])+'\t'+str(i['org']))
	print ("="*40)
	main()

main()
