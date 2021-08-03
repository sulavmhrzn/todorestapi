# DRF-Todo Rest API
A todo rest api made using django and django rest framework.

## Technology Used
1. Docker
1. Django
1. Django Rest Framework

## Installation
1. Clone the repository
    ```bash
    git clone https://github.com/sulavmhrzn/toread-python.git
    ```
1. Create a virtual environment
    ```python
    python -m venv venv
    ```
1. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
1. Install requirements
    ```python
    pip install -r requirements.txt
    ```

## Post Installation
1. Database migrations
    ```python
    python manage.py migrate
    ```

## Run Server
```python
python manage.py runserver
```

## Docker
1. Build 
    ```bash
    docker-compose build
    ```
2. Run
    ```bash
    docker-compose up
    ```