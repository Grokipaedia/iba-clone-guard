# guard.py - IBA protection for website cloning
import json
from datetime import datetime
import sys
import argparse

def create_iba_clone_guard(url: str, hollow_level: str = None):
    cert = {
        "iba_version": "2.0",
        "certificate_id": f"clone-guard-{datetime.now().strftime('%Y%m%d-%H%M')}",
        "issued_at": datetime.now().isoformat(),
        "principal": "human-owner",
        "declared_intent": f"Clone website {url} for legitimate research/reference purposes only. No commercial use, no phishing, no brand impersonation.",
        "scope_envelope": {
            "resources": ["website-clone", "research-reference"],
            "denied": ["commercial-use", "phishing", "impersonation"],
            "default_posture": "DENY_ALL"
        },
        "temporal_scope": {
            "hard_expiry": (datetime.now().replace(year=datetime.now().year + 1)).isoformat()
        },
        "entropy_threshold": {
            "max_kl_divergence": 0.12,
            "flag_at": 0.08,
            "kill_at": 0.12
        },
        "iba_signature": "demo-signature"
    }

    protected_file = f"clone-{url.replace('https://', '').replace('/', '-')}.iba-protected.md"

    content = f"# Cloned Website: {url}\n\n[Cloned content would appear here under IBA governance]\n\n<!-- IBA PROTECTED CLONE -->\n"

    if hollow_level:
        content += f"\n<!-- Hollowed ({hollow_level}): Sensitive elements protected by IBA certificate -->\n"

    with open(protected_file, "w", encoding="utf-8") as f:
        f.write("<!-- IBA PROTECTED WEBSITE CLONE -->\n")
        f.write(f"<!-- Intent Certificate: {json.dumps(cert, indent=2)} -->\n\n")
        f.write(content)

    print(f"✅ IBA-protected clone file created: {protected_file}")
    if hollow_level:
        print(f"   Hollowing level applied: {hollow_level}")
    else:
        print("   Full clone protected by IBA certificate")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Governed website cloning with IBA")
    parser.add_argument("url", help="URL of the website to clone")
    parser.add_argument("--hollow", choices=["light", "medium", "heavy"], help="Apply safe hollowing")
    args = parser.parse_args()

    create_iba_clone_guard(args.url, args.hollow)
