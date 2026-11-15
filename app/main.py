from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import ai, board

app = FastAPI(title="SKS Master API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai.router, prefix="/ai")
app.include_router(board.router, prefix="/board")

# Root folder se index.html ko serve karne ke liye
BASE_DIR = Path(__file__).resolve().parent.parent

@app.get("/", response_class=HTMLResponse)
async def root():
    html_file = BASE_DIR / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    return "<h3>Error: SKS_MASTER_API folder ke andar index.html file nahi mili!</h3>"