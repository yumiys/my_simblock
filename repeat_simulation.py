import count
import explain_text
import para
import simple_cmd

para_list = para.paraname_list
now_para = para_list[para.paranum]
interval = para.interval
blocknum = para.node_num

# calling list of para.py
blocksize_list = []
for i in para.parameter_list:
    blocksize_list.append(i)

# update parameters
for blocksize in blocksize_list:
    infilename = 'SimulationConfiguration.java'
    with open(infilename, 'r') as infile:
        contents = infile.read()
        contents_modified = contents.replace('BLOCK_SIZE = 100000', 'BLOCK_SIZE = {}'.format(blocksize)).replace('NUM_OF_NODES = 300', 'NUM_OF_NODES = {}'.format(blocknum)).replace('INTERVAL = 1000 * 60 * 10', 'INTERVAL = {}'.format(interval))

    path = './simblock/simulator/src/main/java/simblock/settings/'
    outfilename = 'SimulationConfiguration.java'
    with open(path+outfilename, 'w') as outfile:
        outfile.write(contents_modified)

    # compile
    simple_cmd.command('cd simblock; gradle build; cd ..')

    # run
    result = simple_cmd.command('cd simblock; gradle :simulator:run; cd ..')

    # save blockList.txt into blocklists directory
    simple_cmd.command('cp ./simblock/simulator/src/dist/output/blockList.txt ./blocklists/blockList-{}{:010}.txt'.format(now_para, blocksize))

    # output result
    stdoutfilename = './stdouts/result-{}{:010}.txt'.format(now_para, blocksize)
    with open(stdoutfilename, 'w') as stdoutfile:
        stdoutfile.write(result.stdout.decode())
        
# create a directory to save results
dirnum = count.countdir('./results_graph/')
simple_cmd.command('mkdir ./results_graph/file{}'.format(dirnum+1))

# create explanatory txt.file
explain_text.mk_note()

# check if output file exists  
filenum1 = count.countfile('./blocklists')
filenum2 = count.countfile('./stdouts')
if filenum1 == len(para.parameter_list) and filenum2 == len(para.parameter_list):
    print('Successfully executed a program called repeat_simulation.py')
else:
    print('Simulation failed. Not enough files')



