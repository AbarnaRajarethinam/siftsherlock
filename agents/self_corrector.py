def self_correct(findings):
    corrected = []

    for finding in findings:
        confidence = finding["confidence"]
        verified = finding["verified"]

        if verified and confidence >= 0.80:
            finding["reanalysis_required"] = False
            finding["severity"] = "verified"

        elif confidence >= 0.70:
            finding["reanalysis_required"] = True
            finding["severity"] = "needs additional validation"
            finding["claim"] += " [NEEDS ADDITIONAL VALIDATION]"

        elif confidence >= 0.50:
            finding["reanalysis_required"] = True
            finding["severity"] = "moderate uncertainty"
            finding["claim"] += " [REQUIRES FURTHER INVESTIGATION]"

        else:
            finding["reanalysis_required"] = True
            finding["severity"] = "critical uncertainty"
            finding["claim"] += " [LOW CONFIDENCE - DO NOT REPORT AS CONFIRMED]"

        corrected.append(finding)

    return corrected