import numpy as np
import matplotlib.pyplot as plt
import count

# x : vertical axis list
# y : horizontal axis list
# file_name : file name when outputting

def plt_set(x, y, color, ylab ,file_name):
    #default[width:6.4, height:4.8]
    plt.figure(figsize=(7,4))
    
    #call before plt.plot(x,y)
    plt.rcParams['xtick.direction']='in' 
    plt.rcParams['ytick.direction']='in'
    
    if ylab == 'fork probability':
        xmin,xmax = x[0],x[-1]
        plt.hlines(0.05, xmin, xmax, linestyles='dashed')
    
    plt.plot(x, y, color='{}'.format(color), ls= '-', marker='.')
    plt.xscale('log')
    
    plt.xlabel('blocksize [B.]')
    plt.ylabel(ylab)
    
    n = count.countdir('./results_graph/')
    plt.savefig('./results_graph/file{}/{}'.format(n, file_name))
    plt.clf()
