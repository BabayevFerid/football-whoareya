from .utils import compare_players


class WhoAreYaGame:
    MAX_ATTEMPTS = 6

    def __init__(self, api_client):
        self.api_client = api_client
        self.target = self.api_client.get_random_player()
        self.attempts_left = self.MAX_ATTEMPTS
        self.history = []

    def guess(self, player: dict) -> dict:
        if self.attempts_left <= 0:
            raise RuntimeError("No attempts left!")

        self.attempts_left -= 1
        result = compare_players(self.target, player)
        self.history.append({"guess": player["name"], "result": result})

        return result

    def is_won(self, guess: dict) -> bool:
        return guess.get("name") == self.target.get("name")

    def is_over(self) -> bool:
        return self.attempts_left <= 0
