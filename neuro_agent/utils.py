# neuro_agent/utils.py

import plotly.graph_objs as go

# Emotion-to-numeric scale
emotion_scale = {
    "aggression": 0.8,
    "curiosity": 0.5,
    "sadness": -0.5,
    "anxiety": -0.7,
    "despair": -0.9,
    "acceptance": 0.4
}

def plot_trajectory(agent):
    events = agent.memory.recall()

    if not events:
        print("No memory events to plot.")
        return

    times = [e["timestamp"] for e in events]
    emotion_values = [emotion_scale.get(e["emotion"], 0.0) for e in events]
    labels = [f"{e['emotion'].capitalize()}: {e['meaning']}" for e in events]

    trace = go.Scatter(
        x=times,
        y=emotion_values,
        mode='lines+markers',
        text=labels,
        hoverinfo='text',
        line=dict(shape='spline', color='royalblue'),
        marker=dict(size=10)
    )

    layout = go.Layout(
        title="Agent Emotional Trajectory",
        xaxis=dict(title="Time"),
        yaxis=dict(title="Emotion Intensity", range=[-1, 1]),
        height=500
    )

    fig = go.Figure(data=[trace], layout=layout)
    fig.show()
