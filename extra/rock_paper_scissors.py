import random


class Player:

    def __init__(self):
        self.moves = []
        self.score = 0

    def sum_round_victory(self):
        self.score += 1

    def store_move(self, option):
        self.moves.append(option)


ß


class HumanPlayer(Player):

    def choose_move(self):
        while True:
            option = input("Rock, paper or scissors [r/p/s]? ")
            if option not in ["r", "p", "s"]:
                print("Choose a valid option.")
            else:
                self.store_move(option)
                return option


class ComputerPlayer(Player):

    options = ["r", "p", "s"]

    def choose_move(self):
        option = random.choice(ComputerPlayer.options)
        self.store_move(option)
        return option


class Game:

    def __init__(self, human, computer, rounds):
        self.human = human
        self.computer = computer
        self.rounds = rounds

    def play_game(self):
        counter = 0
        while counter < self.rounds:
            human_option = self.human.choose_move()
            computer_option = self.computer.choose_move()
            result = self.__get_round_victory(human_option, computer_option)
            if result == 1:
                self.human.sum_round_victory()
            else:
                self.computer.sum_round_victory()
            counter += 1
            self.__summarize()
        result = self.__decide_winner()
        if result == 1:
            print(f"Your moves: {'|'.join(self.human.moves)}")
        else:
            print(f"Computer moves: {'|'.join(self.computer.moves)}")

    def __get_round_victory(self, human_option, computer_option):
        print(f"You: {human_option} | Computer: {computer_option}")
        if human_option == computer_option:
            print("This round is a tie")
        elif (
            (human_option == "r" and computer_option == "s")
            or (human_option == "p" and computer_option == "r")
            or (human_option == "s" and computer_option == "p")
        ):
            print("You won this round!")
            return 1
        else:
            print("You lost this round!")
            return 0

    def __summarize(self):
        print(
            f"[Game Summary] Your points: {self.human.score} | Computer Points {self.computer.score}"
        )

    def __decide_winner(self):
        if self.human.score == self.computer.score:
            print("The game is a tie")
        elif self.human.score > self.computer.score:
            print("You won")
            return 1
        else:
            print("You lost")
            return 0


def start_menu():
    print("Rock Paper Scissors Game")
    while True:
        try:
            return int(input("How many rounds do you want to play? "))
        except ValueError:
            print("Enter a valid number")


def main():
    rounds = start_menu()
    human = HumanPlayer()
    machine = ComputerPlayer()
    game = Game(human, machine, rounds)
    game.play_game()


if __name__ == "__main__":
    main()
