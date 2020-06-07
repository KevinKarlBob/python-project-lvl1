def game_beginning(game, name):
    counter = 0
    while counter < 3:
        counter += 1
        answer, correct_answer = game()
        if answer != correct_answer:
            print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}
                 Let's try again, {name}!""")
            break
        print('Correct!')
        if counter == 3:
            print(f'Congratulations,{name}')
            break
