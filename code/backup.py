from src.ranking_c.ranking import (
    friends
    )

def main():
    quiz = friends()

    print('------------')

    for name, rank, reason in quiz:
        print(f'{name} has a rank of {rank} because {reason}.')

    print('------------')
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()