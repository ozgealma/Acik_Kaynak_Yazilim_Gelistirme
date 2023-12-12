import requests

url = "https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata"

response = requests.get(url)

if response.status_code == 200:
    meal_data = response.json()
    
    # Verileri ekrana yazdırma
    print("Meals:")
    for meal in meal_data["meals"]:
        print(f"Meal ID: {meal['idMeal']}")
        print(f"Meal Name: {meal['strMeal']}")
        print(f"Category: {meal['strCategory']}")
        print(f"Area: {meal['strArea']}")
        print(f"Instructions: {meal['strInstructions']}")
        
        # Malzemeleri ve ölçüleri ekrana yazdırma
        print("\nIngredients:")
        for i in range(1, 21):
            ingredient_key = f"strIngredient{i}"
            measure_key = f"strMeasure{i}"

            ingredient = meal.get(ingredient_key, "")
            measure = meal.get(measure_key, "")

            if ingredient and measure:
                print(f"{ingredient}: {measure}")

        print("\nImage URL:", meal['strMealThumb'])
        print("Tags:", meal.get('strTags', ""))
        print("YouTube Video URL:", meal.get('strYoutube', ""))
        print("\n" + "=" * 50 + "\n")
else:
    print(f"Error {response.status_code}: Unable to fetch data from the API.")
