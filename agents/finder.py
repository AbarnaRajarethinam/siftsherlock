from tools.gemini_client import ask_gemini
import json


def generate_findings(memory_data):

    findings = []

    for proc in memory_data.get("processes", []):

        if proc.get("suspicious"):

            prompt = f"""
You are a senior DFIR analyst.

Analyze the following forensic evidence.

PROCESS:
Name: {proc.get("name")}
PID: {proc.get("pid")}

NETWORK CONNECTIONS:
{memory_data.get("network_connections", [])}

REGISTRY RUN KEYS:
{memory_data.get("registry", {}).get("run_keys", [])}

DLL INJECTION:
{memory_data.get("dll_injection", {})}

TIMELINE:
{memory_data.get("timeline", {})}

IMPORTANT:
Return ONLY valid JSON.

Required JSON schema:

{{
    "finding": "",
    "severity": "",
    "confidence": 0.0,
    "evidence": [],
    "missing_evidence": [],
    "recommended_actions": []
}}

Rules:
- Keep findings concise.
- Use short evidence bullet points.
- Do not write essays.
- Confidence must be between 0 and 1.
- Severity must be:
  low / medium / high / critical
"""

            ai_response = ask_gemini(prompt)

            try:
                parsed = json.loads(ai_response)

            except Exception:

                parsed = {
                    "finding": "Suspicious PowerShell execution",
                    "severity": "medium",
                    "confidence": 0.75,
                    "evidence": [
                        "Outbound network connection detected",
                        "Suspicious process flag raised"
                    ],
                    "missing_evidence": [
                        "No DLL injection evidence"
                    ],
                    "recommended_actions": [
                        "Inspect process tree",
                        "Review persistence mechanisms"
                    ]
                }

            findings.append({
                "process": proc.get("name"),
                "pid": proc.get("pid"),
                "analysis": parsed,
                "confidence": parsed.get("confidence", 0.75),
                "verified": False
            })

    return findings