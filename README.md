📘 FastAPI Learning Notes
🔹 Phase 1 — FastAPI Mental Model
1️⃣ What is FastAPI?

FastAPI is a thin HTTP layer around Python functions.

It:

receives HTTP requests
validates input
calls your Python function
converts return value into HTTP response

It does NOT:

contain business logic
design architecture
manage your database automatically


2️⃣ Core Idea

FastAPI translates HTTP ↔ Python functions.
Your logic should live outside FastAPI.


3️⃣ Request Lifecycle
Client → HTTP Request
        ↓
FastAPI matches route
        ↓
Validates input
        ↓
Calls Python function
        ↓
Function returns data
        ↓
FastAPI sends HTTP response

4️⃣ Express.js Comparison

Express:

app.post("/expenses", (req, res) => {
  // parse
  // validate
  // logic
  // res.json()
})


FastAPI:

@app.post("/expenses")
def add_expense(expense: Expense):
    return result


Difference:

Express → manual parsing & validation
FastAPI → automatic parsing & validation (via type hints)

5️⃣ Important Concepts

FastAPI() creates the app instance
@app.get() / @app.post() map routes to functions

Return dict → automatically converted to JSON
Type hints enable validation & docs


6️⃣ Mapping to Clean Architecture
Pure Python         	FastAPI
main.py	                app + routing
validators.py	        Pydantic models
processor.py        	service logic
storage.py	            database layer
logging	                same logging




🔹 Phase 2 — Minimal FastAPI Setup
1️⃣ Environment Setup

Create virtual environment:

python -m venv venv
venv\Scripts\activate


Install:

pip install fastapi uvicorn


Why:

fastapi → framework
uvicorn → ASGI server (runs the app)


2️⃣ Minimal App Example
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is working"}


3️⃣ Running the Server
uvicorn main:app --reload


Meaning:

main → filename
app → FastAPI instance
--reload → auto restart on code changes

Open:

http://127.0.0.1:8000


4️⃣ Built-in Documentation

Swagger UI:

http://127.0.0.1:8000/docs


FastAPI auto-generates API documentation based on:

routes
type hints
validation models

5️⃣ What We Learned

FastAPI exposes Python functions over HTTP
Returning dict → automatic JSON response
Uvicorn runs the server
Framework handles request/response conversion