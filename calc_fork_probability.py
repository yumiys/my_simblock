#
# How to run: $ python3 calc_fork_probability.py ./Blocklists/*
#

import matplotlib.pyplot as plt
import sys
import count
import for_plot
import para

# define variables and lists
blocksize_list = []
fork_probability_list = []
prop_rate = para.propagation_rate

# read blocksize from para.py
for i in para.parameter_list:
    blocksize_list.append(i)
    
# caculate fork probability
sys.path.append('./home/Soturon/')
infilenames_list = sys.argv[1:]
for infilename in infilenames_list:
    data_counter = 0
    orphan_counter = 0
    with open(infilename, 'r') as infile:
        for line in infile:
            if data_counter > (10000*prop_rate):
                break  
            elif line.split(':')[0] == 'Orphan ':
                print(line)
                orphan_counter += 1
            data_counter += 1

    orphan_rate = orphan_counter / data_counter
    print('orphan_counter=',orphan_counter)
    print('data_counter=',data_counter)
    print('orphan rate:', orphan_rate)
    fork_probability_list.append(orphan_rate)
    
    # write standard output to a file named fork_probability.txt
    fork_outfilename = './Fork_probability/fork_probability.txt'
    with open(fork_outfilename, 'a') as stdoutfile:
        print(orphan_rate, file=stdoutfile)
      
print('fork_probability_list:')        
print(fork_probability_list)

# plot figure
for_plot.plt_set(blocksize_list, fork_probability_list, 'r', 'fork probability', 'Pfork-plot.png')

