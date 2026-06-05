def generate_findings(memory_data):
    findings = []

    for proc in memory_data["processes"]:
        if proc["suspicious"]:
            findings.append({
                "claim": f"Suspicious process detected: {proc['name']}",
                "confidence": 0.85,
                "verified": False
            })

    return findings