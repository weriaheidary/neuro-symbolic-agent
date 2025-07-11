from neuro_agent.reasoning import GilgameshAgent

agent = GilgameshAgent()

agent.meet_enkidu()
agent.lose_enkidu()
agent.seek_immortality()
agent.fail_quest()
agent.accept_limit()

print("\n--- Memory Summary ---")
agent.memory.summarize()