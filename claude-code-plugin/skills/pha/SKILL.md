---
name: pha
description: "Acquire and configure phone numbers for autonomous system operations"
---

# Phone Acquisition

## Overview
Acquire and configure phone numbers for autonomous system operations

## Steps

### Step 1: Assess requirements and select provider
Evaluate needs to determine best phone solution:

1. Use case assessment:
   - SMS verification only: Cheapest VoIP option
   - Voice calls needed: Reliable VoIP with voice
   - AI phone integration: Twilio or Telnyx (API required)
   - Services block VoIP: Physical SIM required

2. Budget check:
   - $0: TextNow or Google Voice (limited)
   - $1-5/month: Twilio or Telnyx
   - $10-15/month: Physical SIM (Mint, Tello)

3. VoIP acceptability:
   - If target services block VoIP, must use physical SIM
   - Test VoIP first, escalate to SIM if blocked

4. AI calling needs:
   - If using Bland AI: Twilio strongly recommended
   - API access essential for AI integration

Select provider based on assessment.

### Step 2: Create provider account
Set up account with selected provider:

For Twilio (recommended for automation):
1. Go to twilio.com/try-twilio
2. Create account with email
3. Verify email address
4. Complete identity verification (required for production)
5. Note Account SID and Auth Token

For Telnyx:
1. Go to telnyx.com
2. Create account
3. Complete verification
4. Add payment method

For TextNow (free):
1. Download TextNow app
2. Create account
3. Get assigned number

For Google Voice:
1. Go to voice.google.com
2. Sign in with Google account
3. Link existing phone for verification
4. Select available number

Store all credentials securely.

### Step 3: Add funds and purchase number
Fund account and acquire phone number:

For Twilio/Telnyx:
1. Add initial funds ($20 recommended minimum)
2. Go to phone numbers section
3. Search for available numbers
4. Select number type:
   - Local: Standard area code (~$1/month)
   - Toll-free: 800/888 numbers (~$2/month)
5. Purchase selected number
6. Note the phone number

For free services:
- TextNow: Number assigned automatically
- Google Voice: Select from available numbers

Number selection tips:
- Local numbers appear more personal
- Toll-free numbers appear more business-like
- Memorable numbers cost more but may be worth it

### Step 4: Configure for receiving
Set up the number to receive calls and SMS:

For Twilio/Telnyx (webhook-based):
1. Configure SMS webhook:
   - URL to receive incoming SMS
   - Can use Zapier, Make.com, or custom server
2. Configure voice webhook:
   - URL for incoming calls
   - Or set up voicemail with transcription
3. Set up email notifications (optional):
   - Forward SMS to email
   - Voicemail transcription to email

For simple forwarding:
1. Forward SMS to email via Zapier:
   - Trigger: New SMS to Twilio number
   - Action: Send email with message content
2. Forward calls to voicemail:
   - Configure voicemail greeting
   - Enable transcription and email

For direct checking:
- Use Twilio console to view messages
- Check messages via API

### Step 5: Configure AI phone integration (if needed)
Set up for AI phone calling with Bland AI or similar:

Prerequisites:
- Twilio or Telnyx account with phone number
- Bland AI account (bland.ai)

Integration steps:
1. Create Bland AI account:
   - Go to bland.ai
   - Sign up and verify email
   - Add payment method

2. Connect Twilio to Bland AI:
   - In Bland AI, go to settings/integrations
   - Add Twilio credentials (SID and Auth Token)
   - Select your Twilio phone number as caller ID

3. Create test pathway:
   - Define simple conversation script
   - Set up call objective
   - Configure response handling

4. Test integration:
   - Make test call to your own phone
   - Verify AI agent works correctly
   - Check call recording and transcription

### Step 6: Test all capabilities
Verify phone number works for all intended purposes:

SMS testing:
1. Send SMS from another phone to your number
2. Verify message received and accessible
3. Send SMS from your number to another phone
4. Verify message delivered

Voice testing:
1. Call your number from another phone
2. Verify call handling (voicemail, forwarding, etc.)
3. If AI calling configured, make outbound AI call
4. Verify call quality and functionality

Verification code testing:
1. Use number for a test signup
2. Verify code arrives promptly
3. Note any services that block the number

Document any limitations discovered.

### Step 7: Document and schedule maintenance
Create documentation and maintenance plan:

Document:
- Phone number
- Provider and account credentials
- API credentials (SID, Auth Token)
- Webhook URLs if configured
- AI service credentials if connected
- Monthly cost and billing date

Maintenance tasks:
Daily:
- Check for incoming SMS/voicemails
- Respond to callbacks within 24 hours

Monthly:
- Review usage and costs
- Top up balance if needed
- Verify number still active

Annual:
- Evaluate if number still needed
- Consider number changes if compromised
- Update API credentials if rotated

Set up balance alerts:
- Configure low balance notification
- Ensure auto-recharge if available


## When to Use
- Need to receive SMS verification codes for account signups
- Need phone number for two-factor authentication
- Need to receive callbacks from stakeholders or services
- Want to enable AI phone calling (Bland AI integration)
- Need professional phone presence for business communications
- Current phone number is unavailable or inappropriate for project
- Separating project communications from personal phone

## Verification
- Phone number acquired and active
- SMS sending and receiving verified
- Voice calls handled correctly
- AI phone integration working (if configured)
- Credentials documented securely
- Maintenance schedule established
- Cost tracking in place
- Balance monitoring configured

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.