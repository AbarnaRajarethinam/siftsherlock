import json
from datetime import datetime

LOG_FILE = "logs/execution_log.json"

def write_log(agent, action, result):

    log_entry = {
        "timestamp": str(datetime.now()),
        "agent": agent,
        "action": action,
        "result": result
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)