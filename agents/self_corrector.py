def self_correct(findings):
    corrected = []

    for finding in findings:
        confidence = finding.get("confidence", 0)
        verified = finding.get("verified", False)

        analysis = finding.get("analysis", {})

        if verified and confidence >= 0.85:
            finding["reanalysis_required"] = False
            finding["severity"] = "verified"

        elif confidence >= 0.65:
            finding["reanalysis_required"] = True
            finding["severity"] = "needs additional validation"
            analysis["finding"] = (
                analysis.get("finding", "Suspicious activity detected")
                + " [NEEDS ADDITIONAL VALIDATION]"
            )

        elif confidence >= 0.50:
            finding["reanalysis_required"] = True
            finding["severity"] = "moderate uncertainty"
            analysis["finding"] = (
                analysis.get("finding", "Suspicious activity detected")
                + " [REQUIRES FURTHER INVESTIGATION]"
            )

        else:
            finding["reanalysis_required"] = True
            finding["severity"] = "critical uncertainty"
            analysis["finding"] = (
                analysis.get("finding", "Suspicious activity detected")
                + " [LOW CONFIDENCE - DO NOT REPORT AS CONFIRMED]"
            )

        finding["analysis"] = analysis
        corrected.append(finding)

    return corrected