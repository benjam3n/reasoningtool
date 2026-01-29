---
name: deployment
description: "Procedure for planning and executing reliable software deployments"
---

# Deployment

## Overview
Procedure for planning and executing reliable software deployments

## Steps

### Step 1: Pre-deployment preparation
Prepare for deployment before making any changes:
1. Verify artifact is tested and approved
2. Review changes being deployed (commits, migrations)
3. Check deployment prerequisites (dependencies, config)
4. Verify target environment is healthy
5. Confirm rollback procedure and verify it works
6. Notify stakeholders of deployment
7. Ensure team availability for monitoring

### Step 2: Create deployment checkpoint
Establish a known-good state to roll back to:
1. Record current running version
2. Backup relevant data if needed
3. Save current configuration state
4. Verify backup/checkpoint is complete
5. Document checkpoint location and restore procedure

### Step 3: Execute deployment
Deploy the artifact to target environment:
1. Initiate deployment (manual trigger or CI/CD)
2. Monitor deployment progress
3. Watch for errors or warnings
4. Wait for deployment to complete
5. Verify all instances updated
6. Execute database migrations if needed

### Step 4: Run smoke tests
Verify basic functionality immediately after deployment:
1. Run automated smoke test suite
2. Verify critical endpoints respond
3. Check database connectivity
4. Verify external integrations work
5. Confirm key user flows function
6. Check application logs for errors

### Step 5: Gradual traffic migration
Route traffic to new version progressively:
1. Start with small percentage (canary) or instant switch (blue-green)
2. Monitor error rates and latency
3. Check business metrics (conversions, etc.)
4. Gradually increase traffic to new version
5. Continue monitoring at each stage
6. Complete migration when confident

### Step 6: Post-deployment verification
Comprehensive verification that deployment is successful:
1. Run full integration test suite
2. Verify all features function correctly
3. Check performance metrics against baseline
4. Review error rates and alerts
5. Confirm monitoring and alerting is active
6. Verify rollback capability still works

### Step 7: Finalize or rollback
Complete deployment or execute rollback:
If successful:
  1. Mark deployment as complete
  2. Update deployment records
  3. Clean up old version (if blue-green)
  4. Notify stakeholders of success
  5. Archive deployment artifacts
If issues:
  1. Execute rollback procedure
  2. Verify rollback successful
  3. Notify stakeholders of rollback
  4. Document issues for investigation
  5. Plan remediation


## When to Use
- Setting up CI/CD pipeline for a project
- Planning deployment strategy for new application
- Preparing to release new features to production
- Improving existing deployment process
- Implementing deployment automation
- Planning rollback procedures
- Deploying to multiple environments
- Managing production releases

## Verification
- Deployment artifact matches what was tested
- All smoke tests pass
- Error rates within acceptable thresholds
- Performance metrics stable
- Rollback capability verified
- Stakeholders notified of outcome
- Deployment documented

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.