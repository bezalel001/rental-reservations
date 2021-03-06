# Rental reservations
A table of Reservations

[video presentation](https://www.loom.com/share/bc0e89bd45c040f3ba6a69b42d9f2025)


## Tools:

- Language: [Python](https://www.python.org/)
- Frameworks: [Django](https://www.djangoproject.com/)
- Virtual Environment: [Pipenv](https://pipenv.pypa.io/en/latest/)
- Containers: [Docker](https://www.docker.com/)
- Backend Performance: Caching, Indexing
- Database: [PostgreQL](https://www.postgresql.org/) 
- Video: [Loom](https://www.loom.com/looms)
- Others: [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)

## How to run the code

- Download the zip file or clone the repo [here](https://github.com/bezalel001/rental-reservations.git)
- Create a `.env` file in the root directory and copy the content of `.env.example` into it.
- Run  `docker-compose up -d --build` to launch the app
- Home page:  `localhost:8000`
- Admin page:  `localhost:8000/secret-dashboard`
  - username: `guest001`
  - pw: `misha001`

- Run `docker-compose exec web python manage.py test` to run unit test.



### Note:

- I implemented some simple backend performance techniques and security settings as a way of demonstrating how I would approach real-world apps
- I also created a Custom user app for demonstration purposes only

### Suggestions
- Add more unit tests to ensure test coverage
- Ensure that reservations can only be time/date in the future
