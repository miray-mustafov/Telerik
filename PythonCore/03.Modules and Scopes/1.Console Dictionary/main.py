import instruction_runner

command = input()
while command != 'exit':
    print(instruction_runner.execute_instruction(command))
    command = input()
