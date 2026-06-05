def create_plan(memory_data):
    plan = []

    if memory_data.get("processes"):
        plan.append("process_analysis")

    if memory_data.get("network_connections"):
        plan.append("network_analysis")

    if memory_data.get("registry"):
        plan.append("persistence_analysis")

    return plan