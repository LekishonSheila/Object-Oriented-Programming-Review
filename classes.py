# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


class AncestralStories:
    def __init__(self, length, moralLessons, ageGroup, title, language):
        self.length = length
        self.moralLessons = moralLessons
        self.ageGroup = ageGroup
        self.title = title
        self.language = language
    def __str__(self):
       return f"{self.title} is a {self.length} story that teaches {self.moralLessons} to {self.ageGroup} and is written in {self.language} language."
    def translateStory(self, newLanguage):
        if self.language != newLanguage:
            self.language = newLanguage
            return self.language
        else:
            return self.language
    def addStoryToDatabase(self):
        database = []
        if self.title not in database:
            database.append(self.title)
            print(database)
        else:
            print("This story already exists in storage")
class StoryTeller(AncestralStories):
    def __init__(self, length, moralLessons, ageGroup, title, language, name):
        super().__init__(length, moralLessons, ageGroup, title, language)
        self.name = name
    def tellStory(self):
        print(f"This is a story called {self.title}. It teaches {self.ageGroup} about {self.moralLessons}.")
 # instances
story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
story2 = AncestralStories("short", "hardwork", "teenagers", "Vuna Ulichopanda", "Kiswahili")
print(story1)
print(story1.translateStory("Kiswahili"))
story1.addStoryToDatabase()






# // 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# // The app needs to handle recipes from different African countries, each with its
# // unique ingredients, preparation time, cooking method, and nutritional
# // information. Consider creating a `Recipe` class, and think about how you might
# // create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# // `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# // methods.


class Recipe:
   def __init__(self, name, country, ingredients, preparation_time, cooking_methods, nutritional_info):
       self.name = name
       self.country = country
       self.ingredients = ingredients
       self.preparation_time = preparation_time
       self.cooking_methods = cooking_methods
       self.nutritional_info = nutritional_info
   def timeForPreparation(self):
       if self.preparation_time >= 3:
           return "This coloured Rice takes a long time to prepare"
       else:
           return "This coloured Rice can be prepared within a reasonable amount of time"
   def __str__(self):
       return f"Name: {self.name}\ncountry: {self.country}\ingredients: {', '.join(self.ingredients)}\npreparation_time: {self.preparation_time} minutes\ncooking_method: {self.cooking_methods}\nnutrition_info: {self.nutritional_info}"
class MoroccanRecipe(Recipe):
   def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
       super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)
       self.spice_level = spice_level
class EthiopianRecipe(Recipe):
   def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_included):
       super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)
       self.injera_included = injera_included
class NigerianRecipe(Recipe):
   def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, is_spicy):
       super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
       self.is_spicy = is_spicy
# Instances
moroccan_recipe = MoroccanRecipe("Coloured Rice",["rice", "onion", "olive oil", "spices"],45,"Boiled ","Nice for vitamins","Medium")
print(moroccan_recipe)
ethiopian_recipe = EthiopianRecipe("Boiled eggs",["eggs","water"],20,"protein","no spices",True)
print(ethiopian_recipe)
nigerian_recipe = NigerianRecipe("Jollof Rice",["rice", "tomatoes", "onion", "pepper", "spices"],45,"Popular party dish",'is_spicy',True)
print(nigerian_recipe)