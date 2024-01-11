#
# How to run: $ python3 All_simulation.py
#

import simple_cmd

print('simulation start')
# delete existing results
simple_cmd.command('python3 dust.py')

print('running...')
# run the simulation
simple_cmd.command('python3 repeat_simulation.py')

print('start analysis')
# analyze the results
simple_cmd.command('python3 Run_analyses.py')

print('simulation finish')





