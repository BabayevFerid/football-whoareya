#!/usr/bin/env python3
from whoareya.api import FootballAPI
from whoareya.game import WhoAreYaGame

API_KEY = "YOUR_API_KEY_HERE"  # buraya öz API-Football açarını yaz


def main():
    api_client = FootballAPI(API_KEY)
    game = WhoAreYaGame(api_client)

    print("⚽ Welcome to Football Who Are Ya!")
    print("Try to guess the footballer. You have 6 attempts.\n")

    while not game.is_over():
        guess_name = input("Enter a player name: ").strip()

        # İstifadəçinin təxmin etdiyi oyunçu məlumatını API-dən çəkək
        try:
            # Axtarış
            guess_data = api_client.search_player(guess_name)
            if not guess_data:
                print("❌ Player not found in API.")
                continue
        except Exception as e:
            print(f"⚠️ API error: {e}")
            continue

        result = game.guess(guess_data)

        if game.is_won(guess_data):
            print(f"\n🎉 Correct! The player was {game.target['name']}")
            print("📌 Details:")
            for k, v in game.target.items():
                print(f"- {k.capitalize()}: {v}")
            break
        else:
            print(f"\n❌ Wrong guess: {guess_name}")
            print("Hints:")
            for k, v in result.items():
                print(f"- {k.capitalize()}: {v}")
            print(f"Attempts left: {game.attempts_left}\n")

    if game.is_over():
        print(f"\n💀 Game over! The player was {game.target['name']}")


if __name__ == "__main__":
    main()
