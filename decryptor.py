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
	filetocryptname = input("Enter name of cache file to decrypt:")

	keyfile = open("key","rb").read()
	cryptedfile = open(filetocryptname,"rb").read()
	filetowritename = input("Enter name of file to write: ")
	print("decrypting...")
	encryptedfile = encrypt(cryptedfile, keyfile,filetowritename)

main()