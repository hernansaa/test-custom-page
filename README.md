# Edu Agency

## Project Overview
This project is a CRM system that includes task management, user authentication, and periodic background processing with Celery.

## Getting Started

### Prerequisites
- Python 3.x
- Redis (optional)
- PostgreSQL (optional)


### Installation
1. Clone the repository:
  ```
  git clone https://github.com/hernansaa/test-custom-page.git
  ```

2. Set up the virtual environment:
  ```
  (in the same level as your project directory, not inside the project)
  python -m venv venv
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

- **core/**: Main project folder containing settings and configuration.
- **your_app/**: Contains the main application logic.


### Celery Configuration

#### Setting Up Celery

Celery is configured in core/celery.py. Make sure Redis is running and start the Celery worker and beat:

  ```
  celery -A core worker --loglevel=info
  celery -A core beat --loglevel=info
  ```
  
  (Redis server in your system should be running at the ip and port SPECIFY)


#### Installation Celery and Redis
(I have done this installation but I keep it for future reference)

1. Install Celery and Required Dependencies

First, you'll need to install Celery and a message broker (commonly, Redis or RabbitMQ) to handle task queues.
  ```
  pip install celery
  pip install redis
  ```

If you don't have Redis installed on your system, you can install it using your package manager. For example:
  
  ```
  sudo apt-get install redis-server
  ```

2. Configure Celery in Your Django Project

Create a celery.py file in your project directory (same level as settings.py).

  celery.py:
  ```
  from __future__ import absolute_import, unicode_literals
  import os
  from celery import Celery
  from django.conf import settings

  # Set the default Django settings module for the 'celery' program.
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

  # Create a Celery instance
  app = Celery('your_project_name')

  # Load task modules from all registered Django app configs.
  app.config_from_object('django.conf:settings', namespace='CELERY')
  app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

  ```
Replace your_project_name with the name of your Django project.


3. Update Django Settings

Add the following Celery configuration settings to your settings.py file:

  ```
  # Celery settings
  CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Use the Redis broker
  CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Store results in Redis
  CELERY_ACCEPT_CONTENT = ['json']
  CELERY_TASK_SERIALIZER = 'json'
  CELERY_RESULT_SERIALIZER = 'json'
  CELERY_TIMEZONE = 'UTC'  # Adjust to your timezone
  ```

4. Create a test Celery Task

In one of your Django app directories (e.g., your_app), create a tasks.py file. Here's an example of a task that updates student statuses based on course finish dates:

tasks.py:

  ```
  from celery import shared_task

  @shared_task
  def print_hello():
      print("Hello! This task runs every 5 seconds.")
  ```

5. Schedule the Celery Task

Next, configure Celery Beat to run this task every 5 seconds. You can do this by adding the schedule to your settings.py:

settings.py
  ```
  from celery.schedules import timedelta

  CELERY_BEAT_SCHEDULE = {
      'print-hello-every-5-seconds': {
          'task': 'your_app.tasks.print_hello',
          'schedule': timedelta(seconds=5),
      },
  }

  ```
Replace your_app with the name of your Django app.


6. Run Celery Workers and Beat

Now, you need to start the Celery worker and Celery beat (scheduler):

- **Start the Celery worker:**:
  ```
  celery -A your_project_name worker --loglevel=info
  ```
- **Start the Celery beat:**:
celery -A your_project_name beat --loglevel=info

(These commands should be run in separate terminal windows or processes.)


7.  Testing

Ensure everything is set up correctly by running the worker and beat. If there are any errors, Celery will log them in the terminal where you started the worker. You can also manually trigger tasks from the Django shell to test if they run correctly.


8. Monitoring and Management (Optional)

Consider setting up monitoring tools like Flower to keep an eye on your Celery tasks:
  ```
  pip install flower
  celery -A your_project_name flower
  ```

