# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal page/website built with FastAPI backend and TailwindCSS frontend, deployed on AWS.

## Technology Stack

- **Python**: Backend language
- **FastAPI**: Web framework for API and serving static content
- **uv**: Fast Python package manager and project management
- **TailwindCSS**: Utility-first CSS framework
- **AWS**: Cloud hosting and deployment platform

## Common Commands

### Package Management
```bash
# Install dependencies
uv sync

# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>

# Run commands in the virtual environment
uv run <command>
```

### Development Server
```bash
# Run FastAPI development server (typically)
uv run uvicorn main:app --reload

# Or if using a different entry point
uv run fastapi dev
```

### TailwindCSS
```bash
# Watch and compile Tailwind CSS (typical setup)
npx tailwindcss -i ./static/input.css -o ./static/output.css --watch

# Build for production
npx tailwindcss -i ./static/input.css -o ./static/output.css --minify
```

### Testing
```bash
# Run tests (when configured)
uv run pytest

# Run tests with coverage
uv run pytest --cov
```

## Architecture

### Expected Structure
- FastAPI application serving both API endpoints and static HTML/CSS/JS
- Static files (HTML, CSS, JS) served from a `/static` directory
- TailwindCSS compiled styles included in static assets
- API routes typically in `/api` or similar structure
- HTML templates may use Jinja2 (FastAPI's default) or be served as static files

### AWS Deployment
- Application likely deployed using AWS services (EC2, ECS, Lambda, or Elastic Beanstalk)
- Static assets may be served via S3 + CloudFront for better performance
- Environment-specific configurations managed through environment variables or AWS Parameter Store

## Development Workflow

1. Make changes to Python code or HTML templates
2. TailwindCSS processes automatically with `--watch` flag during development
3. FastAPI's `--reload` flag automatically restarts server on code changes
4. Test locally before deploying to AWS
