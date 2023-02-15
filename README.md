# Development

## Database

Start it up with `docker compose up -d`

## Backend

1. Make a virtual environment, enter it, install dependencies from requirement.txt
2. Set up env file from test.env in same directory with same values
3. Run migrations `python manage.py migrate`
4. Create superuser `python manage.py createsuperuser`
5. Run server `python manage.py runserver`
6. Login to admin backend and fill in visits data

## Frontend

1. Install dependencies `npm install`
2. Start frontend `npm start`
