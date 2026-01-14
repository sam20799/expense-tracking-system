# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

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