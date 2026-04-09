# Shared Directory

This directory contains the source code for all three services in the multi-service pipeline.

## Structure

```
shared/
├── frontend/       # mock-frontend (nginx)
│   ├── index.html
│   └── nginx.conf
├── beef1/          # beef1 backend (python)
│   ├── app.py
│   └── Dockerfile
└── beef2/          # beef2 backend (python)
    ├── app.py
    └── Dockerfile
```

## Trigger

Any push to the `shared/` directory on the `main` branch will automatically trigger the `multi-service-deploy` pipeline in Harness.
