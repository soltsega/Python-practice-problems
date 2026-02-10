# polymorphism in python oop is an ability of an object to take on multiple forms
# polymorphism is used to define the behavior of an object when it is used in a particular context
# polymorphism is used to write code that is flexible and reusable

# example of polymorphism in python
class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# The polymorphic calls - same function, different outputs
start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)



# what are the types of polymorphism?
# 1. Ad-hoc polymorphism: This is when a function can be applied to arguments of different types, and the behavior of the function depends on the type of the arguments. For example, the + operator can be used to add two numbers, concatenate two strings, or merge two lists.
print(1 + 2)  # Output: 3 (integer addition)
print("Hello" + " World")  # Output: "Hello World" (string concatenation)

# 2. Parametric polymorphism: This is when a function can be applied to arguments of any type, and the behavior of the function does not depend on the type of the arguments. For example, a function that takes a list as an argument and returns the length of the list can be applied to lists of any type.
def length_of_list(lst):
    return len(lst)

print(length_of_list([1, 2, 3]))  # Output: 3
print(length_of_list("Hello"))  # Output: 5

# 3. Subtype polymorphism: This is when a function can be applied to arguments of a specific type, and the behavior of the function depends on the type of the arguments. For example, a function that takes an object of a parent class as an argument can be applied to objects of any subclass of that parent class.
class Animal:
    def speak(self):
        pass



class Parent:
   def __init__(self):
       self.data = 'Parent data'

class Child(Parent):
   def __init__(self):
       super().__init__()
       self.data = 'Child data'

c = Child()
print(c.__dict__)  # {'data': 'Child data'}