import random

def play_game():
    options = ["камень", "ножницы", "бумага"]
    
    while True:
        user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
        
        if user_choice == "q":
            print("вы вышли из игры")
            break
            
        
        if user_choice not in options:
            print("попробуйте заново")
            continue
        
        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага")(user_choice == "бумага" and computer_choice == "камень"):
            print("Вы победили!")
        else:
            print("Компьютер победил!")


play_game()
