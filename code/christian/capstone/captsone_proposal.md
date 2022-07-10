# Capstone Proposal - Eberhardt
## _Project Name: Anger Iceberg 🧊_
---
## Project Overview
What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?

According to a 2019 poll from [NPR]:

>84% of people surveyed said Americans are angrier today 
>compared with a generation ago, according to the latest 
>NPR-IBM Watson Health poll. When asked about their own 
>feelings, 42% of those polled said they were angrier in
>the past year than they had been further back in time

Although anger is commonly experienced by many Americans it is a complicated emotion. For instance, anger is not a primary emotion... instead, it is a secondary emotion that is triggered by **OTHER** emotions. Although many Americans desire to deal with their anger, often by dealing with anger itself, they fail to look deeper at the true cause of their emotional distress. The problem is one of situational awareness which can be addressed through visuals, adivce (quotes), and an opportunity to apply that advice to every day life to better balance emotions. 

Libraries/Frameworks:

The application will be built on a Django Framework. It remains undetermined what libraries will be incorporated. 

Major Features:
- A Login Page
- An interactive image that educates users on the Anger Iceberg Model
- Clickable emotions that generate advice which best helps address that emotion
- The ability to star/favorite advice that is helpful for later review

## Functionality

Upon starting the application, the user will be greeted with a message that says “Anger is one letter away from…” Upon hovering over the text, an event listener will trigger a JS alert that reads: “DANGER\n Are you ready to look below the surface?\n [Yes]  [No]. Clicking Yes will redirect the user to a login page that allows for account creation. Signing in will then direct the user to a visualization of an anger model which illustrates that emotions such as exhaustion, fear, depression, and many others, are what triggers the emotion of anger. 

Each emotion is clickable and will redirect the member to a page with 3-4 quotes that help a member process that emotion. A Boolean value will be used to determine whether a quote is helpful. Helpful quotes will be saved under the users profile where they can recall/review them in a time of need. The NAVBAR will allow users to rotate between the anger iceberg (to select more advice) and their profile which displays advice they’ve saved. 

## Data Model

User:
-Username = models.CharField()
-Password = models.CharField()

Quotes:
-Text= models.CharField()
-Author= models.CharField()
-Hepful= models.BooleanField()

## Schedule
July 8th: Take initial steps in Django to startproject and create app
July 11th: Successfully pull data from the Quotes API
July 11-15: Review Project with Instructor to seek insight on how best to manage the project
July 18: Produce a solution to pulling quotes that correspond to each emotion
July 22: Recreate illustration of Iceberg Model in HTML & CSS
July 25: Check in with instructor to discuss progress and workthrough lingering development issues
Aug 5 - ____: The Air Force is pulling me back on full-time orders for two months. Regardless, free time will be used to code independent projects, build resume, and apply for work. 