

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




 
