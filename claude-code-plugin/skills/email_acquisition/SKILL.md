---
name: email_acquisition
description: "Acquire and configure email addresses for autonomous system operations"
---

# Email Acquisition

## Overview
Acquire and configure email addresses for autonomous system operations

## Steps

### Step 1: Assess requirements and select approach
Evaluate project needs to determine email approach:

1. Volume assessment:
   - Low (<50/day): Free tier sufficient
   - Medium (50-500): Free with custom domain
   - High (>500): Paid service required

2. Budget check:
   - $0: Gmail/Outlook/ProtonMail free
   - $10-15: Custom domain + Zoho free
   - $50+: Google Workspace or Fastmail

3. Professional requirements:
   - Internal only: Free email OK
   - External stakeholders: Custom domain preferred
   - Business critical: Paid service recommended

4. Privacy requirements:
   - Standard: Any provider
   - Enhanced: ProtonMail or Fastmail
   - Maximum: ProtonMail with anonymous signup

Select tier and specific provider based on assessment.

### Step 2: Register domain (if needed)
If requires_domain is true, register a domain:

1. Choose domain name:
   - Professional and memorable
   - Related to project purpose
   - .com preferred, .io/.co acceptable
   - Avoid hyphens and numbers

2. Select registrar (cost comparison):
   - Porkbun: ~$9/year for .com (cheapest)
   - Namecheap: ~$10/year
   - Cloudflare: ~$9/year (at cost pricing)

3. Registration process:
   - Search for domain availability
   - Add to cart
   - Complete purchase
   - Verify domain ownership via email

4. Enable privacy protection:
   - WHOIS privacy (usually free)
   - Protects personal information

### Step 3: Set up email service
Configure email service for the domain:

For Zoho Free (recommended for custom domain):
1. Go to zoho.com/mail
2. Sign up with "Add Domain" option
3. Verify domain ownership via DNS TXT record
4. Create email addresses as needed

For Gmail (free, no custom domain):
1. Go to accounts.google.com
2. Create new Google account
3. Complete phone verification if required
4. Configure account settings

For ImprovMX (forwarding only, free):
1. Go to improvmx.com
2. Add domain
3. Set up forwarding to existing email
4. Useful for receiving only

Create standard addresses:
- contact@[domain] - general inquiries
- info@[domain] - information requests
- [project]@[domain] - project-specific

### Step 4: Configure DNS for deliverability
Set up DNS records to ensure emails are delivered (not marked as spam):

Required records:
1. MX Records (Mail Exchange):
   - Points to email service's mail servers
   - Example: mx.zoho.com with priority 10

2. SPF Record (Sender Policy Framework):
   - TXT record authorizing mail servers
   - Example: v=spf1 include:zoho.com ~all

3. DKIM Record (DomainKeys Identified Mail):
   - TXT record for email signing
   - Get value from email provider
   - Proves emails are from your domain

4. DMARC Record (Domain-based Message Authentication):
   - TXT record defining policy
   - Example: v=DMARC1; p=none; rua=mailto:dmarc@[domain]

Configuration location: Domain registrar's DNS settings

Propagation: Wait 15 minutes to 48 hours for DNS propagation

### Step 5: Test deliverability
Verify emails will be delivered properly:

1. Send test emails to major providers:
   - Gmail (personal account)
   - Outlook/Hotmail
   - Yahoo (if available)

2. Check each test:
   - Did email arrive in inbox (not spam)?
   - Is sender name/email displayed correctly?
   - Do links and formatting work?

3. Use mail-tester.com:
   - Send email to their test address
   - Get deliverability score
   - Target: 8+ out of 10
   - Review any issues flagged

4. Check authentication headers:
   - View email source in recipient inbox
   - Verify SPF=pass, DKIM=pass, DMARC=pass

If score < 8, troubleshoot:
- Verify DNS records are correct
- Check for blacklist status
- Review email content for spam triggers

### Step 6: Configure automation access (optional)
Set up programmatic access if needed for automation:

IMAP/SMTP access (for scripts):
1. Enable IMAP in email settings
2. Note server addresses:
   - IMAP: imapro.zoho.com:993 (SSL)
   - SMTP: smtppro.zoho.com:465 (SSL)
3. Generate app-specific password if 2FA enabled

API access (provider-specific):
- Gmail: Enable Gmail API, create OAuth credentials
- Zoho: Enable API access in mail settings

Integration platforms:
- Zapier: Connect email for automation
- Make.com: Alternative integration platform
- n8n: Self-hosted option

Document credentials securely for later use.

### Step 7: Document and schedule maintenance
Create maintenance plan for ongoing email health:

Daily tasks:
- Check inbox for responses
- Respond within 24 hours to maintain reputation

Weekly tasks:
- Review spam folder for false positives
- Check deliverability if sending volume

Monthly tasks:
- Verify DNS records still correct
- Check account standing
- Review any bounced emails

Annual tasks:
- Renew domain before expiration
- Review email strategy
- Update passwords

Document all credentials and settings:
- Domain registrar login
- Email service login
- DNS record values
- API credentials (if configured)


## When to Use
- Starting a new autonomous project requiring professional correspondence
- Need to send outreach emails to stakeholders
- Need to receive responses and documents from external parties
- Account registration for services requires email verification
- Need professional appearance for business communications
- Current email is compromised, suspended, or unreliable
- Separating project communications from other email

## Verification
- Email addresses created and accessible
- Test emails arrive in inbox (not spam)
- Deliverability score is 8+ on mail-tester.com
- All DNS records configured correctly (SPF, DKIM, DMARC)
- Credentials documented securely
- Maintenance schedule established
- Domain renewal date tracked
- Cost is within budget

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.