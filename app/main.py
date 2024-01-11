# Fast API Docs : https://fastapi.tiangolo.com/
# import uvicorn  # When using debugging, uncomment debug if statement at bottom of file.
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# get config values from .env
config = dotenv_values(".env")


@app.get("/")
async def root(request: Request):
    return RedirectResponse(url="/index")


@app.get("/index", response_class=HTMLResponse)
async def home(request: Request):
    if request.method.lower() != 'get':
        # Raise http exceptions for unsupported request methods, Json responses for data handling
        raise HTTPException(
            status_code=405,
            detail=f"Request method not allowed: {request.method}"
        )
    else:
        index_var = 'Index_variable'
        return templates.TemplateResponse("index.html", {"request": request, "index_var": index_var})


@app.get("/second")
async def second(request: Request):
    second_var = 'Second_variable'
    return templates.TemplateResponse("second.html", {"request": request, "second_var": second_var})


@app.get("/api")
async def default(request: Request):
    return JSONResponse(
        content={
            "Info": "Below these are the endpoints that are reserved for our application with a brief description",
            "/": "Root page for SSO",
            "index": "Index Url - html response",
            "second": "Second browser endpoint - html response",
            "keepalive": "Keepalive 200 response",
            "api": "List of api endpoints, both browser and json api responses - Json Response",
            "docs": "Swagger API docs"
        },
        status_code=200
    )


@app.get("/keepalive")
async def keepalive():
    return {
        "keepalive":
            200
    }


# Used for debugging purposes
#   Uncomment 'import uvicorn' at top of file
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
