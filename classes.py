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


# question3
# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.
class Species:
    def __init__(self, diet, typical_lifespan, migration_patterns):
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_patterns = migration_patterns
    
    def type_of_animal(self):
        if self.diet == "herbivorous":
            print("This animal is not a danger to other animals")
        elif self.diet == "omnivorous":
            print("This animal feeds on plants but also feeds on some animals")
        else:
            print("This animal is very dangerous to other animals and does not eat plants")


class Predator(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, type_of_teeth, claws, venom, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.type_of_teeth = type_of_teeth
        self.claws = claws
        self.venom = venom
        self.name = name

    def fast_killers(self):
        if self.venom:
            print(f"The bite of a {self.name} kills within hours")
        else:
            print(f"The bite of a {self.name} is not deadly")

    def method_of_killing(self):
        if "carnassial teeth" in self.type_of_teeth:
            print(f"A {self.name} kills by slicing up their prey")
        else:
            print("This predator cannot shear their prey's meat after attacks")


class Prey(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, defense_mechanisms, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.defense_mechanisms = defense_mechanisms
        self.name = name
  
# instances
lion = Predator("carnivorous", 12, "non-migratory", ["carnassial teeth"], True, False, "Lion")
gazelle = Prey("herbivorous", 10, "seasonal migration", ["speed", "herd behavior"], "Gazelle")
lion.type_of_animal() 
lion.fast_killers()   
lion.method_of_killing() 
gazelle.type_of_animal() 
print(gazelle.defense_mechanisms)  


# question4
# 4.**African Music Festival:** You're in charge of organising a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
class Artist:
    def __init__(self, artistsName, country, musicStyle, instruments):
        self.artistsName = artistsName
        self.country = country
        self.musicStyle = musicStyle
        self.instruments = instruments

    def addArtists(self):
        if self.artistsName not in artistDatabase:
            artistDatabase.append(self.artistsName)

    def removeArtists(self):
        return artistDatabase.pop(0)


class Performance(Artist):
    def __init__(self, artistsName, country, musicStyle, instruments, startTime, stopTime):
        super().__init__(artistsName, country, musicStyle, instruments)
        self.startTime = startTime
        self.stopTime = stopTime

    def duration(self):
        timeTaken = self.stopTime - self.startTime
        return f"The duration for the performance was {timeTaken}"

    def schedule(self):
        eventSchedule = {}
        eventSchedule[self.artistsName] = self.startTime
        return eventSchedule


class Stage(Artist):
    def __init__(self, artistsName, country, musicStyle, instruments, supportingArtists):
        super().__init__(artistsName, country, musicStyle, instruments)
        self.supportingArtists = supportingArtists

    def spaceOccupied(self):
        if "drums" in self.instruments and self.supportingArtists:
            return f"{self.artistsName} will occupy only 50% of the stage"
        if "drums" in self.instruments:
            return f"{self.artistsName} will occupy only 70% of the stage"
        if self.supportingArtists:
            return f"{self.artistsName} will occupy only 80% of the stage"


artistDatabase = []

# instances
artist1 = Artist("Justine", "USA", "Intentions", ["guitar", "vocals"])
artist1.addArtists()

performance1 = Performance("Drake", "USA", "Rock", ["guitar", "vocals"], 10, 20)
duration = performance1.duration()
schedule = performance1.schedule()

stage1 = Stage("Jay", "USA", "Rock", ["guitar", "vocals"], True)
spaceOccupied = stage1.spaceOccupied()
print(artistDatabase)
print(duration)
print(schedule)
print(spaceOccupied)



# Q5
# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_value(self):
        return self.price * self.quantity

productA = Product('Laptop', 15000, 2)
productB = Product('Phones', 10000, 2)
productC = Product('Television', 18000, 2)

total_value = productA.calculate_total_value() + productB.calculate_total_value() + productC.calculate_total_value()

print(f'The total value of all products is {total_value}.')
