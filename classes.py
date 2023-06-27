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