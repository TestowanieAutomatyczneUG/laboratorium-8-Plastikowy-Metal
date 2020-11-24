from src.sample.main import *
import unittest


class MealTest(unittest.TestCase):

    # SET UP

    def setUp(self):
        self.temp = Meal()

    # BY NAME

    def test_get_meals_by_name1(self):
        self.assertEqual(self.temp.get_meals_by_name("Steak"), ['Steak Diane', 'Steak and Kidney Pie'])

    def test_get_meals_by_name2(self):
        self.assertEqual(self.temp.get_meals_by_name("Beef"),
                         ['Beef Lo Mein', 'Szechuan Beef', 'Beef Wellington', 'Beef stroganoff', 'Minced Beef Pie', 'Beef Bourguignon', 'Beef Sunday Roast', 'Beef Dumpling Stew', 'Braised Beef Chilli', 'Massaman Beef curry', 'Beef and Oyster pie', 'Beef and Mustard Pie', 'Jamaican Beef Patties', 'Beef Brisket Pot Roast', 'Corned Beef and Cabbage', 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber'])

    def test_get_meals_by_name_not_found1(self):
        self.assertEqual(self.temp.get_meals_by_name("Rapapara"), "No meals found")

    def test_get_meals_by_name_not_found2(self):
        self.assertEqual(self.temp.get_meals_by_name("Ching chang"), "No meals found")

    def test_get_meals_by_name_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meals_by_name(1231)

    def test_get_meals_by_name_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meals_by_name({})

    def test_get_meals_by_name_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meals_by_name(None)

    # BY FIRST LETTER

    def test_get_meal_by_first_letter1(self):
        self.assertEqual(self.temp.get_meal_by_first_letter("a"),
                         ['Apple Frangipan Tart', 'Apple & Blackberry Crumble'])

    def test_get_meal_by_first_letter2(self):
        self.assertEqual(self.temp.get_meal_by_first_letter("e"),
                         ['Eton Mess', 'Eccles Cakes', 'English Breakfast', 'Escovitch Fish', 'Egg Drop Soup', 'Egyptian Fatteh'])

    def test_get_meal_by_first_letter_not_found1(self):
        self.assertEqual(self.temp.get_meal_by_first_letter("ź"), "Wrong char")

    def test_get_meal_by_first_letter_not_found2(self):
        self.assertEqual(self.temp.get_meal_by_first_letter("ą"), "Wrong char")

    def test_get_meals_by_first_letter_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_first_letter(1231)

    def test_get_meals_by_first_letter_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_first_letter("siema")

    def test_get_meals_by_first_letter_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_first_letter(None)

    # BY ID

    def test_get_meal_by_id1(self):
        self.assertEqual(self.temp.get_meal_by_id(52772), ['Teriyaki Chicken Casserole'])

    def test_get_meal_by_id2(self):
        self.assertEqual(self.temp.get_meal_by_id(52775), ['Vegan Lasagna'])

    def test_get_meal_by_id_not_found1(self):
        self.assertEqual(self.temp.get_meal_by_id(997), "No meals found")

    def test_get_meal_by_id_not_found2(self):
        self.assertEqual(self.temp.get_meal_by_id(1337), "No meals found")

    def test_get_meals_by_id_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_id(-100)

    def test_get_meals_by_id_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_id("siema")

    def test_get_meals_by_id_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_by_id(None)

    # RANDOM MEAL

    def test_get_meal_random1(self):
        self.assertIsNot(self.temp.get_meal_random(), [])

    def test_get_meal_random2(self):
        self.assertIsNot(self.temp.get_meal_random(), [])

    def test_get_meal_random3(self):
        self.assertEqual(len(self.temp.get_meal_random()), 1)

    def test_get_meal_random4(self):
        self.assertEqual(len(self.temp.get_meal_random()), 1)

    # MEAL CATEGORIES

    def test_get_meal_categories1(self):
        self.assertEqual(self.temp.get_meal_categories(),
                         ['Beef', 'Chicken', 'Dessert', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter', 'Vegan', 'Vegetarian', 'Breakfast', 'Goat'])

    # MAIN INGREDIENT

    def test_get_meal_by_main_ingredient1(self):
        self.assertEqual(self.temp.get_meal_filter_by_main_ingredient('chicken_breast'),
                         ['Chick-Fil-A Sandwich', 'Chicken Couscous', 'Chicken Fajita Mac and Cheese', 'Chicken Ham and Leek Pie', 'Chicken Quinoa Greek Salad', "General Tso's Chicken", 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes', 'Katsu Chicken curry', 'Rappie Pie'])

    def test_get_meal_by_main_ingredient2(self):
        self.assertEqual(self.temp.get_meal_filter_by_main_ingredient('cabbage'),
                         ['Bigos (Hunters Stew)', 'Corned Beef and Cabbage', 'Crispy Sausages and Greens', 'Gołąbki (cabbage roll)', 'Rosół (Polish Chicken Soup)', 'Yaki Udon'])

    def test_get_meals_by_main_ingredient_not_found1(self):
        self.assertEqual(self.temp.get_meal_filter_by_main_ingredient("Rapapara"), "No meals found")

    def test_get_meals_by_main_ingredient_not_found2(self):
        self.assertEqual(self.temp.get_meal_filter_by_main_ingredient("Daswidanja"), "No meals found")

    def test_get_meals_by_main_ingredient_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_main_ingredient(123)

    def test_get_meals_by_main_ingredient_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_main_ingredient(["siema"])

    def test_get_meals_by_main_ingredient_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_main_ingredient(None)

    # CATEGORY get_meal_filter_by_category('Lamb')

    def test_get_meals_by_category1(self):
        self.assertEqual(self.temp.get_meal_filter_by_category('Lamb'), ['Kapsalon', 'Keleya Zaara', 'Lamb and Lemon Souvlaki', 'Lamb and Potato pie', 'Lamb Biryani', 'Lamb Rogan josh', 'Lamb Tagine', 'Lamb tomato and sweet spices', 'Lamb Tzatziki Burgers', 'Lancashire hotpot', 'McSinghs Scotch pie', 'Rigatoni with fennel sausage sauce', 'Stuffed Lamb Tomatoes', 'Tunisian Lamb Soup'])

    def test_get_meals_by_category2(self):
        self.assertEqual(self.temp.get_meal_filter_by_category('Chicken'), ['Brown Stew Chicken', 'Chick-Fil-A Sandwich', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Couscous', 'Chicken Enchilada Casserole', 'Chicken Fajita Mac and Cheese', 'Chicken Ham and Leek Pie', 'Chicken Handi', 'Chicken Karaage', 'Chicken Marengo', 'Chicken Parmentier', 'Chicken Quinoa Greek Salad', 'Coq au vin', 'Crock Pot Chicken Baked Tacos', 'French Onion Chicken with Roasted Carrots & Mashed Potatoes', "General Tso's Chicken", 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes', 'Jerk chicken with rice & peas', 'Katsu Chicken curry', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Nutty Chicken Curry', 'Pad See Ew', 'Potato Gratin with Chicken', 'Rappie Pie', 'Rosół (Polish Chicken Soup)', 'Shawarma', 'Tandoori chicken', 'Teriyaki Chicken Casserole', 'Thai Green Curry'])

    def test_get_meals_by_category_wrong_category1(self):
        self.assertEqual(self.temp.get_meal_filter_by_category('Dadadada'), "No meals found")

    def test_get_meals_by_category_wrong_category2(self):
        self.assertEqual(self.temp.get_meal_filter_by_category('Ffffffffffff'), "No meals found")

    def test_get_meals_by_category_wrong_category_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_category(123)

    def test_get_meals_by_category_wrong_category_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_category(["siema"])

    def test_get_meals_by_category_wrong_category_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_category(None)

    # AREA

    def test_get_meals_by_area1(self):
        self.assertEqual(self.temp.get_meal_filter_by_area('Polish'), ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)', 'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)', 'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)'])

    def test_get_meals_by_area2(self):
        self.assertEqual(self.temp.get_meal_filter_by_area('French'), ['Beef Bourguignon', 'Boulangère Potatoes', 'Brie wrapped in prosciutto & brioche', 'Chicken Basquaise', 'Chicken Marengo', 'Chicken Parmentier', 'Chinon Apple Tarts', 'Chocolate Gateau', 'Chocolate Souffle', 'Coq au vin', 'Duck Confit', 'Fennel Dauphinoise', 'Fish Stew with Rouille', 'Flamiche', 'French Lentils With Garlic and Thyme', 'French Omelette', 'French Onion Soup', 'Pear Tarte Tatin', 'Pork Cassoulet', 'Prawn & Fennel Bisque', 'Provençal Omelette Cake', 'Ratatouille', 'Steak Diane', 'Summer Pistou', 'Tarte Tatin', 'Three-cheese souffles', 'Tuna Nicoise', 'White chocolate creme brulee'])

    def test_get_meals_by_area_wrong_area1(self):
        self.assertEqual(self.temp.get_meal_filter_by_area('Gibberish'), "No meals found")

    def test_get_meals_by_area_wrong_area2(self):
        self.assertEqual(self.temp.get_meal_filter_by_area('Mascarpone'), "No meals found")

    def test_get_meals_by_area_wrong_area_exception1(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_area(123)

    def test_get_meals_by_area_wrong_area_exception2(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_area(["siema"])

    def test_get_meals_by_area_wrong_area_exception3(self):
        with self.assertRaises(ValueError):
            self.temp.get_meal_filter_by_area(None)


    # TEAR DOWN

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
