# a health-tracking application

(I dropped the course last period because of some emergencies, but for this period I will continue the development of this application.)

## This is a health-tracking website. It mainly consists of four pages: login/register, feed, diets, exercises

### Login/Register: 

There will first be some initial users data in the dataset. A visitor must first login to the website with username and password. if name or password is incorrect, the visitor cannot successfully log in. the visitor can choose to register a new user with name, password, gender, and current physical situation.

### Feed: 

The user will be able to see their user info, past diets, and past exercises data based on their past input by clicking on the button. the user can add new data by importing their new diet or exercise data. Their health overall score will be shown on the screen based on the calculation of data. 

### Diets:

There are two modules: one is the recommendation of diet based on the user's information on their past diet (some articles), and one is the course module that needs user's payment to unlock. They will not be implemented in details because of the limited amount of time.

### Exercises: 

There are two modules: one is the recommendation of exercise based on the user's information on their past diet (some articles), and one is the course module that needs user's payment to unlock. They will not be implemented in details because of the limited amount of time.

Progress report:

Interim 2:

The databases have been set up (users, user_exes, user_diets, exes, diets, dcourses, ecourses), and the modules have been divided. Tables exes and diets store the exercise types and diet types (but it has not yet been decided how diets should be implemented, should it be diets in general or it should be specific ingredients?), and the calories column in user_exes and user_diets are calculated based on the calories provided by the selected type * time length / kilogram, and the calculated calories should in turn be displayed on the user feed. The retrieving and updating functions have been mainly and roughtly specified in the users.py file.

There are five pages: index.html, login.html, register.html, diets.html, and exes.html. The details are not yet implemented.

The general structure has been roughtly listed in the app.py, but the details are not yet realized for most of the functions, and some are still missing there. 

the supplimentary files have been set (i.e. gitignore, .env). 

I encountered some problems with connecting to the database on the client side, and it takes me for more than five hours while the problem still remains unresolved. Therefore, it has not yet been tested on Heroku.
