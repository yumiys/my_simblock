#
# How to run: $ python3 calculate_average_block_propagation_time.py ./stdouts/*
#

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import count
import for_plot
import para


# Reference
# https://atmarkit.itmedia.co.jp/ait/articles/2102/09/news026.html
# 文字列が数値を表し、int関数による変換が可能かどうかを判定
def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True


#calling list of para.py
sys.path.append('./home/Soturon/')
blocksize_list = []
for i in para.parameter_list:
    #print(i)
    blocksize_list.append(i)
#print(blocksize_list)


average_propagation_time_list = []
std_propagation_time_list = []
nodenum = para.node_num
rate = para.propagation_rate

infilenames_list = sys.argv[1:]
for infilename in infilenames_list:
    previous_block_propagation_time_list = []
    previous_flag = False
    line_counter = 0
    with open(infilename, 'r') as infile:
        for line in infile:
            data_list = line.replace('\n', '').split(',')
            if len(data_list) == 2 and isint(data_list[0]) and line_counter <= (math.floor(nodenum*rate)):
                #print(int(data_list[0]), int(data_list[1]))
                previous_block_propagation_time = int(data_list[1])
                previous_flag = True
                line_counter += 1 
            elif line_counter >= (math.floor(nodenum*rate)) and previous_flag == True:
                previous_block_propagation_time_list.append(previous_block_propagation_time)
                previous_flag = False
            elif data_list[0] == '':
                line_counter = 0
            else:
                continue

    #print(previous_block_propagation_time_list)
    print('len=',len(previous_block_propagation_time_list))
    print('average:', np.average(previous_block_propagation_time_list))
    #print('standard deviation:', np.std(previous_block_propagation_time_list))
    average_propagation_time_list.append(np.average(previous_block_propagation_time_list))
    std_propagation_time_list.append(np.std(previous_block_propagation_time_list))

    # write standard output to a file named average_time.txt
    av_outfilename = './Average_time/average_time.txt'
    with open(av_outfilename, 'a') as stdoutfile:
        print(str(np.average(previous_block_propagation_time_list)), file=stdoutfile)
        

# plot figures
for_plot.plt_set(blocksize_list, average_propagation_time_list, 'b', 'average block propagation time [mili sec.]', 'M_time-plot.png')
for_plot.plt_set(blocksize_list, std_propagation_time_list, 'b', 'std block propagation time [mili sec.]', 'avstd-plot.png')

