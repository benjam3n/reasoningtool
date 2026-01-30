---
name: "ais - Advocacy Infrastructure Setup"
description: "Set up foundational infrastructure for autonomous advocacy operations"
---

# Advocacy Infrastructure Setup

## Overview
Set up foundational infrastructure for autonomous advocacy operations

## Steps

### Step 1: Budget and resource assessment
Verify available resources and create setup plan:
1. Confirm budget meets minimum ($35)
2. Check for existing resources to integrate
3. Create prioritized setup timeline
4. Identify any constraints or special requirements

### Step 2: Domain registration and DNS setup
Register professional domain and configure DNS:
1. Choose domain name (e.g., [cause]policy.org, evidence[topic].org)
2. Register via Porkbun or Namecheap ($8-15)
3. Access DNS management panel
4. Prepare for mail provider DNS records

### Step 3: Email configuration with deliverability
Set up email hosting with all authentication records:
1. Create Zoho Mail account (free tier)
2. Add MX records (mx.zoho.com, priority 10)
3. Add SPF record (v=spf1 include:zoho.com ~all)
4. Generate and add DKIM record
5. Add DMARC record (v=DMARC1; p=none)
6. Create primary email addresses
7. Test deliverability with mail-tester.com

### Step 4: Phone and AI calling setup
Configure Twilio and Bland AI for phone outreach:
1. Create Twilio account
2. Add initial credit ($15-20)
3. Purchase phone number (professional area code)
4. Configure voicemail-to-email
5. Note Account SID and Auth Token
6. Create Bland AI account
7. Connect Twilio credentials to Bland AI
8. Add payment method
9. Create and test simple script
10. Make test call to personal phone

### Step 5: Database initialization
Create SQLite database with advocacy schema:
1. Initialize database file (data/advocacy.db)
2. Create policies table (tracking policy candidates)
3. Create targets table (legislators and staff)
4. Create campaigns table (outreach campaigns)
5. Create outreach table (individual contacts)
6. Create donations table (funding tracking)
7. Create learnings table (knowledge base)
8. Test CRUD operations on each table

### Step 6: Legislative monitoring setup
Configure monitoring for legislative activity:
1. Set up Congress.gov RSS feeds for relevant committees
2. Configure Google Alerts for policy keywords
3. Set up GovTrack API access if needed
4. Create RSS reader organization (Feedly or similar)
5. Test alert delivery with sample keywords
6. Document monitoring checklist for regular review

### Step 7: Integration testing and documentation
Verify all components work together:
1. Send test email and verify delivery
2. Make test AI phone call
3. Log test outreach in database
4. Verify monitoring alerts firing
5. Document all credentials securely
6. Create quick-reference setup guide
7. Test recovery procedures


## When to Use
- Starting a new advocacy project from scratch
- Setting up autonomous outreach capability for campaigns
- Need professional communication infrastructure for credibility
- Establishing legislative monitoring for policy tracking
- Building capacity for multi-channel advocacy campaigns
- Transitioning from informal to systematic advocacy operations

## Verification
- Email deliverability score meets 8+/10 threshold
- Test phone call completes with clear audio quality
- AI phone call via Bland AI executes successfully
- Database accepts and retrieves test records correctly
- Legislative monitoring alerts trigger for test keywords
- All credentials are documented securely
- Integration between components verified end-to-end

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.