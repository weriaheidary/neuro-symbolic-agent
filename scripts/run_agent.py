from neuro_agent.reasoning import GilgameshAgent

agent = GilgameshAgent()

print("State:", agent.state, "| Meaning:", agent.current_meaning())
agent.meet_enkidu()
print("State:", agent.state, "| Meaning:", agent.current_meaning())
agent.lose_enkidu()
print("State:", agent.state, "| Meaning:", agent.current_meaning())
