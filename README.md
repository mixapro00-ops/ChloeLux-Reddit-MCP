# ChloeLux Reddit MCP (starter)

A **read-only prototype** for viewing public Reddit submissions through an MCP server. This is not a deployed service, does not authenticate to the user's account, and cannot publish posts, upload images, reply to comments, or manage private data.

## Status and permissions

**Reddit Data API approval is not yet granted.** Do not use this prototype to bypass Reddit's API access requirements. API usage is subject to Reddit's Developer Terms, Data API Terms, subreddit rules, and applicable rate limits. Approval is not guaranteed. This repository is a starter to describe the planned integration to Reddit.

## Setup (Windows PowerShell)

Install Python 3.11+, then run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

After API access is approved, fill `.env` with authorized credentials and a descriptive user agent. **Never commit `.env`**. Then run:

```powershell
.\.venv\Scripts\python.exe server.py
```

The server communicates using MCP **stdio**, not a public URL. It must be configured in an MCP-compatible local client to call its tools. This does **not** automatically connect it to ChatGPT; a compatible remote MCP deployment and supported connection flow may be required.

## Tools

- `recent_public_posts(username="MickoMrk", limit=5)`: read recent public submissions and basic engagement counts.

## Roadmap (subject to API approval)

- OAuth account authorization with least-privilege scopes
- Explicitly user-approved post creation and comment replies
- Image publishing, if supported by approved API access
- Secure remote MCP hosting for compatible clients

No automated unsolicited messaging, vote manipulation, spam, or bypass of community restrictions is planned. Promotional content will only be submitted where permitted.
