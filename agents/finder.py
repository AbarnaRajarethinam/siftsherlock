from tools.gemini_client import ask_gemini


def generate_findings(memory_data):
    findings = []

    for proc in memory_data.get("processes", []):
        if proc.get("suspicious"):

            prompt = f"""
Analyze this memory-forensics evidence.

Process:
- Name: {proc.get("name")}
- PID: {proc.get("pid")}
- Suspicious flag: {proc.get("suspicious")}

Available evidence:
- Processes: {memory_data.get("processes", [])}
- Network connections: {memory_data.get("network_connections", [])}
- Registry run keys: {memory_data.get("registry", {}).get("run_keys", [])}
- DLL injection indicators: {memory_data.get("dll_injection", {})}
- Timeline: {memory_data.get("timeline", {})}

Return:
1. Main finding
2. Supporting evidence
3. Missing evidence
4. Confidence from 0-100
5. Recommended next analysis step
"""

            ai_response = ask_gemini(prompt)

            findings.append({
                "claim": ai_response,
                "process": proc.get("name"),
                "pid": proc.get("pid"),
                "confidence": 0.85,
                "verified": False
            })

    return findings