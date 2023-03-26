import json


def turing_machine(config, input_word):
    # Ustalam wartosci poczatkowe tasmy, glowicy itd
    tape = ['znak_pusty'] * 1000
    head_position = 0
    current_state = config['initial_state']

    for symbol in input_word:
        tape[head_position] = symbol
        head_position += 1
    head_position = 0
    print(f'Initial tape: {tape}')
    print(f'Initial state: {current_state}')

    while current_state not in config['accepted_states'] and current_state not in config['rejected_states']:
        print('=' * 100)
        current_symbol = tape[head_position]
        if current_symbol not in config['tape_alphabet']:
            return 'Rejected'

        print(f'Head position: {head_position}')
        print(f'Current symbol: {current_symbol}')
        print(f'Current state: {current_state}')

        transition = config['transitions'][current_state][current_symbol]
        if transition is None:
            return 'Rejected'

        print(f'Transition: {transition}')
        tape[head_position] = transition[1]
        if transition[2] == 'R':
            head_position += 1
        else:
            head_position += -1
        if head_position < 0:
            head_position = 0
        current_state = transition[0]
        print(f'New tape: {tape}')
        print(f'New state: {current_state}')
    if current_state in config['accepted_states']:
        return 'Accepted'
    else:
        return 'Rejected'


# Otwieram plik konfiguracyjny do zadania i uruchamiam maszyne dla zadanego slowa
with open('config_turing_machine_1.json') as f:
    config = json.load(f)

input_word = str(input("Podaj slowo: "))
result = turing_machine(config, input_word)
print(result)
