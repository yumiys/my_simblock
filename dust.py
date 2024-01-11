import subprocess
import count

# x is the directory location
def del_results(x):
    cmd = 'rm {}/*.txt'.format(x)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    file_num = count.countfile(x)
    if file_num == 0:
        print('Success. There are no files left in [{}] directory'.format(x))
    else:
        print('Failed to delete files in [{}] directory'.format(x))


# average_time.txt 
del_results('./Average_time')
# fork_probability.txt
del_results('./Fork_probability')
# ./Stdouts files
del_results('./Stdouts')
# ./Blocklists files
del_results('./Blocklists')
