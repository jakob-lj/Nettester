# python
from time import sleep
import requests
import datetime

def test():
	start = datetime.datetime.now()
	req = requests.get("http://localhost:3000/")
	end = datetime.datetime.now()
	diff = end - start
	t = diff.microseconds/1000
	res = req.json()
	return {'suc': res['Hello'] == 'World', 'time':t}


def main():
	successes = []
	fails = []
	while True:
		res = test()
		print("%s: " % datetime.datetime.now(), end="")
		if (res['suc']):
			ap = successes
			print("Success - %s ms" % res['time'])
		else:
			ap = fails
			print("Failed - %s ms" % res['time'])
		ap.append({'time':datetime.datetime.now()})
		sleep(5)

if (__name__ == '__main__'):
	main()
				
