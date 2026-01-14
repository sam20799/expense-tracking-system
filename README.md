# Budget Buddy

- This project started as a simple local expense tracker — and evolved into a production-ready full-stack system after facing real deployment challenges.

- It is built with a FastAPI backend and Streamlit frontend, designed using an API-first approach, and deployed on the cloud with a PostgreSQL production database.

- Along the way, the system was refactored to handle real-world constraints such as environment-based configuration, containerized file systems, database persistence, structured logging, and automated testing.

- This repository demonstrates not just feature development, but how to take a Python project from “works locally” to “works in production.”
## Preview

### Add/Update Page
![Add/Update Page](/add_update.png)

### Category wise Analytics Page
![Analytics Page](/category_analytics.png)

### Monthly Analytics Page
![Analytics Page](/monthly_analytics.png)


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **database/**: Contains creation and testing of postgresql.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions


1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn backend.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```