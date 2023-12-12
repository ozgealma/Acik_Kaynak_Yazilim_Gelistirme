from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Örnek yemek verisi
meal_data = {
    "idMeal": "52771",
    "strMeal": "Spicy Arrabiata Penne",
    "strDrinkAlternate": None,
    "strCategory": "Vegetarian",
    "strArea": "Italian",
    "strInstructions": "Bring a large pot of water to a boil... (devam ediyor)",
    "strMealThumb": "https://www.themealdb.com/images/media/meals/ustsqw1468250014.jpg",
    "strTags": "Pasta,Curry",
    "strYoutube": "https://www.youtube.com/watch?v=1IszT_guI08",
    "strIngredient1": "penne rigate",
    "strIngredient2": "olive oil",
    "strIngredient3": "garlic",
    # (diğer malzemeler burada devam ediyor)
}

# Web sayfası için route
@app.route('/')
def home():
    return render_template('index.html', meal=meal_data)

# API endpoint'i
@app.route('/api/meal', methods=['GET'])
def get_meal():
    return jsonify({"meals": [meal_data]})

# Yeni endpoint ve fonksiyon
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
