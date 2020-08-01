# Python & Sense HAT programming
``` 
RMIT University Vietnam
Course: COSC2790 Programming Internet of Things
Semester: 2020A
Assessment: Assessment 1: Python & Sense HAT programming
Student Name - ID: 
    1. Nguyen Quoc Cuong - s3748840
    2. Nguyen Thi Thuy Tien - s3757934
```
## Getting Started

This is a small IoT application working on Raspberry Pi and Sense HAT using Python language to serve a number of different tasks and requirements. During the development process, a variety of technologies and tools have been applied. Following is the description of the project repository.

## Repo status

This respository is private and shared between 2 contributors as stated above.

### Branches

There are 4 different branches beside the default master including emoji, context, bluetooth and game. Contributors are using different branches to develop the corresponding solutions. 

### Activities

This project is being developed for around 4 weeks. Git and git hub have been used from the beginning of the project to manage the work and help contributors to collaborate with each other. 

Contributors pull code from the appropriate branch everytime to continue working on the solution. Commit and push activities happen continuously after some new parts of the solution are coded serveral times per week or per day.

Finalized solution is merged to master branch after being checked for the first half of the cycle. 
For the second half of the cycle when context solution is being finalized, it also acts as a master branch when providing a new structurized format for all the project's modules, later solutions are checked and merged to this context branch. 

## Solutions

Overal, Raspberry Pi 3 and 4 have been used to develop and test the solutions. The application is designed and developed based on Object-oriented programming (OOP) with different classes and objects using Python 3.5 and Visual Studio Code IDE. The team also follow PEP 8 for code styling. Morever, GitHub is used as the version control system for the whole project. 

Besides working on functional requirements, the team also put effort in developing error handling functions to handle different types of error with files, databases, api, etc ... All input from files and user are checked prior using.

### Emoji

3 different Emojis are designed with types and lots of colors. They are displayed in Sense HAT one by one with 3 seconds interval. The team has also put effort in making the Emoji animated during the 3 displaying seconds.

### Context 

A script is developed to run automatically every minute, get the current environment context (time, temperature, humidity) and log the record in to the SQLite database. When working with database commands, SQL Injection is avoided by using parameters.

The recorded contexts are evaluated accordingly with the user preferences in the config file. The evaluated result is used to:
    Alert user in terms of uncomfortable (only 1 notification per day, reset at the end of the day) and dangerous (everytime) situation via PushBulet API. 
    If the weather is good all day, then a last message will be sent at the end of the day to inform the average temperature and humidity of that day.
    Displayed in the Sense HAT with appropriate colors for each status. 

Another script is used to manually get the last context record from the database and save the record with its corressponding status and message in a csv file. The file has a default name but can be changed by user as well. 

When Pi boots, a script is scheduled to run automatically to open RESTful APIs connection allowing user to perform 3 methods:
    1. GET: retrieve the latest record in JSON format
    2. POST: upload a new record to database with current time
    3. PUT: update the latest record in database
A test script is also prepared to test the mentioned APIs with pass and fail scenarios.

### Bluetooth



### Game



## Acknowledgments

[1] "get_smooth", calibrating function is taken from lecutre's week 3 code archive. 

