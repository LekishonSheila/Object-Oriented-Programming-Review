

// 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.



class AncestralStories{
   constructor(length,moralLessons,ageGroup,title,language){
       this.length=length;
       this.moralLessons=moralLessons;
       this.ageGroup=ageGroup;
       this.title=title;
       this.language=language;
   }
   translateStory(newLanguage){
       if(this.language !== newLanguage){
           return this.language = newLanguage
       }
       else{
           return this.language
       }
   }
   addStoryToDatabase() {
       let database = []


           if(!database.includes(this.title)){
               database.push(this);
               console.log(database);
              
           }
           else{
               console.log("This story already exists in storage");
           }
       }
      
     }


class StoryTeller extends AncestralStories{
   constructor(length,moralLessons,ageGroup,title,language,name){
       super(length,moralLessons,ageGroup,title,language)
       this.name=name;
   }
   tellstory(){
       console.log(`This is a story called ${this.title}, it teaches ${this.ageGroup} about ${this.moralLessons}`);
   }
}




  
let story1 = new AncestralStories("long","courage","children","The Lion King","English");
let story2 = new AncestralStories("short","hardwork","teenagers","Vuna Ulichopanda","Kiswahili")
console.log(story1);
console.log(story1.translateStory("Kiswahili"));
story1.addStoryToDatabase()


let abunuwasi = new StoryTeller("long","bravery","Young Adults","Adventures of Kinjikitile","Mijikenda","Abunuwasi");
console.log(abunuwasi);
abunuwasi.tellstory()



// 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.

class Recipe{
    constructor(ingredients,preparationTime,cookingMethod,nutritionalInfo){
        this.ingredients=ingredients;
        this.preparationTime=preparationTime;
        this.cookingMethod=cookingMethod;
        this.nutritionalInfo=nutritionalInfo;
 
 
    }
    timeForPreparation(){
        if(this.preparationTime>=3){
            console.log("this cuisine takes a long time to prepare")
        }
        else{
            console.log("This cuisine can be prepared within a reasonable amount of time");
        }
    }
    checkForItems(){
        if(this.ingredients.includes("beans")||this.ingredients.includes("maize")||this.ingredients.includes("njahi")){
            console.log("You need a pressure cooker to boil this first");
        }
        else{
            console.log("A normal cooker will work just fine");
        }
    }
 }
 class MoroccanRecipe extends Recipe{
    constructor(ingredients,preparationTime,cookingMethod,nutritionalInfo,flavourings){
        super(ingredients,preparationTime,cookingMethod,nutritionalInfo)
        this.flavorings = flavourings;
       
    }
 
 
 }
 class EthiopianRecipe extends Recipe{
    constructor(ingredients,preparationTime,cookingMethod,nutritionalInfo,typeOfOilUsed){
        super(ingredients,preparationTime,cookingMethod,nutritionalInfo)
        this.typeOfOilUsed = typeOfOilUsed;
       
    }
 
 
 }
 class NigerianRecipe extends Recipe{
    constructor(ingredients,preparationTime,cookingMethod,nutritionalInfo,chilliesUsed){
        super(ingredients,preparationTime,cookingMethod,nutritionalInfo)
        this.chilliesUsed = chilliesUsed;
 
 
 }
 }
 const recipe1 = new Recipe(["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"],60, "Boiling/Stir-frying","carbohydrates");
 console.log(recipe1)
 const moroccan_recipe = new MoroccanRecipe(["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling","High in vitamins","Cumin")
 console.log(moroccan_recipe)
 const ethiopian_recipe = new EthiopianRecipe(["Flour", "Water", "Salt"], 60, "Fermentation", "Contains healthy amino acids", "Fresh fry")
 console.log(ethiopian_recipe)
 const nigerian_recipe = new NigerianRecipe(["mushroom", "Meat", "Fish", "Vegetables", "Pepper"], 90, "dry-fry","High in Protein", 3)
 console.log(nigerian_recipe)
 
 
 recipe1.checkForItems()
 
 

 
