#
# How to run: $ python3 Run_analyses.py
#

import os
import count
import simple_cmd

# execute calc_average_blockprop_time.py
simple_cmd.command('python3 calc_avg_blockprop_time.py ./Stdouts/*')

# execute calc_fork_probability.py
simple_cmd.command('python3 calc_fork_probability.py ./Blocklists/*')

# execute calc_performance.py
simple_cmd.command('python3 calc_performance.py')

# check the number of files generated
dir_path = './Results_graph/'
dirnum = count.countdir(dir_path)
filenum = count.countfile('./Results_graph/file{}'.format(dirnum))
if os.path.isdir(dir_path) == True and filenum == 4+1:
    print('Successfully executed a program called analyse_results.py')
else:
    print('Analysis failed')
    

    
