def verify_findings(findings, memory_data):

    for finding in findings:

        confidence = finding["confidence"]

        network_support = False
        injection_support = False
        persistence_support = False

        for conn in memory_data["network_connections"]:
            if conn["suspicious"]:
                network_support = True

        if memory_data["dll_injection"].get("powershell.exe"):
            injection_support = True

        if memory_data["registry"]["run_keys"]:
            persistence_support = True

        supporting_count = sum([
            network_support,
            injection_support,
            persistence_support
        ])

        if supporting_count >= 2:
            confidence += 0.15
            finding["verified"] = True

        elif supporting_count == 1:
            confidence -= 0.10
            finding["verified"] = False
            finding["reason"] = "Weak supporting evidence"

        else:
            confidence -= 0.40
            finding["verified"] = False
            finding["reason"] = "Contradictory or insufficient evidence"

        finding["confidence"] = round(confidence, 2)

    return findings