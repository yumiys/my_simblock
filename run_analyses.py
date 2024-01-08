import os
import count
import simple_cmd


# execution calculate_average_blockprop_time.py
simple_cmd.command('python3 calculate_average_blockprop_time.py ./stdouts/*')

# execution calculate_fork_probability.py
simple_cmd.command('python3 calculate_fork_probability.py ./blocklists/*')

# execution calculate_performance.py
simple_cmd.command('python3 calculate_performance.py')

dirnum = count.countdir('./results_graph/')
dir_path = './results_graph'
filenum = count.countfile('./results_graph/file{}'.format(dirnum))
if os.path.isdir(dir_path) == True and filenum == 4+1:
    print('Successfully executed a program called analyse_results.py')
else:
    print('Analysis failed')
