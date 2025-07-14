# Perception module placeholder

class PerceptionModule:
    def interpret(self, input_text: str) -> str | None:
        # Very basic rule-based example:
        input_text = input_text.lower()
        # Priority matters: more specific → earlier
        if any(word in input_text for word in ["fail", "impossible", "defeat"]):
            return "fail_quest"
        if any(word in input_text for word in ["eternal", "immortal", "escape death", "live forever"]):
            return "seek_immortality"
        if "enkidu" in input_text and "meet" in input_text:
            return "meet_enkidu"
        if any(word in input_text for word in ["death", "die", "loss", "devastated", "mourning", "grief"]):
            return "lose_enkidu"
        if any(word in input_text for word in ["accept", "return", "limit", "human"]):
            return "accept_limit"

        return None