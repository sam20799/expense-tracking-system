# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Preview

### Add/Update Page
![Add/Update Page](/preview1_add_update.png)

### Analytics Page
![Analytics Page](/preview2_analytics.png)

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
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
    uvicorn server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run app.py
   ```