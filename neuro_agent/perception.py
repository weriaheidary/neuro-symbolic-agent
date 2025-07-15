# Perception module placeholder
from sentence_transformers import SentenceTransformer, util
from pathlib import Path
    

class PerceptionModule:
    def __init__(self):
        model_path = Path(__file__).parent / "fine_tuned_sbert"
        self.model = SentenceTransformer(str(model_path))
        self.labels = {
            "meet_enkidu": "Gilgamesh meets Enkidu",
            "lose_enkidu": "Enkidu dies and Gilgamesh mourns",
            "seek_immortality": "Gilgamesh seeks eternal life",
            "fail_quest": "Gilgamesh fails in his quest",
            "accept_limit": "He accepts the limits of mortality"
        }
        self.label_embeddings = self.model.encode(list(self.labels.values()), convert_to_tensor=True)

    def interpret(self, input_text: str) -> str | None:
        input_embedding = self.model.encode(input_text, convert_to_tensor=True)
        similarities = util.cos_sim(input_embedding, self.label_embeddings)[0]  # type: ignore

        best_match_idx = int(similarities.argmax())
        best_score = float(similarities[best_match_idx])
        threshold = 0.6

        if best_score >= threshold:
            return list(self.labels.keys())[best_match_idx]
        return None
