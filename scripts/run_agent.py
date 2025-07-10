from neuro_agent.reasoning import GilgameshAgent

agent = GilgameshAgent()

def print_state(agent):
    print(f"State: {agent.state} | Meaning: {agent.current_meaning()} | Emotion: {agent.current_emotion()}")

print_state(agent)
agent.meet_enkidu()
print_state(agent)
agent.lose_enkidu()
print_state(agent)
