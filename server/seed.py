from server.app import app
from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("🌱 Seeding data...")

    # Clear old data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Main Street")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Side Avenue")
    db.session.add_all([r1, r2])

    # Create Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    db.session.add_all([p1, p2])

    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=10, restaurant_id=r2.id, pizza_id=p1.id)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("✅ Done seeding!")
