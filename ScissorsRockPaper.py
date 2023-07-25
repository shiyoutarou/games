import random

def get_user_choice():
    while True:
        user_choice = input("請輸入你的選擇（剪刀/石頭/布）：").lower()
        if user_choice in ["剪刀", "石頭", "布"]:
            return user_choice
        else:
            print("請輸入有效的選擇（剪刀/石頭/布）！")

def get_computer_choice():
    choices = ["剪刀", "石頭", "布"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平手"
    elif (user_choice == "剪刀" and computer_choice == "布") or \
         (user_choice == "石頭" and computer_choice == "剪刀") or \
         (user_choice == "布" and computer_choice == "石頭"):
        return "你贏了！"
    else:
        return "電腦贏了！"

def play_again():
    return input("要再玩一次嗎？（是/否）：").lower().startswith("是")

def main():
    print("歡迎來到剪刀石頭布遊戲！")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"你選擇了：{user_choice}")
        print(f"電腦選擇了：{computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if not play_again():
            print("謝謝你玩剪刀石頭布遊戲！再見！")
            break

if __name__ == "__main__":
    main()
