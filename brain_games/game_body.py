def game_beginning(game, name):
    for i in range(3):
        answer, correct_answer = game()
        if answer != correct_answer:
            print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}
                        Let's try again, {name}!""")
            return
        print('Correct!')
    print(f'Congratulations, {name}')
