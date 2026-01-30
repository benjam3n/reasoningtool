---
name: "ts - Testing Strategy"
description: "Procedure for designing and implementing effective software testing strategies"
---

# Testing Strategy

## Overview
Procedure for designing and implementing effective software testing strategies

## Steps

### Step 1: Assess current state
Understand the project's testing starting point:
1. Inventory existing tests by type and coverage
2. Measure current test suite runtime
3. Identify flaky or problematic tests
4. Review historical bug sources
5. Assess team testing skills and experience
6. Document testing infrastructure and tools

### Step 2: Define testing goals
Establish what testing needs to achieve:
1. Identify critical business functionality
2. Determine acceptable risk levels
3. Set coverage and quality targets
4. Define test runtime budgets
5. Establish testing requirements for CI/CD
6. Consider compliance or regulatory needs

### Step 3: Design test pyramid distribution
Determine the right balance of test types:
1. Start with standard pyramid (70/20/10)
2. Adjust based on project type:
   - API-heavy: More integration tests
   - UI-heavy: More E2E but keep focused
   - Library: Mostly unit tests
3. Identify what to test at each level
4. Map critical paths to test coverage
5. Plan for test data management

### Step 4: Select testing tools and frameworks
Choose appropriate testing infrastructure:
1. Select test runner and framework
2. Choose assertion library
3. Select mocking/stubbing tools
4. Choose coverage measurement tool
5. Select E2E testing framework if needed
6. Plan test data management approach
7. Consider CI/CD integration requirements

### Step 5: Create test implementation plan
Plan how to implement the testing strategy:
1. Prioritize what to test first (high-risk, high-value)
2. Create phased implementation timeline
3. Define patterns and conventions for tests
4. Plan for test maintenance
5. Set up CI/CD test stages
6. Define when to run which tests

### Step 6: Write initial tests
Begin implementing tests following the strategy:
1. Set up testing infrastructure
2. Write example tests demonstrating patterns
3. Start with highest-priority tests
4. Establish test data fixtures
5. Create helpers and utilities
6. Document testing patterns for team

### Step 7: Integrate and iterate
Embed testing into development workflow:
1. Configure CI/CD pipeline stages
2. Set up coverage reporting
3. Establish test review practices
4. Train team on testing approach
5. Monitor test suite health
6. Iterate based on feedback


## When to Use
- Starting a new project and defining test approach
- Existing project needs improved test coverage
- Team debating which types of tests to write
- Current tests are slow, flaky, or not catching bugs
- Implementing Test-Driven Development (TDD)
- Defining quality gates for CI/CD pipelines
- Establishing testing standards for a team
- Deciding how to test a new feature

## Verification
- Testing strategy covers critical functionality
- Test pyramid is appropriately balanced
- Tests run fast enough for development workflow
- CI/CD pipeline includes appropriate test stages
- Team understands and follows testing patterns
- Coverage targets are met for new code
- Tests catch bugs before production

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.