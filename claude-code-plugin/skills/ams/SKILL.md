---
name: ams
description: "Collection of strategies for bypassing or working around API limitations, including rate limits, IP blocks, and access restrictions."
---

# API Middleman Strategies

## Overview
Collection of strategies for bypassing or working around API limitations, including rate limits, IP blocks, and access restrictions.

## Steps

### Step 1: Diagnose the limitation
Identify what's actually blocking access:

RATE LIMITED:
- HTTP 429 responses
- "Too many requests" errors
- Requests throttled or slowed

IP BLOCKED:
- HTTP 403 from specific IPs
- Works from browser but not script
- Works from home but not cloud

AUTHENTICATION REQUIRED:
- HTTP 401/403 requiring login
- Content only visible when logged in
- Requires API key you don't have

COST PROHIBITIVE:
- API works but too expensive at scale
- Would exceed budget with volume needed

FUNCTIONALITY MISSING:
- API doesn't expose needed data
- Data available on website but not API

### Step 2: Check official options first
Before workarounds, verify official options exhausted:

1. Rate limit options:
   - Can you request a higher limit?
   - Can you use authenticated requests for higher limits?
   - Is there a paid tier with higher limits?

2. IP block options:
   - Is there an official way to whitelist?
   - Are you violating ToS that triggered the block?
   - Can you fix the violation?

3. Authentication options:
   - Is there an official API key program?
   - Is there a developer/researcher program?
   - Can you use OAuth properly?

4. Cost options:
   - Are there volume discounts?
   - Is there an academic/nonprofit rate?
   - Can you reduce scope to fit budget?

Document what official options were considered and why not viable.

### Step 3: Select primary strategy
Choose the best workaround based on failure type:

FOR YOUTUBE TRANSCRIPTS:
1. Browser Cookie Passthrough (yt-dlp)
   - Reliability: HIGH (when working)
   - Setup: 5 minutes
   - Use when: IP blocked or rate limited
   - Note: May be blocked during high-volume periods

2. Alternative Transcript Services
   - Reliability: MEDIUM
   - Cost: Usually free
   - Use when: Cookie method doesn't work

3. Residential Proxy Rotation
   - Reliability: HIGH
   - Cost: $20-100/month
   - Use when: High volume needed

4. Local Whisper Transcription
   - Reliability: HIGH
   - Cost: Compute only
   - Use when: All API methods fail

5. Manual Extraction
   - Reliability: HIGHEST
   - Cost: Time (5 min/video)
   - Use when: Low volume, all else fails

FOR LLM APIS:
1. Local Models (Ollama)
   - Reliability: HIGH
   - Cost: Compute only
   - Use when: Cost is primary issue

2. API Aggregators (OpenRouter)
   - Reliability: HIGH
   - Cost: Variable
   - Use when: Need redundancy across providers

3. Model Fallback Chain
   - Reliability: HIGH
   - Use when: Single provider unreliable

FOR GENERAL WEB:
1. Browser Automation (Playwright)
   - Reliability: HIGH
   - Use when: Anti-bot measures active

2. Scraping APIs (ScrapingBee)
   - Reliability: HIGH
   - Cost: Paid
   - Use when: Complex anti-bot

### Step 4: Build fallback chain
Create ordered list of fallback strategies:

Example for YouTube transcripts:
1. YouTube Transcript API (official)
2. yt-dlp with browser cookies
3. Alternative services (youtubetranscript.com)
4. Residential proxy + API
5. Local Whisper transcription
6. Manual extraction

Example for LLM APIs:
1. Primary provider (Anthropic Claude)
2. Secondary provider (OpenAI)
3. API aggregator (OpenRouter)
4. Local model (Ollama)

For each fallback:
- Define trigger condition (when to fall back)
- Define retry logic (how many attempts)
- Define escalation path (when to give up)

### Step 5: Implement primary strategy
Set up the chosen strategy. See YOUTUBE_TRANSCRIPT_MIDDLEMEN
and LLM_API_STRATEGIES sections below for specific implementations.

Key implementation patterns:
- Always add caching layer
- Always implement exponential backoff
- Always have manual fallback

### Step 6: Add reliability layers
Add infrastructure for reliable operation:

1. EXPONENTIAL BACKOFF
   - Wait progressively longer after failures
   - Add jitter to prevent thundering herd

2. CACHING LAYER
   - Cache responses with TTL
   - Avoid repeat requests for same data

3. REQUEST SPREADING
   - Track requests in sliding window
   - Wait when approaching limit

See RATE_LIMIT_STRATEGIES section below for code templates.

### Step 7: Test full pipeline
Verify the complete solution works:

1. Test happy path:
   - Normal request succeeds
   - Response is correct format
   - Performance is acceptable

2. Test failure handling:
   - Simulate rate limit (does backoff work?)
   - Simulate timeout (does retry work?)
   - Simulate primary failure (does fallback work?)

3. Test at scale:
   - Process 10-100 items
   - Monitor error rate
   - Check cache hit rate
   - Verify cost is within budget


## When to Use
- When direct API access is blocked or rate-limited
- When API costs are prohibitively high
- When building extraction pipelines that need reliability
- When IP addresses are flagged or blocked
- When scaling up data collection
- When official API lacks needed functionality
- When setting up automation that must handle failures

## Verification
- Limitation is correctly diagnosed
- Official options were considered first
- Strategy matches the specific failure type
- Fallback chain covers all likely failures
- Implementation includes reliability layers
- Pipeline tested at expected scale

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.