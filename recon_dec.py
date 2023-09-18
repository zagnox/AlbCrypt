import os

def get_paths(path):

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


def get_files(startpath):
    x = get_paths(startpath)
    for i in x:
        return str(i)

#check if it works correctly
if __name__ == "__main__":
    x = get_files('/home')
