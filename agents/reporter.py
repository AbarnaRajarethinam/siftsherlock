def generate_report(findings):

    report = "\n=== FINAL INVESTIGATION REPORT ===\n"

    for item in findings:

        analysis = item["analysis"]

        report += f"\nPROCESS: {item['process']} (PID: {item['pid']})\n"
        report += f"Severity: {analysis['severity'].upper()}\n"
        report += f"Confidence: {analysis['confidence']}\n"
        report += f"Verified: {item['verified']}\n"
        report += f"Validation Status: {item.get('severity', 'unknown')}\n"

        report += "\nFinding:\n"
        report += f"- {analysis['finding']}\n"

        report += "\nSupporting Evidence:\n"

        for ev in analysis["evidence"]:
            report += f"  • {ev}\n"

        report += "\nMissing Evidence:\n"

        for miss in analysis["missing_evidence"]:
            report += f"  • {miss}\n"

        report += "\nRecommended Actions:\n"

        for action in analysis["recommended_actions"]:
            report += f"  • {action}\n"

        report += "\n----------------------------------------\n"

    return report