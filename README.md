# iba-clone-guard

**Clone websites safely. Human intent required.**

New Claude Code tools can now clone any website perfectly in one prompt — exact fonts, colors, layout, everything.

This tool adds real cryptographic governance using **Intent-Based Authorization (IBA)**.

Wrap any cloning request with a signed IBA Intent Certificate so the clone can only be used under your exact approved rules.

## Patent & Filings
- **Patent Pending**: GB2603013.0 (filed 5 Feb 2026, PCT route open — 150+ countries)
- **NIST Docket**: NIST-2025-0035 (13 IBA filings)
- **NCCoE Filings**: Multiple submissions on AI agent authorization

## How It Works

1. Use any tool (Claude Code + Chrome MCP, Playwright, etc.) to clone the website
2. Run `iba-clone-guard` on the cloned content
3. The output is a protected file with an embedded IBA certificate

## Features
- Requires IBA-signed intent before any cloning action
- Enforces scope (research only, no commercial use, no phishing, no impersonation)
- Optional safe hollowing (light / medium / heavy)
- Works with any cloned website content

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-clone-guard.git
cd iba-clone-guard
pip install -r requirements.txt
python guard.py "path/to/your-cloned-site.md" --hollow medium
