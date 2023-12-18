#
# How to run: $ python3 calculate_fork_probability.py ./blocklists/*
#
import matplotlib.pyplot as plt
import sys
import count
import for_plot
import para

infilenames_list = sys.argv[1:]
fork_probability_list = []

# calling list of para.py
sys.path.append('./home/Soturon/')
blocksize_list = []
for i in para.parameter_list:
    blocksize_list.append(i)
    print(blocksize_list)

# count
for infilename in infilenames_list:
    data_counter = 0
    orphan_counter = 0
    with open(infilename, 'r') as infile:
        for line in infile:
            #print(line)
            if line.split(':')[0] == 'Orphan ':
                orphan_counter += 1
                print(orphan_counter)
            data_counter += 1
            
    orphan_rate = orphan_counter/(data_counter-orphan_counter)
    #print(data_counter, orphan_counter)
    print('orphan rate:', orphan_rate)
    fork_probability_list.append(orphan_rate)
    
    # write standard output to a file named fork_probability.txt
    fork_outfilename = './Fork_probability/fork_probability.txt'
    with open(fork_outfilename, 'a') as stdoutfile:
        print(orphan_rate, file=stdoutfile)
        
print(fork_probability_list)

# plot figure
for_plot.plt_set(blocksize_list, fork_probability_list, 'r', 'fork probability', 'Pfork-plot.png')

