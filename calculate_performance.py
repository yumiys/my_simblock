#
# How to run: $ python3 calculate_performance.py
#

import math
import for_plot
import para

# calling list of para.py
blocksize_list = []
for i in para.parameter_list:
    blocksize_list.append(i)

interval = para.interval
M_data_list = []
Pfork_data_list = []
result_list = []

# reading numerical values from Average_time file 
infilename1 = './Average_time/average_time.txt'
with open(infilename1, 'r') as infile:
    for line in infile:
        M_data_list.append(float(line.replace('\n', '')))
        
# reading numerical values from Fork_probability file
infilename2 = './Fork_probability/fork_probability.txt'
with open(infilename2, 'r') as infile:
    for line in infile:
        Pfork_data_list.append(float(line.replace('\n', '')))

# performance
for i in range(len(blocksize_list)):
    result = (M_data_list[i]/(interval*Pfork_data_list[i]))*math.exp(((-1)*M_data_list[i])/interval)
    result_list.append(result)
    
print(result_list)

#plot figures
for_plot.plt_set(blocksize_list, result_list, 'g', 'Performance', 'result.png')

