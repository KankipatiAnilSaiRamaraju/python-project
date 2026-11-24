from flask import Flask, render_template

app = Flask(__name__)

food_items = [
    {
        "name": "Cheese Burger",
        "price": 149,
        "category": "Fast Food",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600"
    },
    {
        "name": "Delicious Pizza",
        "price": 299,
        "category": "Italian",
        "image": "https://images.unsplash.com/photo- pizza"
    },
    {
        "name": "Chicken Biryani",
        "price": 199,
        "category": "Indian",
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?w=600"
    },
    {
        "name": "Veg Sandwich",
        "price": 99,
        "category": "Snacks",
        "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=600"
    },
    {
        "name": "French Fries",
        "price": 89,
        "category": "Snacks",
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600"
    },
    {
        "name": "Chocolate Cake",
        "price": 129,
        "category": "Dessert",
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600"
    }
]


@app.route("/")
def home():
    return render_template("index.html", foods=food_items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
