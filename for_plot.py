import numpy as np
import matplotlib.pyplot as plt
import count

def plt_set(x, y, color, ylab ,file_name):
    #default[width:6.4, height:4.8]
    plt.figure(figsize=(7,4))
    
    #call before plt.plot(x,y)
    plt.rcParams['xtick.direction']='in' 
    plt.rcParams['ytick.direction']='in'
    
    plt.plot(x, y, color='{}'.format(color), ls= '-')
    plt.xscale('log')
    
    plt.xlabel('blocksize [B.]')
    plt.ylabel(ylab)
    
    n = count.countdir('./results_graph/')
    plt.savefig('./results_graph/file{}/{}'.format(n, file_name))
    plt.clf()
