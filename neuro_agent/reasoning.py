# Reasoning module placeholder
from transitions import Machine
from neuro_agent.memory import NarrativeMemory

class GilgameshFSM:
    states = [
        "tyrant",
        "encounter_with_enkidu",
        "grief",
        "quest_for_immortality",
        "limit_encounter",
        "return_to_city",
    ]
    def __init__(self):
        self.machine = Machine(model=self, states=self.states, initial='tyrant')
        self._bind_transitions()

    def _bind_transitions(self):
        self.machine.add_transition('meet_enkidu', 'tyrant', 'encounter_with_enkidu')
        self.machine.add_transition('lose_enkidu', 'encounter_with_enkidu', 'grief')
        self.machine.add_transition('seek_immortality', 'grief', 'quest_for_immortality')
        self.machine.add_transition('fail_quest', 'quest_for_immortality', 'limit_encounter')
        self.machine.add_transition('accept_limit', 'limit_encounter', 'return_to_city')

    
    def current_meaning(self):
        meanings = {
            "tyrant": "Will to control; denial of death or limit.",
            "encounter_with_enkidu": "A mirror encounter; emergence of the Other.",
            "grief": "Loss of the idealized self; first touch of mortality.",
            "quest_for_immortality": "A desperate displacement to escape grief.",
            "limit_encounter": "Collision with the boundary of human condition.",
            "return_to_city": "Integration of limit; subjectivized leadership."
        }
        return meanings.get(self.state, "")

    def current_emotion(self):
        emotions = {
            "tyrant": "aggression",
            "encounter_with_enkidu": "curiosity",
            "grief": "sadness",
            "quest_for_immortality": "anxiety",
            "limit_encounter": "despair",
            "return_to_city": "acceptance"
        }
        return emotions.get(self.state, "")