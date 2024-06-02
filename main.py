import sys
import random
def main():
    current_round = int(sys.argv[1])
    opponent_previous = sys.argv[2]
    if current_round == 1:
        print(random.choice(["YES", "NO"]))
    else:
        if current_round <= 200:
            print(random.choice(["YES", "NO"]))

if __name__ == "__main__":
    main()