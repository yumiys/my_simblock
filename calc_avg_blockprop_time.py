#
# How to run: $ python3 calc_avg_blockprop_time.py ./Stdouts/*
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

# define variables and lists
blocksize_list = []
avg_proptime_list = []
std_proptime_list = []
nodenum = para.node_num
rate = para.propagation_rate

# read blocksize from para.py
for i in para.parameter_list:
    blocksize_list.append(i)

# calculate average block propagation time
sys.path.append('./home/Soturon/')
infilenames_list = sys.argv[1:]
for infilename in infilenames_list:
    previous_blockprop_time_list = []
    previous_flag = False
    line_counter = 0
    with open(infilename, 'r') as infile:
        for line in infile:
            data_list = line.replace('\n', '').split(',')
            if len(data_list) == 2 and isint(data_list[0]) and line_counter <= (math.floor(nodenum*rate)):
                previous_blockprop_time = int(data_list[1])
                previous_flag = True
                line_counter += 1 
            elif line_counter >= (math.floor(nodenum*rate)) and previous_flag == True:
                previous_blockprop_time_list.append(previous_blockprop_time)
                previous_flag = False
            elif data_list[0] == '':
                line_counter = 0
            else:
                continue

    print('len=',len(previous_blockprop_time_list))
    print('average:', np.average(previous_blockprop_time_list))
    avg_proptime_list.append(np.average(previous_blockprop_time_list))
    std_proptime_list.append(np.std(previous_blockprop_time_list))

    # write standard output to a file named average_time.txt
    av_outfilename = './Average_time/average_time.txt'
    with open(av_outfilename, 'a') as stdoutfile:
        print(str(np.average(previous_blockprop_time_list)), file=stdoutfile)
        

# plot figures
for_plot.plt_set(blocksize_list, avg_proptime_list, 'b', 'average block propagation time [mili sec.]', 'M_time-plot.png')
for_plot.plt_set(blocksize_list, std_proptime_list, 'b', 'std block propagation time [mili sec.]', 'avstd-plot.png')

