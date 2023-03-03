# kuromiSurvey
The goal of this application is to automate the calculation of average survey results from given users. The user will input the scores in a specified age range, in this case 16-24, and the program will return the average score for each age.
This project uses a variety of APIs from the google cloud platform. We are using the gspread and google auth libraries to access our google sheet https://docs.google.com/spreadsheets/d/1tw2SX4CEhTe-73U9Lv_Fyw3-vyfEaaLXzJDSxz8v9Bw/edit?usp=sharing to view and edit data. 

On the google cloud platform we start by creating a new project and installing our previously mentioned libraries, once we have these enabled we can create a credentials file, creds.json, by adding a key to our google cloud project under the "Service accounts" tab. We also receive a service account email that we can share our sheet with so that we have access to it from within our application. 
# Deployment
This application was deployed on heroku by creating a new app and linking it to our github repository. We then added our creds.json file to settings to maintain our privacy, we also added buildpacks we need to run the application, python and node.js. The app was then manually deployed. 

The deployed build can be found at https://kuromisurvey.herokuapp.com/