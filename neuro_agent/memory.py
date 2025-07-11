# Memory module placeholder
from typing import List, Dict
from datetime import datetime

class NarrativeMemory:

    def __init__(self):
        self.events: List[Dict] = []

    def record(self, state: str, meaning: str, emotion: str):
        self.events.append({
            'state': state,
            "meaning": meaning,
            "emotion": emotion,
            "timestamp": datetime.utcnow().isoformat()
        })

    def recall(self) -> List[Dict]:
        return self.events
    
    def summarize(self):
        for i, e in enumerate(self.events):
            print(f"[{i+1}] At state '{e['state']}', felt '{e['emotion']}': {e['meaning']}")