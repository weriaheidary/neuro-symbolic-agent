from neuro_agent.reasoning import GilgameshFSM
from neuro_agent.memory import NarrativeMemory

class NeuroSymbolicAgent:
    def __init__(self):
        self.reasoning = GilgameshFSM()
        self.memory = NarrativeMemory()

    def transition(self, event_name: str):
        if hasattr(self.reasoning, event_name):
            getattr(self.reasoning, event_name)()
            self.memory.record(
                state=self.reasoning.state,
                meaning=self.reasoning.current_meaning(),
                emotion=self.reasoning.current_emotion()
            )
        else:
            raise ValueError(f"No such event: {event_name}")

    def recall(self):
        return self.memory.recall()
