# Test our agent's reasoning capabilities
from neuro_agent.reasoning import GilgameshAgent

agent = GilgameshAgent()

print("Initial:", agent.current_state())
agent.meet_enkidu()
print("After meeting Enkidu:", agent.current_state())
agent.lose_enkidu()
print("After Enkidu dies:", agent.current_state())
agent.seek_immortality()
agent.fail_quest()
agent.accept_limit()
print("Final state:", agent.current_state())