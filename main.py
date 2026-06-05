import json

from agents.planner import create_plan
from agents.finder import generate_findings
from agents.verifier import verify_findings
from agents.self_corrector import self_correct
from agents.reporter import generate_report

with open("data/sample_memory_output.json") as f:
    memory_data = json.load(f)

print("\n=== INVESTIGATION PLAN ===")
plan = create_plan(memory_data)
print(plan)

print("\n=== GENERATING FINDINGS ===")
findings = generate_findings(memory_data)
print(findings)

print("\n=== VERIFYING FINDINGS ===")
verified = verify_findings(findings, memory_data)
print(verified)

print("\n=== SELF CORRECTION ===")
corrected = self_correct(verified)
print(corrected)

print(generate_report(corrected))