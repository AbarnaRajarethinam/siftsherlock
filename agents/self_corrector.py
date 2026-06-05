def self_correct(findings):

    corrected = []

    for finding in findings:

        if finding["confidence"] < 0.70:

            finding["reanalysis_required"] = True

            finding["claim"] += " [REQUIRES FURTHER INVESTIGATION]"

            if finding["confidence"] < 0.50:
                finding["severity"] = "critical uncertainty"
            else:
                finding["severity"] = "moderate uncertainty"

        else:
            finding["reanalysis_required"] = False
            finding["severity"] = "verified"

        corrected.append(finding)

    return corrected