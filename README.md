MS-Club-Projects-Backend
A simple Notes REST API built with **Flask** and **SQLite**.  
This folder contains the backend for a Notes app demonstrating CRUD operations.

 Tech stack
- Python 3.x
- Flask
- Flask-SQLAlchemy (SQLite as DB)

Files
- `app.py` — Flask application with CRUD routes (`/notes`)
- `models.py` — SQLAlchemy `Note` model
- `venv/` — local Python virtual environment (not committed)

#Run locally (quick)
1. Open terminal in this folder.
2. Activate virtualenv:
   - Windows: `.\venv\Scripts\Activate.ps1` (or `venv\Scripts\activate.bat`)
3. Install (if not already): `pip install flask flask_sqlalchemy`
4. Start server: `python app.py`
5. Open API: `http://127.0.0.1:5000`

 Endpoints
- `GET /notes` — list all notes  
- `GET /notes/<id>` — get a note  
- `POST /notes` — create (body JSON: `{ "title": "...", "content": "..." }`)  
- `PUT /notes/<id>` — update (body JSON)  
- `DELETE /notes/<id>` — delete

Demo commands (PowerShell)
```powershell
# Create
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes -Method Post -ContentType "application/json" -Body '{"title":"First note","content":"This is a test note."}'

# List
Invoke-RestMethod -Uri http://127.0.0.1:5000/notes -Method Get
```
