import datetime
import count
import os
import para

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

def mk_note():    
    dirnum = count.countdir('./results_graph/')
    save_file_at_dir('./results_graph/file{}'.format(dirnum), 'settings_note.txt', 'Parameter notes')

    path_w = './results_graph/file{}/settings_note.txt'.format(dirnum)
    s0 = 'timestamp : '+str(datetime.datetime.now())
    s1 = '\n\ninterval : '+ str(para.interval/(1000*60))+'[min]'
    s2 = '\nnode num : '+ str(para.node_num)+'[個]'
    s3 = '\nchange para : '+ para.paraname_list[para.paranum]
    s4 = '\nparalist : '+ str(para.parameter_list)+' [Byte]'
    s5 = '\npropagation_rate :'+str(para.propagation_rate)+'[割合]'

    with open(path_w, mode='w') as f:
        f.write(s0+s1+s2+s3+s4+s5)



