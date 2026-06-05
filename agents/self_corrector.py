def self_correct(findings):

    corrected = []

    for finding in findings:

        if finding["confidence"] < 0.70:
            finding["claim"] += " (LOW CONFIDENCE)"
            finding["reanalysis_required"] = True

        corrected.append(finding)

    return corrected