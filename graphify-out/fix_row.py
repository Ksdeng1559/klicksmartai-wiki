#!/usr/bin/env python3
"""Fix Explorium task row at Tasks!A246 — full 7-column row via direct Sheets REST API."""
import json, urllib.request, urllib.parse

with open('/home/denni/.hermes/google_token.json') as f:
    t = json.load(f)

data = urllib.parse.urlencode({
    'client_id': t['client_id'], 'client_secret': t['client_secret'],
    'refresh_token': t['refresh_token'], 'grant_type': 'refresh_token'
}).encode()
req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data)
with urllib.request.urlopen(req) as r:
    creds = json.loads(r.read())

SHEET_ID = '1gZdR1MdNlCjjHiLE29dML4EeK-y6F56zuf9LcwtzTuQ'
row = [
    "FALSE",
    "Wire Explorium AgentSource MCP into Hermes (11 tools)",
    "P2",
    "",
    "Hermes",
    "Integration",
    "Needs EXPLORIUM_API_KEY in ~/.hermes/.env + mcp_servers.explorium → https://mcp.explorium.ai/mcp with Bearer auth. 11 tools mapped to progressive enrichment stages (wiki: raw/wiki-knowledge/concepts/progressive-enrichment-architecture.md + gtm-engineer-resources/01-data-enrichment/explorium-ai.md). Deferred by owner 2026-08-06."
]
url = f'https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/Tasks!A246:G246?valueInputOption=RAW'
body = json.dumps({'values': [row]})
req = urllib.request.Request(
    url, data=body.encode(),
    headers={'Authorization': f"Bearer {creds['access_token']}", 'Content-Type': 'application/json'},
    method='PUT'
)
with urllib.request.urlopen(req) as r:
    result = json.loads(r.read())
    print(json.dumps(result))
