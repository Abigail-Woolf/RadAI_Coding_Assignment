# RadAI_Coding_Assignment
Build Food Truck API


## Description of the problem and solution
In this assignment, I built and api, using FastAPI, that searched a JSON file for different elements of the data. I built a single function to handle the "search by name of applicant," "search by status" and "search by street name." 

To use this API, download the python files and data. Next, install the proper tools by typing `pip install fastapi uvicorn geopy` into the command line. Next, also from the comman line, navigate to the folder with the python files and run `uvicorn main:app --reload`. This will return the URL that you can copy and paste into a browser to start searching the data.

Search by name of applicant: http://127.0.0.1:8000/search/?applicant="Enter_name_here"
Search by applicant status: http://127.0.0.1:8000/search/?status="Enter_status_here"
Search by street name: http://127.0.0.1:8000/search/?address="Enter_street_name_here"

I combined all three of these search options into one function so that they can be used together or separately. By adding an ampersand, you can include all of these parameters into one search, or decide to use them on at a time. 
Here is an example of them being used all at once: http://127.0.0.1:8000/search/??applicant="Enter_name_here"&?status="Enter_status"&address="Enter_street_name"

I built a separate function to handle the location search by latitiude and longitude that returns the 5 nearest food trucks with a status that is APPROVED.

To include all statuses:
http://127.0.0.1:8000/nearest_coordinates/?latitude=YOUR_LATITUDE&longitude=YOUR_LONGITUDE&include_all=true

To filter by "APPROVED" statuses:
http://127.0.0.1:8000/nearest_coordinates/?latitude=YOUR_LATITUDE&longitude=YOUR_LONGITUDE

Search by name of applicant. Include optional filter on "Status" field.
Search by street name. The user should be able to type just part of the address. Example: Searching for "SAN" should return food trucks on "SANSOME ST"
Given a latitude and longitude, the API should return the 5 nearest food trucks. By default, this should only return food trucks with status "APPROVED", but the user should be able to override this and search for all statuses.
You can use any external services to help with this (e.g. Google Maps API).
For the programming languages allowed we would prefer that you use the one that was discussed with the recruiter or the hiring manager. So make sure that this is clear before you start this challenge, please :)
We write automated tests and we would like you to do so as well.


## Reasoning for technical/architectural decisions

What would you have done differently if you had spent more time on this?
What are the trade-offs you might have made?
What are the things you left out?
What are the problems with your implementation and how would you solve them if we had to scale the application to a large number of users?
Please document any steps necessary to run your solution and your tests.
Please indicate the amount of time you spent on the project
