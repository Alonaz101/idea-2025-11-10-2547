# Project Overview: Mood-based Recipe Recommendation MVP

## Features Implemented per Jira Issues

- **SCRUM-208: MVP Architecture and Components**
  - React SPA frontend for user mood input
  - Flask RESTful backend API
  - PostgreSQL database for persistence
  - Redis caching for recipe queries
  - JWT-based authentication

- **SCRUM-209: Data Model Design for MVP**
  - Models for User, Mood, Recipe, Favorite entities implemented via SQLAlchemy

- **SCRUM-210: API Specifications for MVP**
  - Endpoints for login, submitting mood, retrieving recipes

- **SCRUM-211: Security, Privacy & Compliance for MVP**
  - HTTPS assumed for deployment
  - JWT authentication enforced on API
  - Input validation in backend routes

- **SCRUM-212: Performance, Scalability & Reliability for MVP**
  - Redis caching for frequent recipe queries
  - Backend designed for horizontal scaling

- **SCRUM-213: MVP Roadmap and Implementation Considerations**
  - Core MVP features completed: DB schema, seed data, frontend, backend, recommendation engine logic

- **SCRUM-214: Testing, Logging & Monitoring for MVP**
  - Basic structure ready; testing, logging, monitoring to be added (described in issue)

- **SCRUM-215: Post-MVP Enhancements**
  - Placeholder for user accounts enhancement and mood history

- **SCRUM-216: Future Expansions**
  - Placeholder for AI mood detection, multi-language support, offline mode

## Repository Structure

```
/backend
  app.py  # Flask app with models and routes
/frontend
  src/
    App.js  # React SPA mood input and recipe display
/docs
  overview.md  # Project documentation
```

## How to Run

- Backend requires Python, Flask, PostgreSQL, Redis
- Frontend requires Node.js, React

## Next Steps
- Implement full testing, logging, monitoring as per SCRUM-214
- Expand features post-MVP
- Prepare deployment with HTTPS and secrets management

---

**Repository URL:** [https://github.com/Alonaz101/idea-2025-11-10-2547](https://github.com/Alonaz101/idea-2025-11-10-2547)
