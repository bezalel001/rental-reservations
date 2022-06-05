# Rental reservations
A table of Reservations


## Tools:

- Language: [Python](https://www.python.org/)
- Frameworks: [Django](https://www.djangoproject.com/)
- Virtual Environment: [Pipenv](https://pipenv.pypa.io/en/latest/)
- Containers: [Docker](https://www.docker.com/)
- Backend Performance: Caching, Indexing
- Database: [PostgreQL](https://www.postgresql.org/) 
- Others: [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)

## How to run the code

- Download the zip file or clone the repo [here](https://github.com/bezalel001/rental-reservations.git)
- Create a `.env` file in the root directory and copy the content of `.env.example` into it.
- Run  `docker-compose up -d --build` to launch the app
- Home page:  `localhost:8000`
- Admin page:  `localhost:8000/admin`
  - username: `guest001`
  - pw: `misha001`

- Run `docker-compose exec web python manage.py test` to run unit test.



### Note:

- I implemented some simple backend performance techniques for demonstration purposes only
- I also created a Custom user app for demonstration purposes only


