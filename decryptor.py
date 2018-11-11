def keygen(l):
	key = b'\x0D\x1E\x2F\x40\x51\x62\x73\x84\x95\xA6\xB7\xC8\xD9\xEA\xFB\x0C'
	for i in range(15):
		for j in range(16):
			key += bytes([(key[(i*16)+j]+16)%256])
	key *= l//len(key)
	key += key[:(l-len(key))]
	return key

def main():
	file = open(input("Enter name of cache file to decrypt:"),"rb").read()
	key = keygen(len(file))
	filetowrite = open(input("Enter name of file to write: "),"wb")
	for i in range(len(key)):
		filetowrite.write(bytes([file[i]^key[i]]))	

if __name__ == '__main__':
	main()