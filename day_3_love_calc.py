def calculate_love_score(name1, name2):
    true_count = (name1.lower() + name2.lower()).count('t') + \
                 (name1.lower() + name2.lower()).count('r') + \
                 (name1.lower() + name2.lower()).count('u') + \
                 (name1.lower() + name2.lower()).count('e')
    
    love_count = (name1.lower() + name2.lower()).count('l') + \
                 (name1.lower() + name2.lower()).count('o') + \
                 (name1.lower() + name2.lower()).count('v') + \
                 (name1.lower() + name2.lower()).count('e')
    
    love_score = int(str(true_count) + str(love_count))
    
    return love_score


def interpret_love_score(love_score):
    if love_score < 10 or love_score > 90:
        return f"Your score is {love_score}, you go together like coke and mentos."
    elif 40 <= love_score <= 50:
        return f"Your score is {love_score}, you are alright together."
    else:
        return f"Your score is {love_score}."


def main():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    print("The Love Calculator is calculating your score...")
    love_score = calculate_love_score(name1, name2)
    print(interpret_love_score(love_score))


if __name__ == "__main__":
    main()
