from neuro_agent.agent import NeuroSymbolicAgent

agent = NeuroSymbolicAgent()

agent.transition("meet_enkidu")
agent.transition("lose_enkidu")
agent.transition("seek_immortality")
agent.transition("fail_quest")
agent.transition("accept_limit")


print("\n--- Memory Summary ---")
agent.memory.summarize()