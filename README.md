# iba-clone-guard

**Clone websites safely. Human intent required.**

New Claude Code tools can now clone any website perfectly in one prompt — exact fonts, colors, layout, everything.

This tool adds real cryptographic governance using **Intent-Based Authorization (IBA)**.

Wrap any cloning request with a signed IBA Intent Certificate so the clone can only be used under your exact approved rules.

## Patent & Filings
- **Patent Pending**: GB2603013.0 (filed 5 Feb 2026, PCT route open — 150+ countries)
- **NIST Docket**: NIST-2025-0035 (13 IBA filings)
- **NCCoE Filings**: Multiple submissions on AI agent authorization

## Features
- Requires IBA-signed intent before any cloning action
- Enforces scope (research only, no commercial use, no phishing, no impersonation)
- Optional safe hollowing / blocking of sensitive elements
- Works with any Claude Code or MCP-based website cloner

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-clone-guard.git
cd iba-clone-guard
pip install -r requirements.txt
python guard.py "https://example.com" --hollow medium
