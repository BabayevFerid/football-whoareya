import requests
import random
import os


class FootballAPI:
    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self, api_key: str):
        self.headers = {"x-apisports-key": api_key}

    def get_random_player(self, league_id: int = 39) -> dict:
        """
        league_id: 39 → Premier League, 140 → La Liga, və s.
        """
        # Çox oyunçu siyahısından random seçək
        url = f"{self.BASE_URL}/players?league={league_id}&season=2023"
        response = requests.get(url, headers=self.headers)
        data = response.json()

        if "response" not in data or not data["response"]:
            raise Exception("No player data found from API.")

        players = data["response"]
        player = random.choice(players)["player"]

        return {
            "name": player.get("name"),
            "age": player.get("age"),
            "number": player.get("number"),
            "position": player.get("position"),
            "nationality": player.get("nationality"),
            "club": player.get("team", {}).get("name") if "team" in player else None,
        }
