import socket
import subprocess

def reset(modemIP,cmd='PHY'):
  sock = socket.create_connection((modemIP, 9200), 2)
  sock.send(b'AT?S\n')
  print("cmd : " + cmd)
  if (cmd == 'PHY' or cmd == 'ATP'):
    if (b'PHY' not in sock.recv(1024)):
      sock.send(b'ATP\n')
      sock.recv(1024)
      print ("# modem " + modemIP + " reset to ATP")
  else:
    if (b'PHY' in sock.recv(1024)):
      sock.send(b'ATA\n')
      sock.recv(1024)
      print ("# modem " + modemIP + " reset to ATA")

def runCMD(cmd,modemID):
	print ("# exec cmd : " + cmd)
	shell = subprocess.Popen(["sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	with open('f.tmp','w') as w:
		w.write(cmd)
	cmdSh = "./sdmsh " + modemID + " -f f.tmp\n"
	shell.stdin.write(cmdSh.encode('ascii'))
	shell.stdin.close()
	for l in shell.stdout:
		print(l)

def runLocalCMD(cmd):
	print ("# exec cmd : " + cmd)
	shell = subprocess.Popen(["sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	shell.stdin.write(cmd.encode('ascii'))
	shell.stdin.close()
	for l in shell.stdout:
		print(l)

import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
