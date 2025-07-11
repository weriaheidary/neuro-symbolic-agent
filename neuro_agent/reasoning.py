# Reasoning module placeholder
from transitions import Machine
from neuro_agent.memory import NarrativeMemory

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
    state_affects = {
        "tyrant": "aggression",
        "encounter_with_enkidu": "curiosity",
        "grief": "sadness",
        "quest_for_immortality": "anxiety",
        "limit_encounter": "despair",
        "return_to_city": "acceptance"
    }
    def __init__(self):
        self.memory = NarrativeMemory()
        self.machine = Machine(model=self, states=GilgameshAgent.states, initial='tyrant')

        self.machine.add_transition('meet_enkidu', 'tyrant', 'encounter_with_enkidu')
        self.machine.add_transition('lose_enkidu', 'encounter_with_enkidu', 'grief')
        self.machine.add_transition('seek_immortality', 'grief', 'quest_for_immortality')
        self.machine.add_transition('fail_quest', 'quest_for_immortality', 'limit_encounter')
        self.machine.add_transition('accept_limit', 'limit_encounter', 'return_to_city')

        self.log_current_state()

    def log_current_state(self):
        self.memory.record(
            state=self.state,
            meaning=self.current_meaning(),
            emotion=self.current_emotion()
        )

    # override transitions to log after each change
    def meet_enkidu(self):
        self.trigger('meet_enkidu')
        self.log_current_state()

    def lose_enkidu(self):
        self.trigger('lose_enkidu')
        self.log_current_state()

    def seek_immortality(self):
        self.trigger('seek_immortality')
        self.log_current_state()

    def fail_quest(self):
        self.trigger('fail_quest')
        self.log_current_state()

    def accept_limit(self):
        self.trigger('accept_limit')
        self.log_current_state()

    def current_state(self):
        return self.state
    
    def current_meaning(self):
        return self.state_meanings.get(self.state, "Unknown state")
    
    def current_emotion(self):
        return self.state_affects.get(self.state, "neutral")