# AirBnB clone - The console

# Concepts
For this project, we expect you to look at these concepts:

* [Python packages](https://intranet.alxswe.com/concepts/66)
* [AirBnB clone](https://intranet.alxswe.com/concepts/74)

# Background Context
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page

# Hbnb
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
                                                                                         not all the features would be implmented, only some of them to cover all fundamental concepts of the higher level programming track.

* First step:  Write a command interpreter to manage your AirBnB objects.                This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-e
nd integration…

# What’s a command interpreter?                                                          A command interpreter is a program that executes other programs, but in our case ours is
to:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# Description of cli
Example on how to start, how to use.                                                     
Execution                                                                                Your shell should work like this in interactive mode:                                    
* $ ./console.py
* (hbnb) help

* Documented commands (type help <topic>):
* ========================================
* EOF  help  quit

* (hbnb)
* (hbnb)
* (hbnb) quit
* $

 But also in non-interactive mode: (like the Shell project in C)

* $ echo "help" | ./console.py
* (hbnb)

* Documented commands (type help <topic>):
* ========================================
* EOF  help  quit
* (hbnb)
* $
* $ cat test_help
* help
* $
* $ cat test_help | ./console.py
* (hbnb)

* Documented commands (type help <topic>):
* ========================================
* EOF  help  quit
* (hbnb)
* $

....Have fun

