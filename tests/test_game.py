import unittest
from whoareya.game import WhoAreYaGame

class FakeAPI:
    """Sadə test API-si: yalnız statik futbolçuları qaytarır."""
    def __init__(self):
        self.players = [
            {"name": "Lionel Messi", "club": "Inter Miami", "position": "Forward", "age": 36, "number": 10, "nationality": "Argentina"},
            {"name": "Cristiano Ronaldo", "club": "Al Nassr", "position": "Forward", "age": 39, "number": 7, "nationality": "Portugal"}
        ]

    def search_player(self, name):
        for p in self.players:
            if p["name"].lower() == name.lower():
                return p
        return None

    def random_player(self):
        return self.players[0]  # Messi seçək test üçün


class WhoAreYaGameTest(unittest.TestCase):
    def setUp(self):
        self.api = FakeAPI()
        self.game = WhoAreYaGame(self.api)

    def test_correct_guess(self):
        guess = self.api.search_player("Lionel Messi")
        result = self.game.guess(guess)
        self.assertTrue(self.game.is_won(guess))
        self.assertEqual(result["club"], "✅")

    def test_wrong_guess(self):
        guess = self.api.search_player("Cristiano Ronaldo")
        result = self.game.guess(guess)
        self.assertFalse(self.game.is_won(guess))
        self.assertIn("❌", result["club"])  # Messi deyil deyə klub səhv olmalıdı

    def test_attempts_decrease(self):
        guess = self.api.search_player("Cristiano Ronaldo")
        _ = self.game.guess(guess)
        self.assertEqual(self.game.attempts_left, 5)

if __name__ == "__main__":
    unittest.main()
