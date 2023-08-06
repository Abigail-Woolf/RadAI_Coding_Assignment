# RadAI_Coding_Assignment
Build Food Truck API


## Description of the problem and solution
In this assignment, I built and api, using FastAPI, that searched a JSON file for different elements of the data. I built a single function to handle the "search by name of applicant," "search by status" and "search by street name." 

To use this API, download the python files and data. Next, install the proper tools by typing `pip install fastapi uvicorn geopy` into the command line. Next, also from the comman line, navigate to the folder with the python files and run `uvicorn main:app --reload`. This will return the URL that you can copy and paste into a browser to start searching the data.

Search by name of applicant: http://127.0.0.1:8000/search/?applicant="Enter_name_here"\

Search by applicant status: http://127.0.0.1:8000/search/?status="Enter_status_here"

Search by street name: http://127.0.0.1:8000/search/?address="Enter_street_name_here"

I combined all three of these search options into one function so that they can be used together or separately. By adding an ampersand, you can include all of these parameters into one search, or decide to use them on at a time. \

Here is an example of them being used all at once: http://127.0.0.1:8000/search/??applicant="Enter_name_here"&?status="Enter_status"&address="Enter_street_name"

I built a separate function to handle the location search by latitiude and longitude that returns the 5 nearest food trucks with a status that is APPROVED.

To include all statuses:
http://127.0.0.1:8000/nearest_coordinates/?latitude=YOUR_LATITUDE&longitude=YOUR_LONGITUDE&include_all=true

To filter by "APPROVED" statuses:
http://127.0.0.1:8000/nearest_coordinates/?latitude=YOUR_LATITUDE&longitude=YOUR_LONGITUDE


## Reasoning for technical/architectural decisions\
I chose to use FastAPI to build this program because it is what is used at RadAI and it has built-in API documentation. This is helpful to track the functionality of the API and I figured I should learn the tools that are required for this position. 

### What would you have done differently if you had spent more time on this?\

If I had more time to spend on this assignment, I would have hosted the JSON data on a database and connected that to the application. This would allow for more compartmentalization of the app program and for future expansion of the data. I think that it is a more practical approach to building APIs, especially when they handle much larger datasets. 


### What are the trade-offs you might have made?
### What are the things you left out?\

I left out some automated tests that I probably should have included. I know that at Rad AI, software engineers write automated tests in their code to make sure that errors are caught and corrected early. Admittedly, I am not too experienced writing automated tests, and I would have made a greater attempt at this had I been given more time.

### What are the problems with your implementation and how would you solve them if we had to scale the application to a large number of users?\
The main problem with my implementation is that it is all run locally and the data is read directly into the program. In a real setting, there will be exponentially more data to handle and not enough storage on a single machine. Also, without the use of a databse, other users would not be able to access the same data and could therefore not run the API.

### Please indicate the amount of time you spent on the project\
I spent about 8-9 hours on this assignment. I will admit that it took me a bit of trial and error before I was finally on the right track, but once I got everything situated and I had a finer understanding of the assignment, my pace picked up. 
