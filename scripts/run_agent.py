from neuro_agent.agent import NeuroSymbolicAgent

agent = NeuroSymbolicAgent()

inputs = [
    "Gilgamesh meets Enkidu in the forest",
    "He is devastated by Enkidu's death",
    "He seeks eternal life to avoid suffering",
    "He fails in his quest for immortality",
    "Finally, he accepts the limits of being human"
]

for sentence in inputs:
    print(f"\n Input: {sentence}")
    agent.perceive_and_act(sentence)
    print(f"{agent.narrate()} Gilgamesh said.")
