# OctoFit Tracker

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. This project is structured into a backend built with Django and a frontend developed using React.

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                     # Python virtual environment for the backend
│   ├── octofit_tracker/          # Django application package
│   │   ├── __init__.py           # Marks the directory as a Python package
│   │   ├── asgi.py                # ASGI configuration for asynchronous requests
│   │   ├── settings.py            # Django settings and configuration
│   │   ├── urls.py                # URL routing for the Django application
│   │   └── wsgi.py                # WSGI configuration for synchronous requests
│   ├── manage.py                  # Command-line utility for interacting with the Django project
│   └── requirements.txt           # Required Python packages for the project
└── frontend/
    ├── src/
    │   ├── App.jsx                # Main component of the React application
    │   └── main.jsx               # Renders the React application to the DOM
    ├── package.json               # Configuration file for npm
    └── vite.config.js             # Configuration for Vite, the build tool
```

## Setup Instructions

### Backend Setup

1. **Create a Python Virtual Environment:**
   Run the following command to create a virtual environment for the backend:
   ```bash
   python3 -m venv backend/venv
   ```

2. **Activate the Virtual Environment:**
   ```bash
   source backend/venv/bin/activate
   ```

3. **Install Required Packages:**
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Run Migrations:**
   Apply migrations to set up the database:
   ```bash
   python backend/manage.py migrate
   ```

5. **Run the Development Server:**
   Start the Django development server:
   ```bash
   python backend/manage.py runserver
   ```

### Frontend Setup

1. **Install Frontend Dependencies:**
   Navigate to the frontend directory and install the required npm packages:
   ```bash
   npm install
   ```

2. **Run the Frontend Development Server:**
   Start the Vite development server:
   ```bash
   npm run dev
   ```

## Features

- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.