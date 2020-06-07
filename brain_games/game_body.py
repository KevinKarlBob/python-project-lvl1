def game_beginning(game, name):
    counter = 0
    while counter < 3:
        counter += 1
        result = game()
        if not result[0]:
            print(f"""{result[1]} is wrong answer ;(. Correct answer was {result[2]}
                 Let's try again, {name}!""")
            break
        print('Correct!')
        if counter == 3:
            print(f'Congratulations,{name}')
            break
