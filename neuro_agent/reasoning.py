# Reasoning module placeholder
from transitions import Machine

class GilgameshAgent:
    states = [
        "tyrant",
        "encounter_with_enkidu",
        "grief",
        "quest_for_immortality",
        "limit_encounter",
        "return_to_city",
    ]
    state_meanings = {
        "tyrant": "Will to control; denial of death or limit.",
        "encounter_with_enkidu": "A mirror encounter; emergence of the Other.",
        "grief": "Loss of the idealized self; first touch of mortality.",
        "quest_for_immortality": "A desperate displacement to escape grief.",
        "limit_encounter": "Collision with the boundary of human condition.",
        "return_to_city": "Integration of limit; subjectivized leadership."
    }
    def __init__(self):
        self.machine = Machine(model=self, states=GilgameshAgent.states, initial='tyrant')

        self.machine.add_transition('meet_enkidu', 'tyrant', 'encounter_with_enkidu')
        self.machine.add_transition('lose_enkidu', 'encounter_with_enkidu', 'grief')
        self.machine.add_transition('seek_immortality', 'grief', 'quest_for_immortality')
        self.machine.add_transition('fail_quest', 'quest_for_immortality', 'limit_encounter')
        self.machine.add_transition('accept_limit', 'limit_encounter', 'return_to_city')

    def current_state(self):
        return self.state
    
    def current_meaning(self):
        return self.state_meanings.get(self.state, "Unknown state")