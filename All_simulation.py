import simple_cmd

print('simulation start')
simple_cmd.command('python3 dust.py')

print('running...')

# run the simulation
simple_cmd.command('python3 repeat_simulation.py')

# analyze the results
simple_cmd.command('python3 run_analyses.py')

    
print('simulation finish')





