import random


COMMANDS = ("!exit", "!rating")
VARIANTS = {
    "rock": ["scissors"],
    "paper": ["rock"], 
    "scissors": ["paper"]
}
RESULT = {
    "win": {
        "txt": "Well done. The computer chose {} and failed",
        "score": 100
    },
    "lose": {
        "txt": "Sorry, but the computer chose {}",
        "score": 0
    },
    "draw": {
        "txt": "There is a draw ({})",
        "score": 50
    }
}


def command_handler(command, rating):
    if command == "!exit":
        print("Bye!")
        return True
    print(f"Your rating: {rating}")
    return False


def greetings():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    return name


def define_variants():
    variants = {}
    variants_input = input()
    print("Okay, let's start")
    
    if not variants_input:
        return VARIANTS
        
    variants_input = variants_input.split(",")
    v_len = len(variants_input)
    i = 0
    for v in variants_input:
        tmp_list = variants_input[-(v_len - i - 1):] + variants_input[:i]
        variants[v] = tmp_list[-(v_len // 2):]
        i += 1
    return variants


def set_rating(name):
    rating = 0
    with open("rating.txt", "r") as f:
        for line in f:
            if name + " " in line:
                rating = int(line.split()[-1])
    return rating


def main():
    name = greetings()
    variants = define_variants()
    rating = set_rating(name)
                
    while True:
        user = input()
        
        if user in COMMANDS:
            if command_handler(user, rating):
                break
                
        if user not in variants:
            print("Invalid input")
            continue
            
        computer = random.choice(list(variants))
        if user == computer:
            result = "draw"
        elif computer in variants[user]:
            result = "win"
        else:
            result = "lose"
        rating += RESULT[result]["score"]
        print(RESULT[result]["txt"].format(computer))


if __name__ == "__main__":
    main()
