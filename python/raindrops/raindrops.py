def raindrops(number):
    rain = {3: "Pling", 5: "Plang", 7: "Plong"}
    drops = [v for k, v in rain.items() if not number % k]

    return "".join(drops) if drops else str(number)
