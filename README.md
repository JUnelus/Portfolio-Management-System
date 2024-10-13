# Portfolio Management System

## Overview
This Portfolio Management System is built with Flask for the backend, MongoDB for the database, and React for the frontend. It allows users to add, view, and retrieve portfolios.

## Technologies Used
- **Backend**: Flask
- **Frontend**: React
- **Database**: MongoDB (Atlas or Localhost)

![img.png](img.png)

## Installation and Setup

### 1. Clone the Repository
Clone the repository from GitHub or download the source code as a ZIP file.

```bash
git clone https://github.com/JUnelus/Portfolio-Management-System.git
cd Portfolio-Management-System
```

### 2. Backend Setup (Flask API)
1. Set up a virtual environment and install the required dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. Create a `.env` file to store environment variables for MongoDB connection (MongoDB Atlas or Localhost).
    ```env
    MONGO_URI=mongodb://localhost:27017/
    ```

3. Run the Flask server:
    ```bash
    python app.py
    ```

The API will be accessible at `http://localhost:5000`.

### 3. Frontend Setup (React)
1. Navigate to the `frontend` directory and install dependencies:
    ```bash
    cd frontend
    npm install
    ```

2. Start the React app:
    ```bash
    npm start
    ```

The frontend will run on `http://localhost:3000`.

## API Endpoints
- **POST /portfolio**: Add a new portfolio.
- **GET /portfolio**: Get all portfolios.
- **GET /portfolio/{name}**: Get a specific portfolio by name.
