def verify_findings(findings, memory_data):

    for finding in findings:

        supporting_evidence = False

        for conn in memory_data["network_connections"]:
            if conn["suspicious"]:
                supporting_evidence = True

        if supporting_evidence:
            finding["verified"] = True
            finding["confidence"] += 0.10
        else:
            finding["confidence"] -= 0.30

    return findings