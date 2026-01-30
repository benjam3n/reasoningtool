---
name: "apid - API Design"
description: "Procedure for designing, implementing, and documenting effective APIs"
---

# API Design

## Overview
Procedure for designing, implementing, and documenting effective APIs

## Steps

### Step 1: Understand requirements
Gather the context for API design:
1. Identify use cases and user stories
2. Understand who will consume the API
3. List data entities and relationships
4. Identify operations needed on each entity
5. Understand non-functional requirements
6. Review any existing APIs for consistency

### Step 2: Design resource model
Define the API's resource structure:
1. Identify resources from entities
2. Name resources (plural, lowercase, nouns)
3. Define resource relationships
4. Map operations to HTTP methods
5. Design URL structure
6. Identify sub-resources

### Step 3: Design request/response schemas
Define what data flows in and out:
1. Define resource schemas
2. Design request bodies for create/update
3. Design response bodies for each operation
4. Plan pagination, filtering, sorting
5. Design error response format
6. Define common headers

### Step 4: Design authentication and authorization
Define how security works:
1. Choose authentication method
2. Design authorization model
3. Define which endpoints need auth
4. Plan rate limiting
5. Design API keys or tokens
6. Consider security headers

### Step 5: Create API specification
Document the complete API formally:
1. Write OpenAPI specification
2. Document each endpoint completely
3. Include examples for all operations
4. Document error codes and responses
5. Specify authentication requirements
6. Review specification for completeness

### Step 6: Write documentation
Create consumer-facing documentation:
1. Write getting started guide
2. Create authentication guide
3. Generate reference from OpenAPI
4. Write guides for common use cases
5. Include code examples in multiple languages
6. Set up interactive API explorer

### Step 7: Plan versioning and evolution
Prepare for API changes over time:
1. Choose versioning strategy
2. Define what constitutes breaking change
3. Plan deprecation process
4. Design for forward compatibility
5. Plan changelog maintenance
6. Document migration paths


## When to Use
- Designing a new API for internal or external use
- Adding endpoints to existing API
- Reviewing API design before implementation
- Planning API versioning strategy
- Creating API documentation
- Defining error handling patterns
- Establishing API standards for a team

## Verification
- API is RESTful and follows conventions
- All endpoints documented
- Error handling is comprehensive
- Authentication and authorization defined
- Documentation enables self-service
- Versioning strategy established
- API specification validates

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.