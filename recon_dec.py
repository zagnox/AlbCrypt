import os

def get_files(path):

    #list of extensions to search
    extensions = [
        'albcrypt' #used for decryption
    ]

    #yield absolute path of each file
    for dirpath, dirs, files in os.walk(path):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

#check if it works correctly
if __name__ == "__main__":
    x = get_files('/home')
    for i in x:
        print(i)
