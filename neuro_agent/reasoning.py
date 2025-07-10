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
    def __init__(self):
        self.machine = Machine(model=self, states=GilgameshAgent.states, initial='tyrant')

        self.machine.add_transition('meet_enkidu', 'tyrant', 'encounter_with_enkidu')
        self.machine.add_transition('lose_enkidu', 'encounter_with_enkidu', 'grief')
        self.machine.add_transition('seek_immortality', 'grief', 'quest_for_immortality')
        self.machine.add_transition('fail_quest', 'quest_for_immortality', 'limit_encounter')
        self.machine.add_transition('accept_limit', 'limit_encounter', 'return_to_city')

    def current_state(self):
        return self.state