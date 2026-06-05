def generate_report(findings):

    report = "\n=== FINAL INVESTIGATION REPORT ===\n"

    for finding in findings:

        report += f"\nFinding: {finding['claim']}"
        report += f"\nConfidence: {round(finding['confidence'],2)}"
        report += f"\nVerified: {finding['verified']}"

        if finding.get("reanalysis_required"):
            report += "\nAction: Additional analysis recommended"

        report += "\n"

    return report