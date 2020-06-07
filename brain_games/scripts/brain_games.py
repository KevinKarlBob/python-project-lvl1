from brain_games.cli import welcome_user


def greeting(special_greeting=None):
    print('Welcome to the Brain Games!')
    if special_greeting:
        print(special_greeting)


def main():
    greeting()
    welcome_user()


if __name__ == '__main__':
    main()
