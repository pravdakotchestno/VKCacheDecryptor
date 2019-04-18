import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Decrypts VK android app cached mp3 music files.')
	parser.add_argument('-i', '--infile', type=str, nargs='+', required=True)
	parser.add_argument('-o', '--outfile', type=str, nargs='+')
	args = parser.parse_args()

	if args.outfile != None and len(args.outfile) != len(args.infile):
		print('Error: number of outfiles should be equal to number of infiles')

	if args.outfile == None:
		args.outfile = map(lambda x: x + '.mp3', args.infile)

	for inf, outf in zip(args.infile, args.outfile):
		try:
			infile = open(inf, "rb")
		except FileNotFoundError:
			resp = input('Error: file {} not found, continue?(y/n)'.format(inf)).lower()
			if resp == 'y': continue
			exit()
		outfile = open(outf, "wb")

		filebyte = infile.read(1)
		keybyte = 0x0D
		while filebyte != b'':
			outfile.write(bytes([filebyte[0] ^ keybyte]))
			keybyte = (keybyte + 0x11) % 256
			filebyte = infile.read(1)
		
		infile.close()
		outfile.close()
		print('Successfully decrypted:', outf)