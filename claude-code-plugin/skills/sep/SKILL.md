---
name: "sep - Security Practices"
description: "Procedure for implementing security throughout the software development lifecycle"
---

# Security Practices

## Overview
Procedure for implementing security throughout the software development lifecycle

## Steps

### Step 1: Understand security context
Assess the security landscape for your system:
1. Identify data sensitivity (PII, financial, health)
2. Understand compliance requirements
3. Identify threat actors and motivations
4. Map attack surface (entry points)
5. Review existing security controls
6. Understand risk tolerance

### Step 2: Perform threat modeling
Systematically identify and analyze threats:
1. Decompose system into components
2. Identify trust boundaries
3. For each component, identify threats using STRIDE:
   - Spoofing (identity)
   - Tampering (data)
   - Repudiation (deniability)
   - Information disclosure
   - Denial of service
   - Elevation of privilege
4. Prioritize threats by risk
5. Identify mitigations for each threat

### Step 3: Design security architecture
Design security controls for the system:
1. Design authentication mechanism
2. Design authorization model
3. Plan data protection (encryption, masking)
4. Design secure communication channels
5. Plan logging and monitoring
6. Design for defense in depth

### Step 4: Implement secure coding practices
Apply security during development:
1. Validate all input
2. Encode all output appropriately
3. Use parameterized queries
4. Implement proper error handling
5. Manage secrets securely
6. Use security-focused code review
7. Follow OWASP guidelines

### Step 5: Perform security testing
Verify security through testing:
1. Run static analysis (SAST)
2. Run dependency vulnerability scanning
3. Perform dynamic testing (DAST)
4. Test authentication and authorization
5. Test for OWASP Top 10 vulnerabilities
6. Consider penetration testing

### Step 6: Configure security monitoring
Set up detection and response capabilities:
1. Configure security logging
2. Set up alerting for suspicious activity
3. Implement intrusion detection
4. Monitor for vulnerability announcements
5. Establish incident response process
6. Plan regular security reviews

### Step 7: Document and maintain
Document security for ongoing maintenance:
1. Document security architecture
2. Document threat model
3. Create security runbooks
4. Establish security update process
5. Plan regular security assessments
6. Train team on security practices


## When to Use
- Designing security architecture for new system
- Reviewing code for security vulnerabilities
- Implementing authentication and authorization
- Handling sensitive data (PII, credentials, payments)
- Preparing for security audit
- Responding to security incident
- Training developers on secure coding
- Establishing security standards for a team

## Verification
- Threat model covers all significant risks
- Authentication and authorization are robust
- OWASP Top 10 vulnerabilities addressed
- Sensitive data is properly protected
- Security testing completed
- Monitoring and alerting configured
- Incident response plan exists

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.