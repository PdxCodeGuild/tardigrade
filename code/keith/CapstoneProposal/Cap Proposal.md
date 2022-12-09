## Keith Townsend
# Capstone Proposal


- Your proposal must set specific and attainable goals
- Your proposal must cover all major topics we've covered
- Your proposal must include the sections below

## Project Overview
Major Features: Login for users, Calender to display and log data, input gigs/rehearsals
log venue details. (load in time, lodging/food, point of contact, ect.)

Secondary Features: Possible link with google calender, easy on the eyes UI, maybe pictures of venues (img url) when you click on the date.  

## Functionality
- First the user will be brought to a log in process  

- Second thing user sees is a calender, when they click on a date/cell then the input fields will show for that day/night.

- After inputing the gig/rehearsal details the user will be brought back to calnder view and maybe that could be color coded at that point to deonote on/off day and gig or rehearsal

- My thought is that maybe once a show has finished to user can either dismiss it or log some data such as audience number/tickets sold, merch sales, general comments.

- My thought at this point is to include some functionality to maybe share this information via text or maybe even linking google calender to share that way.

- Maybe eventually one day it would be nice to figure out how to share with groups (much like slack) inside of the app.



<!-- -  7/12 finish calendar, make nav bar for login/logout, protect all the routes, add  -->
<!-- 
-  7/14 fix my redirecting problems for the user login process.  I want to go from login to the about.html then to navigate to the calendar with the nav bar. CHECK!!!!! -->

<!-- -7/17 make login in success or failure, -->

<!-- 7/18 look into or ask about color palets -->

<!-- 7/19 make the login and register new user bars shorter, make the users info be automatically asgined to there acc. when entering a new event. pics of stage stuff like mics and amps for the event add page.
Welcome user after they login. -->

<!-- 7/21 figure out where the form is in html so you can style it slightly, adding breakpoints for some of the pictures. -->

<!-- 7/26 Add a nav button to get to "quick view" -->

<!-- 7/27 render users events for the month/week in the about page(use bootstrap cards, write another function for the view?). Also make it so you don't have to to fill out all fields on new events to submit. -->

<!-- 8/1 maybe add a footer? -->

<!-- 8/2 figure out how to make description box smaller in new event form. -->

<!-- 8/2 figure out how to arrange bootsrap cards and make about.html image take up the whole screen. -->

8/3 display which user is logged in up in the nav bar? figure out how to override
standarize spacing and tabbing in css file and add comments. Later task, download the photos into schedule.app photos. Comments everywhere!!! change Form color outline.


## Data Model

User: name, password

event type: Gig or Rehearsal

   GIGS                                 
-distance to gig
-address
-contact person phone/email
-load in time
-downbeat time
-length of set
-rate of pay
-lodging

 REHEARSALS
- time
- location


## Schedule

Week 1:Get the app set up as far as Django, HTML, make models, create user profile.


Week 2: Create the forms for the inputs, make sure forms and models are interacting correctly, hopefully link google calender, testing and debugging


Week 3: finish details and stylise, more testing and debugging I'm betting.


Week 4: possible time to add features tweak the user experience aft




