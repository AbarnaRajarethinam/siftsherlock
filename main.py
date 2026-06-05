import json
import os

from agents.planner import create_plan
from agents.finder import generate_findings
from agents.verifier import verify_findings
from agents.self_corrector import self_correct
from agents.reporter import generate_report
from tools.log_writer import write_log


DATA_FILE = "data/sample_memory_output.json"
LOG_FILE = "logs/execution_log.json"


def load_memory_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Memory data file not found: {file_path}")

    with open(file_path, "r") as f:
        return json.load(f)


def reset_logs():
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "w") as f:
        json.dump([], f, indent=4)


def main():
    reset_logs()

    print("\n=== SIFTSHERLOCK: SELF-CORRECTING MEMORY FORENSICS AGENT ===")

    memory_data = load_memory_data(DATA_FILE)

    print("\n=== INVESTIGATION PLAN ===")
    plan = create_plan(memory_data)
    print(plan)
    write_log(
        "Planner Agent",
        "Generated investigation plan",
        plan
    )

    print("\n=== GENERATING FINDINGS ===")
    findings = generate_findings(memory_data)
    print(findings)
    write_log(
        "Finding Agent",
        "Generated preliminary findings",
        findings
    )

    print("\n=== VERIFYING FINDINGS ===")
    verified_findings = verify_findings(findings, memory_data)
    print(verified_findings)
    write_log(
        "Verification Agent",
        "Verified findings against supporting evidence",
        verified_findings
    )

    print("\n=== SELF CORRECTION ===")
    corrected_findings = self_correct(verified_findings)
    print(corrected_findings)
    write_log(
        "Self-Correction Agent",
        "Applied confidence-based correction logic",
        corrected_findings
    )

    print("\n=== FINAL REPORT ===")
    final_report = generate_report(corrected_findings)
    print(final_report)
    write_log(
        "Report Agent",
        "Generated final investigation report",
        final_report
    )

    os.makedirs("reports", exist_ok=True)

    with open("reports/final_report.txt", "w") as f:
        f.write(final_report)

    print("\nReport saved to: reports/final_report.txt")
    print("Execution logs saved to: logs/execution_log.json")


if __name__ == "__main__":
    main()