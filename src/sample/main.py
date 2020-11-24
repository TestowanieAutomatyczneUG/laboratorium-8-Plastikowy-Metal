import requests as req


class Meal:
    def __init__(self):
        self.meals = []
        self.categories = []

    def get_meals_by_name(self, name):
        if type(name) == str:
            r = req.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}')
            r = r.json()['meals']
            if r is not None:
                for meal in r:
                    self.meals.append(meal['strMeal'])
                else:
                    return self.meals
            else:
                return "No meals found"
        else:
            raise ValueError

    def get_meal_by_first_letter(self, letter):
        if type(letter) == str:
            if(len(letter) == 1):
                if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
                    r = req.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
                    r = r.json()['meals']
                    if r is not None:
                        for meal in r:
                            self.meals.append(meal['strMeal'])
                        else:
                            return self.meals
                    else:
                        return "No meals found"
                else:
                    return "Wrong char"
            else:
                raise ValueError
        else:
            raise ValueError

    def get_meal_by_id(self, id_meal):
        if type(id_meal) == int and id_meal >= 0:
            r = req.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id_meal}')
            r = r.json()['meals']
            if r is not None:
                for meal in r:
                    self.meals.append(meal['strMeal'])
                else:
                    return self.meals
            else:
                return "No meals found"
        else:
            raise ValueError

    def get_meal_random(self):
        r = req.get('https://www.themealdb.com/api/json/v1/1/random.php')
        r = r.json()['meals']

        if r is not None:
            for meal in r:
                self.meals.append(meal['strMeal'])
            return self.meals
        else:
            return "No meals found"



    def get_meal_categories(self):
        r = req.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        r = r.json()['categories']
        if r is not None:
            for category in r:
                self.categories.append(category['strCategory'])
            return self.categories
        else:
            return "No categories found"

    def get_meal_filter_by_main_ingredient(self, ingredient):
        if type(ingredient) == str:
            r = req.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}')
            r = r.json()['meals']
            if r is not None:
                for meal in r:
                    self.meals.append(meal['strMeal'])
                else:
                    return self.meals
            else:
                return "No meals found"
        else:
            raise ValueError

    def get_meal_filter_by_category(self, category):
        if type(category) == str:
            r = req.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}')
            r = r.json()['meals']
            if r is not None:
                for meal in r:
                    self.meals.append(meal['strMeal'])
                else:
                    return self.meals
            else:
                return "No meals found"
        else:
            raise ValueError

    def get_meal_filter_by_area(self, area):
        if type(area) == str:
            r = req.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}')
            r = r.json()['meals']

            if r is not None:
                for meal in r:
                    self.meals.append(meal['strMeal'])
                else:
                    return self.meals
            else:
                return "No meals found"
        else:
            raise ValueError
