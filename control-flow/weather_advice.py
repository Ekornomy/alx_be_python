users_weather_condition = input("What's the weather like today? (sunny/rainy/cold): ")
if users_weather_condition == "sunny":
    print("wear a t-shirt and sunglasses.")
elif users_weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif users_weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather.")