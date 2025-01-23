from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to query recipes based on ingredients
def get_recipes(ingredients):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    # Search for recipes containing any of the input ingredients
    query = "SELECT name, instructions FROM recipes WHERE "
    query += " OR ".join([f"ingredients LIKE '%{ingredient}%'" for ingredient in ingredients])
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return results

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Search route
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    ingredients = data.get('ingredients', [])
    recipes = get_recipes(ingredients)
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
