import subprocess

# function to easily execute commands
def command(x):
    cmd = '{}'.format(x)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return result
