---
name: "mcs - MCP Setup"
description: "Configure MCP servers to enable autonomous GOSM execution capabilities"
---

# MCP Setup

## Overview
Configure MCP servers to enable autonomous GOSM execution capabilities

## Steps

### Step 1: Assess requirements
Analyze which MCP servers are needed based on project requirements:

CORE CAPABILITIES:
- Gmail: Send/receive emails for stakeholder communication
- Google Drive: Store documents, letters, submissions
- Playwright: Web automation for research and form filling
- SQLite: Local database for data persistence

COMMUNICATION CAPABILITIES:
- Telnyx/Twilio: Phone calls and SMS
- Bland AI: AI-powered phone conversations

For each capability, determine:
1. Is it required for this project?
2. What authentication is needed?
3. What are the costs?
4. What are the security implications?

SAFETY: Document all capabilities requested and why.
Human must approve external service integrations.

### Step 2: Verify prerequisites
Check that required tools are available:

1. Node.js and npm:
   - Required for MCP server packages
   - Check: node --version, npm --version
   - Install if missing

2. Claude Code CLI:
   - Required for MCP integration
   - Check: claude --version

3. Project directory:
   - Must exist and be writable
   - Check: ls -la {project_path}

4. Network access:
   - Required for OAuth and API calls
   - Check: connectivity to googleapis.com

SAFETY: Never install packages without user awareness.
Document all prerequisite checks.

### Step 3: Create MCP configuration
Generate .mcp.json file for the project:

Base structure:
```json
{
  "mcpServers": {
    // Servers will be added based on requirements
  }
}
```

For each required capability, add server config:

GMAIL:
```json
"gmail": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-gmail"],
  "env": {
    "GMAIL_OAUTH_PATH": "${HOME}/.config/gmail-mcp/credentials.json"
  }
}
```

GOOGLE DRIVE:
```json
"google-drive": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-gdrive"]
}
```

PLAYWRIGHT:
```json
"playwright": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-playwright"]
}
```

SQLITE:
```json
"sqlite": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-sqlite", "{database_path}"]
}
```

SAFETY: Configuration file should not contain secrets.
Use environment variables for sensitive paths.

### Step 4: Configure Google OAuth
Guide user through Google OAuth setup (if Gmail/Drive needed):

1. Go to Google Cloud Console:
   URL: https://console.cloud.google.com/

2. Create or select project:
   - Create new project for isolation
   - Or use existing project

3. Enable required APIs:
   - Gmail API: APIs & Services > Library > Gmail API > Enable
   - Drive API: APIs & Services > Library > Google Drive API > Enable

4. Configure OAuth consent screen:
   - User type: External (or Internal if Workspace)
   - App name: "GOSM Autonomous Agent"
   - Scopes: gmail.send, gmail.readonly, drive

5. Create OAuth credentials:
   - APIs & Services > Credentials > Create Credentials
   - Select "OAuth client ID"
   - Application type: "Desktop application"
   - Download JSON file

6. Save credentials:
   - Create directory: mkdir -p ~/.config/gmail-mcp/
   - Save as: ~/.config/gmail-mcp/credentials.json

SAFETY: Credentials file contains sensitive data.
Never share or expose credentials.json.
Store in secure location with restricted permissions.

### Step 5: Authenticate MCP servers
Complete authentication for each configured server:

GMAIL/DRIVE (OAuth flow):
1. In Claude Code, run: /mcp
2. Select gmail or google-drive server
3. Follow OAuth prompts in browser
4. Authorize requested permissions
5. Return to Claude Code

PLAYWRIGHT (no auth needed):
- Works immediately after configuration
- Runs headless browser locally

SQLITE (no auth needed):
- Works immediately after configuration
- Database created on first use

PHONE SERVICES (API key):
- Telnyx: Get API key from dashboard
- Set environment variable: TELNYX_API_KEY
- Or configure in wrapper scripts

SAFETY: OAuth tokens are stored by the MCP server.
Tokens can be revoked from Google account settings.
API keys should be stored in environment variables, not files.

### Step 6: Create database schema
If SQLite is configured, create the schema for autonomous operations:

TABLES:

crossings (for Tunnel Vision example):
- id TEXT PRIMARY KEY
- state, city, county, road_name TEXT
- railroad TEXT
- fatalities_10yr, injuries_10yr INTEGER
- adt, trains_per_day INTEGER
- score REAL
- status TEXT
- created_at, updated_at TIMESTAMP

stakeholders:
- id INTEGER PRIMARY KEY
- crossing_id TEXT (foreign key)
- name, organization, role TEXT
- email, phone TEXT
- status TEXT
- last_contact TIMESTAMP
- next_action TEXT
- next_action_date DATE
- notes TEXT

communications:
- id INTEGER PRIMARY KEY
- stakeholder_id INTEGER (foreign key)
- type TEXT (email/phone/sms)
- direction TEXT (inbound/outbound)
- timestamp TIMESTAMP
- subject, content TEXT
- classification TEXT
- processed BOOLEAN

letters:
- id INTEGER PRIMARY KEY
- stakeholder_id INTEGER (foreign key)
- status TEXT
- requested_date, received_date DATE
- file_path TEXT

automation_state:
- key TEXT PRIMARY KEY
- value TEXT
- updated_at TIMESTAMP

SAFETY: Database should be in project directory only.
Never create databases in system directories.
Backup database before schema changes.

### Step 7: Verify installation
Test that all configured MCP servers are working:

1. List configured servers:
   Command: claude mcp list
   Expected: See all servers from .mcp.json

2. Test each server:

   GMAIL:
   - Send test email to self
   - Check inbox for test email
   - Verify send and read work

   GOOGLE DRIVE:
   - Create test document
   - Read document back
   - Delete test document

   PLAYWRIGHT:
   - Navigate to test URL
   - Extract page content
   - Verify browser automation works

   SQLITE:
   - Insert test record
   - Query test record
   - Delete test record

3. Document any failures with error messages.

SAFETY: Test with non-destructive operations only.
Use test data, not production data.
Verify cleanup of test artifacts.

### Step 8: Configure wrapper scripts
For services without MCP servers, create wrapper scripts:

scripts/send_email.py:
- Send email via Gmail API
- Parameters: to, subject, body, attachments

scripts/check_email.py:
- Check inbox for new messages
- Filter by sender, subject, date
- Return structured response

scripts/send_sms.py:
- Send SMS via Twilio/Telnyx
- Parameters: to, message

scripts/ai_phone_call.py:
- Initiate Bland AI call
- Parameters: to, script, context

scripts/scrape_fra.py:
- Scrape FRA safety database
- Return crossing data

Each script should:
- Read credentials from environment
- Log all actions
- Return structured JSON output
- Handle errors gracefully

SAFETY: Scripts should validate inputs.
Rate limiting should be implemented.
All actions should be logged.

### Step 9: Document setup
Create documentation for the MCP setup:

1. SETUP_COMPLETE.md:
   - What capabilities are configured
   - How to use each capability
   - Common commands and examples

2. TROUBLESHOOTING.md:
   - Common issues and solutions
   - How to re-authenticate
   - How to check server status

3. SECURITY.md:
   - What credentials are stored where
   - How to revoke access
   - Security best practices

Store in project's docs/ directory.

SAFETY: Documentation should not contain credentials.
Reference environment variables and secure storage.


## When to Use
- Setting up new autonomous project requiring external integrations
- Enabling email send/receive for stakeholder outreach
- Configuring web automation for research tasks
- Setting up persistent data storage for multi-session projects
- Adding phone/SMS capabilities for communication
- Expanding capabilities of existing autonomous setup
- Migrating project to new environment
- Troubleshooting broken MCP connections

## Verification
- All requested capabilities are configured
- Authentication is complete for all servers
- Test operations succeed for each server
- Credentials are stored securely
- Documentation is complete
- Troubleshooting guide covers common issues
- Human has reviewed and approved setup

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.