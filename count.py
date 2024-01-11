import os

# x : file location
def countfile(x):
    dir = '{}'.format(x)
    count_file = 0
    for file_name in os.listdir(dir):
        file_path = os.path.join(dir,file_name)
        if os.path.isfile(file_path):
            count_file += 1
    return count_file

# y : directory location
def countdir(y):
    path = y
    dirnum_list = []
    for x in os.listdir(path):
        if os.path.isdir(path+x):
            dirnum_list = os.listdir(y)
    count_dir = len(dirnum_list)
    return count_dir
    

