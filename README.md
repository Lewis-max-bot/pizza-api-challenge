<!-- PIZZA RESTAURANT API -->

A RESTful Flask API for managing pizzas, restaurants, and their associations. This project follows an MVC structure and uses SQLAlchemy for ORM and Alembic for migrations.

---

<!--TO USE THIS API, DO THE FOLLOWING......  -->

1. Create a virtual enironment by running the command  ..... pipenv shell ..... 

2. Install dependencies by running the command .... pipenv install ....

3. Set env. variables. Do this by running the commands 
    ....export FLASK_APP=server/app.py....
    ....export FLASK_ENV=development....

4. Run migrations 
    ....flask db init
    ....flask db migrate -m "Initial migration"
    ....flask db upgrade

6. Seed the database 
    ....python -m server.seed

7. Run the server
    ....flask run 


 <!-- THE API ENDPOINTS ARE AS FOLLOWS -->

GET/Pizzas => returns a list of all pizzas 
GET/restaurants => returns a list of all restaurants
GET/restaurant_pizza => associates a pizza with a specific pizza 


<!-- TESTING USING POSTMAN -->

=> Use postman to test the post/restaurant_pizzas route