import os

def get_encrypted_files(path):

    #list of extensions to search
    extensions = [
        'albcrypt' #used for decryption
    ]

    #get absolute path of each file
    file_list = []
    for dirpath, dirs, files in os.walk(path):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                file_list.append(absolute_path)

    return file_list

#check if it works correctly
if __name__ == "__main__":
    get_encrypted_files('/home')
