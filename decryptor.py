from time import time

def encrypt(file,key,filetowritename):
	key *= len(file)//len(key)
	key += key[:(len(file)-len(key))]

	filetowrite = open(filetowritename,"wb")

	t0 = time()
	for i in range(len(key)):
		filetowrite.write(bytes([file[i]^key[i]]))
	t1 = time()
	print('encrypting took %f' %(t1-t0))
	
def main():
	keyfilename = input("Enter name of file with key:")
	filetocryptname = input("Enter name of file to crypt:")

	keyfile = open(keyfilename,"rb").read()
	cryptedfile = open(filetocryptname,"rb").read()
	if len(keyfile) > len(cryptedfile):
		print("Error: key is taller than file");raise SystemExit
	filetowritename = input("Enter name of file to write: ")
	print("crypting...")
	encryptedfile = encrypt(cryptedfile, keyfile,filetowritename)

main()