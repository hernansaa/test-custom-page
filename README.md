# Edu Agency

## Project Overview
This project is a CRM system that includes task management, user authentication, and periodic background processing with Celery.

## Getting Started

### Prerequisites
- Python 3.x
- Redis
- PostgreSQL

### Installation
1. Clone the repository:
  ```
  git clone https://github.com/yourusername/yourproject.git
  cd yourproject
  ```

2. Set up the virtual environment:
  ```
  git clone https://github.com/yourusername/yourproject.git
  cd yourproject
  ```

3. Install dependencies:
  ```
  pip install -r requirements.txt
  ```

4. Set up the database:
  ```
  python manage.py migrate
  python manage.py createsuperuser
  ```

5. Run the development server:
  ```
  python manage.py runserver
  ```


### Project Structure

-core/: Main project folder containing settings and configuration.
-your_app/: Contains the main application logic.


### Celery Configuration
#### Setting Up Celery

Celery is configured in core/celery.py. Make sure Redis is running and start the Celery worker and beat:

  ```
  celery -A core worker --loglevel=info
  celery -A core beat --loglevel=info
  ```
  
  (Redis server in your system should be running at the ip and port SPECIFY)


