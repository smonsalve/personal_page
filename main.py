from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Personal Page", description="Personal website with portfolio")

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with introduction and highlights"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio(request: Request):
    """Portfolio page showcasing projects"""
    # In a real app, this data would come from a database
    projects = [
        {
            "title": "Project 1",
            "description": "Description of your first project",
            "technologies": ["Python", "FastAPI", "TailwindCSS"],
            "image": "/static/images/project1.jpg",
            "github": "https://github.com/yourusername/project1",
            "demo": "https://project1.demo.com"
        },
        {
            "title": "Project 2",
            "description": "Description of your second project",
            "technologies": ["Python", "Django", "PostgreSQL"],
            "image": "/static/images/project2.jpg",
            "github": "https://github.com/yourusername/project2",
            "demo": "https://project2.demo.com"
        },
        {
            "title": "Project 3",
            "description": "Description of your third project",
            "technologies": ["JavaScript", "React", "Node.js"],
            "image": "/static/images/project3.jpg",
            "github": "https://github.com/yourusername/project3",
            "demo": "https://project3.demo.com"
        }
    ]
    return templates.TemplateResponse("portfolio.html", {
        "request": request,
        "projects": projects
    })


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About me page with personal information"""
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page with form"""
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/cv", response_class=HTMLResponse)
async def cv(request: Request):
    """CV/Resume page"""
    # In a real app, this data would come from a database or structured file
    cv_data = {
        "experience": [
            {
                "title": "Software Developer",
                "company": "Company Name",
                "period": "2022 - Present",
                "description": "Description of your role and achievements"
            },
            {
                "title": "Junior Developer",
                "company": "Previous Company",
                "period": "2020 - 2022",
                "description": "Description of your role and achievements"
            }
        ],
        "education": [
            {
                "degree": "Bachelor's in Computer Science",
                "institution": "University Name",
                "period": "2016 - 2020",
                "description": "Relevant coursework and achievements"
            }
        ],
        "skills": [
            {"category": "Backend", "items": ["Python", "FastAPI", "Django", "PostgreSQL"]},
            {"category": "Frontend", "items": ["HTML", "CSS", "TailwindCSS", "JavaScript"]},
            {"category": "DevOps", "items": ["AWS", "Docker", "CI/CD", "Git"]}
        ]
    }
    return templates.TemplateResponse("cv.html", {
        "request": request,
        "cv": cv_data
    })


@app.post("/contact")
async def contact_form(request: Request):
    """Handle contact form submission"""
    form_data = await request.form()
    # TODO: Implement email sending or save to database
    # For now, just acknowledge receipt
    return {"message": "Thank you for your message! I'll get back to you soon."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
