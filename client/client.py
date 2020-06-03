# python
from time import sleep
import requests
import datetime
import os
now = str(datetime.datetime.now()).split(" ")[1]
today = str(datetime.date.today())
try:
	os.system("mkdir logs")
	os.system("mkdir logs/%s" % today)
	os.system("mkdir logs/%s/%s/" % (today, now))
except:
	pass
logfile = 'logs/%s/%s/log.dat' % (today, now)
resultFile = 'logs/%s/%s/result.dat' % (today, now)

with open(logfile, "w") as f:
	f.write("Started server at %s\n" % datetime.datetime.now())

def test():
	start = datetime.datetime.now()
	req = requests.get("http://nettester.jakoblj.xyz")
	end = datetime.datetime.now()
	diff = end - start
	t = diff.microseconds/1000
	res = req.json()
	return {'suc': res['Hello'] == 'World', 'time':t}
	#return {'suc': False, 'time': 10.5}

def log(msg):
	print(msg)
	with open(logfile, 'a') as f:
		f.write(msg + "\n")		

def finallog():
	testEnd = datetime.datetime.now()
	if (lastLog == False):
		e = datetime.datetime.now()
		unavailPeriod.append({'start':s, 'end':e, 'duration':e-s})
	total = 0
	elapsed = (testEnd - testStart).seconds
	if (elapsed < 1):
			elapsed = 1
	with open(resultFile, 'w') as r:
		for e in unavailPeriod:
			total += e['duration'].seconds
			r.write("Start: %s" % e['start'])
			r.write('End: %s' % e['end'])
			r.write('Duration: %s seconds' % e['duration'].seconds)
			r.write('\n\n')
		r.write("Total scores: ------")
		r.write("	Total time unavailable: %s \n" % total)
		r.write("	Elapsed time: %s \n" % elapsed)
		r.write("	Procentage: %s  \n" % ((total/elapsed)*100))
		r.write("	Total failes: %s \n" % len(unavailPeriod))
	print("Test finished")
	print("You can find a final report at: %s" % resultFile)
	
def main():
	successes = []
	fails = []
	
	global lastLog
	
	inarow = 0
	global s
	e = datetime.datetime.now()
	while True:
		res = test()
		# print("%s: " % datetime.datetime.now(), end="")
		if (res['suc']):
			if (inarow > 1 and lastLog == False):
				e = datetime.datetime.now()
				unavailPeriod.append({'start':s, 'end':e, 'duration':e-s})
			inarow = 0
			lastLog = True
			ap = successes
			msg = "Success - %s ms" % res['time']
		else:
			if lastLog:
				s = datetime.datetime.now()
			inarow += 1
			lastLog = False
			ap = fails
			msg = "Failed - %s ms" % res['time']
		ap.append({'time':datetime.datetime.now()})
		log(msg)
		sleep(5)

if (__name__ == '__main__'):
	unavailPeriod = []
	lastLog = True
	s = datetime.datetime.now()
	testStart = datetime.datetime.now()
	try:
		main()
	except KeyboardInterrupt as e:
		print("Finishing up")
		finallog()		
	
