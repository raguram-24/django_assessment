
Octopus Assignment
===============================
## Details
This Application reads a CSV file, merge with models and renders it on the browser



## Bootstrap instructions
To run this server locally,

1. Install python 3 on your local machine 
2. Clone the repository using **git clone https://github.com/raguram-24/django_assessment.git**.
3. Navigate to project root directory and open a terminal.
4. Run the following commands
    1. pip install pipenv
    2. pipenv install django
    3. pipenv shell
    4. pip freeze
    5. python manage.py runserver


To run this server locally using docker,

1. Install docker on your machine.
2. In the terminal, navigate to your project root directory.
3. Run **docker build .**
4. Once its built, it will return the container id and 
5. Copy the container id or to view all the containers and get the container id run **docker ps -a**
6. Run **docker run -it -p 8000:8000 <container_id>**.
7. To stop the docker container run **docker stop <container_id>**.
8. To restart the docker container run **docker start <container_id>**.

## Assumptions
1. Student_Score is taken as Subject_score


## API endpoints
1. http://localhost:8000/api/v1/schools
2. http://localhost:8000/api/v1/answers
3. http://localhost:8000/api/v1/assessmentareas
4. http://localhost:8000/api/v1/awards
5. http://localhost:8000/api/v1/classes
6. http://localhost:8000/api/v1/students
7. http://localhost:8000/api/v1/subjects
8. http://localhost:8000/api/v1/summary



