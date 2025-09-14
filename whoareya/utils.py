def compare_players(target: dict, guess: dict) -> dict:
    """
    İki futbolçunun məlumatlarını müqayisə et, ipucu qaytar.
    """
    hints = {}

    # Klub
    hints["club"] = guess.get("club") == target.get("club")

    # Mövqe
    hints["position"] = guess.get("position") == target.get("position")

    # Milliyət
    hints["nationality"] = guess.get("nationality") == target.get("nationality")

    # Nömrə
    hints["number"] = guess.get("number") == target.get("number")

    # Yaş
    if guess.get("age") and target.get("age"):
        if guess["age"] == target["age"]:
            hints["age"] = "✅ Same"
        elif guess["age"] > target["age"]:
            hints["age"] = "⬇️ Lower"
        else:
            hints["age"] = "⬆️ Higher"
    else:
        hints["age"] = "Unknown"

    return hints
