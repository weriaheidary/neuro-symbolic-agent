from neuro_agent.reasoning import GilgameshFSM
from neuro_agent.memory import NarrativeMemory
from neuro_agent.perception import PerceptionModule

class NeuroSymbolicAgent:
    def __init__(self):
        self.reasoning = GilgameshFSM()
        self.memory = NarrativeMemory()
        self.perception = PerceptionModule()

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
    
    def narrate(self):
        state = self.reasoning.state
        meaning = self.reasoning.current_meaning()
        emotion = self.reasoning.current_emotion()
        return f"In the state of {state}, I feel {emotion}. This means: {meaning}"
    
    def perceive_and_act(self, input_text: str):
        event = self.perception.interpret(input_text)
        if event:
            self.transition(event)
        else:
            print(f"No event matched for: {input_text}")
