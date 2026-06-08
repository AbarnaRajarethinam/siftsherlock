def verify_findings(findings, memory_data):

    verified_findings = []

    for finding in findings:

        confidence = finding["confidence"]

        if confidence >= 0.85:
            finding["verified"] = True
            finding["reason"] = "Strong supporting evidence"

        elif confidence >= 0.65:
            finding["verified"] = False
            finding["reason"] = "Moderate evidence requires validation"

        else:
            finding["verified"] = False
            finding["reason"] = "Weak supporting evidence"

        verified_findings.append(finding)

    return verified_findings