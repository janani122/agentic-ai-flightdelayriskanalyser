# Planner Agent
def planner_agent(state):

    state["plan"] = "Analyze weather, airport traffic, and aircraft delay"
    return state


# Analysis Agent
def analysis_agent(state):

    # Simulated data
    state["weather"] = "Heavy rain detected"
    state["traffic"] = "Runway congestion high"
    state["flight_status"] = "Incoming aircraft delayed by 15 minutes"
    state["gate"] = "Available"

    return state


# Decision Agent (NO LLM - WORKING VERSION)
def decision_agent(state):

    weather = state.get("weather")
    traffic = state.get("traffic")
    status = state.get("flight_status")

    if "rain" in weather.lower() or "congestion" in traffic.lower():
        decision = "High delay risk. Recommend rescheduling or preparing for delay."
    elif "delayed" in status.lower():
        decision = "Moderate delay risk due to late incoming aircraft."
    else:
        decision = "Low delay risk. Flight is likely on time."

    state["decision"] = decision
    return state