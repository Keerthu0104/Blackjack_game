import random
import os
import time
import sys
from colorama import init, Fore, Style
import art

init(autoreset=True)

# 🔢 Score tracking
wins = 0
losses = 0
draws = 0

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):
    """Returns (colored result message, result_type: 'win', 'loss', 'draw')"""
    if user == computer:
        return (Fore.BLUE + "It's a Draw 🙃", 'draw')
    elif computer == 0:
        return (Fore.RED + "You lose, opponent has Blackjack 😱", 'loss')
    elif user == 0:
        return (Fore.GREEN + "You win with a Blackjack 😎", 'win')
    elif user > 21:
        return (Fore.RED + "You went over. You lose 😭", 'loss')
    elif computer > 21:
        return (Fore.GREEN + "Opponent went over. You win 😁", 'win')
    elif user > computer:
        return (Fore.GREEN + "You win 😃", 'win')
    else:
        return (Fore.RED + "You lose 😤", 'loss')

def show_progress_bar(duration=2, steps=20):
    print(Fore.YELLOW + "Computer is drawing cards", end='')
    for _ in range(steps):
        sys.stdout.write(Fore.YELLOW + ".")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()  # Newline after bar

def play_game():
    print(Fore.CYAN + art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(Fore.WHITE + f"\nYour cards: {user_cards}, current score: {user_score}")
        print(Fore.WHITE + f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input(Fore.YELLOW + "Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    user_score = calculate_score(user_cards)

    if computer_score != 0 and computer_score < 17:
        show_progress_bar()

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(Fore.WHITE + f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(Fore.WHITE + f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    result_message, result_type = compare(user_score, computer_score)
    print(result_message)

    global wins, losses, draws
    if result_type == 'win':
        wins += 1
    elif result_type == 'loss':
        losses += 1
    elif result_type == 'draw':
        draws += 1

    print(Fore.MAGENTA + Style.BRIGHT + "\n🎮 GAME OVER 🎮")
    print(Fore.WHITE + f"🟢 Wins: {wins}  🔴 Losses: {losses}  🔵 Draws: {draws}\n")

# 🎮 Game loop
while True:
    print("\n" * 20)
    play_game()

    play_again = input(Fore.YELLOW + "🔁 " + Style.BRIGHT + "Play again? (y/n): ").lower()
    if play_again != 'y':
        print(Fore.CYAN + Style.BRIGHT + "\nThanks for playing! 👋")
        print(Fore.CYAN + f"Final Score — 🟢 Wins: {wins}, 🔴 Losses: {losses}, 🔵 Draws: {draws}")
        break
