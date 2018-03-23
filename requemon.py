#!/bin/python

import requests
import argparse
import time

base = {}

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--url', type=str, required=True, help="Target URL")
	parser.add_argument('-r','--requests', type=int, help="# of requests")
	parser.add_argument('-s','--sleep', type=int, help="Seconds between each request")
	return parser.parse_args()

def banner():
	b = '''
		THIS WAS SUPPOSED TO BE A BANNER
	'''
	print b

def baseline(url):
	global base
	print "Baseline response:"
	print "[+] URL: " + url
	req = requests.get(url)
	base['status'] = req.status_code
	base['time'] = req.elapsed.total_seconds()
	base['size'] = len(req.text)

	print "[.] Status code: " + str(base['status'])
	print "[.] Time: " + str(base['time'])
	print "[.] Size:" + str(base['size'])
	print "||||||||||||||||||||||||||||||||||||||||||"
	return

def repeat(url):
	global base
	req = requests.get(url)
	
	if req.status_code != base['status']:
		print "[!] Status changed: " + str(req.status_code)
	else:
		print "[.] Status code: " + str(req.status_code)

	if req.elapsed.total_seconds() > base['time']:
		print "[+] Time increased: " + str(req.elapsed.total_seconds())
	elif req.elapsed.total_seconds() < base['time']:
		print "[-] Time decreased: " + str(req.elapsed.total_seconds())

	if len(req.text) > base['size']:
		print "[+] Size increased: " + str(len(req.text))
	elif len(req.text) < base['size']:
		print "[-] Size decreased: " + str(len(req.text))	
	else:
		print "[.] Size: " + str(len(req.text))
def main():
	banner()
	args = parse_args()
	url = args.url
	baseline(url)
	
	if args.requests is None:
		num = 100
	else:
		num = args.requests

	if args.sleep is None:
		pause = 3
	else:
		pause = args.sleep

	count = 0
	while(count < num):
		time.sleep(pause)
		print "\n[!] Request: " + str(count+1)
		repeat(url)
		count = count + 1
	
main()
