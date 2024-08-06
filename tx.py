from time import sleep
from helper import reset
from helper import runCMD

#Fs = 62500 #7-17 Modems
Fs = 250000 #4-48 Modems
c = {}

############################
####   Variables    ########
############################

modems = ['136']
c['131'] = ['200','1','3'] # threshold 1-4095 , gain , level
c['137'] = ['200','0','0']
c['138'] = ['1','0','0']
c['146'] = ['1','0','0']
c['239'] = ['1','0','3']
c['148'] = ['1','0','3']
c['149'] = ['1','0','3']
c['136'] = ['1','0','3']
c['163'] = ['1','0','0']
############################
#### Run the script ########
############################

# commands :
# stop
# config Threshold, gain, level
# tx [filename]
# tx ShortLFM
# tx LFM
# ref [filename]
# rx [samples] tmp/[filename]


for m in modems:
	try:
		reset('192.168.0.' + m)
	except:
		print("# Cannot connect to modem : " + m )
		continue
	#e.g. 	config 1 0 3
	runCMD('config ' + ' '.join(c[m]) + '\n',m)

	i=-1
	#for ind in range(1):
	while(1<100000):
		i=i+1
		print("transmission #" + str(i+1))
		runCMD('tx TxChirp',m)
		#runCMD('tx Sig',m)
		sleep(1)   # in seconds

