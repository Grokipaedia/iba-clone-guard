# iba-clone-guard

**Clone websites safely. Human intent required.**

New Claude Code tools can now clone any website perfectly in one prompt — fonts, colors, layout, everything.

This tool adds real cryptographic governance.

Wrap any cloning request with a signed **IBA Intent Certificate** so the clone can only be used under **your exact approved rules**.

## Features
- Requires IBA-signed intent before any cloning action
- Enforces scope (research only, no commercial use, no phishing, etc.)
- Optional safe hollowing / blocking of sensitive elements
- Works with any Claude Code or MCP-based website cloner

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-clone-guard.git
cd iba-clone-guard
pip install -r requirements.txt
python guard.py "https://example.com" --hollow medium
