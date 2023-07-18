from flask import Flask, render_template, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__, template_folder='./templates')

run_with_ngrok(app)

@app.route('/')
def index():
  return "<h1>Welcome</h1> <p>This page is under construction<p>"

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/profile/harry')
def profile():
    return "This is Harry's profile"

@app.route('/product/<name>')
def product_page(name):
    return "<h3>Product " + name + "<h3>"

@app.route('/product/<name>/<price>')
def product_information(name, price):
    return "<h2> The product: " + name + " costs: £" + price + "<h2>"

@app.route('/first-template')
def first_template():
    return render_template('first_template.html')

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', name=username)

Animals = [
    {'id': 1, 'title': 'Butterfly', 'image_url': 'https://cdn.pixabay.com/photo/2023/05/30/15/12/blue-butterfuly-8028888_1280.jpg'},
    {'id': 2, 'title': 'Lion', 'image_url': 'https://cdn.pixabay.com/photo/2023/06/29/10/33/lion-8096155_640.png'},
    {'id': 3, 'title': 'dog', 'image_url': 'https://media.istockphoto.com/id/1302412371/photo/happy-easter-concept-preparation-for-holiday-cute-puppy-dog-border-collie-holding-basket-with.webp?b=1&s=612x612&w=0&k=20&c=xxznSYiVO3IWB0lhlt6czsu7Rb7AzBVQq8XsCvAHJkc='},
]

@app.route('/api/animals')
def api_animals():
    return jsonify(Animals)

@app.route('/animals')
def animals():
    return render_template('all_animals.html', animals = Animals)

if __name__ == '__main__':
  app.run()
