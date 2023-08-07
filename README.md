# RadAI_Coding_Assignment
Build Food Truck API


## _Description of the problem and solution_
In this assignment, I built and api, using FastAPI, that searched a JSON file for inforation pertaining to food truck applicantions in SF. I built a single function to handle the "search by name of applicant," "search by status of application" and "search by street name." 

To use this API, download the python files and JSON data, applicants.JSON. Next, install the proper tools by typing `pip install fastapi uvicorn geopy` into the command line. Next, also from the command line, navigate to the folder with the python files and run `uvicorn main:app --reload`. This will return the URL that you can copy and paste into a browser to start searching the data.

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


## _Reasoning for technical/architectural decisions_
I chose to use FastAPI to build this program because it is what is used at RadAI and it has built-in API documentation, that can be accessed at this URL: http://127.0.0.1:8000/docs
This is helpful to track the functionality of the API and I figured I should learn the tools that may be required for this position. I attempted to make the Dockerfile to contain all of the files for this assignment into one runnable container, but I ran into trouble with the `docker build` command. Given more time, I could have resolved this issue, but I decided to move forward due to time constraints. 

## _Critique Section_

### What would you have done differently if you had spent more time on this?

If I had more time to spend on this assignment, I would have hosted the JSON data on a database and connected that to the application. This would allow for more compartmentalization of the program and for future expansion of the data. I think that it is a more practical approach to building APIs, especially when they handle much larger datasets. 

### What are the trade-offs you might have made?

I am not sure if I fully understand this question, but a trade off I can think of is using geopy instead of a more robust locational data API like Google Maps. I felt like, for me, it was mmuch simpler to use geopy than go through the steps of retreiving an API key from the Google Maps API.

### What are the things you left out?

I left out some automated tests that I probably should have included. I know that at Rad AI, software engineers write automated tests in their code to make sure that errors are caught and corrected early. Admittedly, I am not too experienced writing automated tests, and I would have made a greater attempt at this had I been given more time. Despite my current inexperience, I actively work hard to learn and become up-to-speed with the methods required for this position at RadAI.

### What are the problems with your implementation and how would you solve them if we had to scale the application to a large number of users?

The main problem with my implementation is that it is all run locally and the data is read directly into the program. In a real setting, there will be exponentially more data to handle and not enough storage on a single machine. Also, without the use of a databse, other users would not be able to access the same data and could therefore not run the API.

### Please indicate the amount of time you spent on the project

I spent about 8-9 hours on this assignment. I will admit that it took me a bit of trial and error before I was finally on the right track, but once I got everything situated and I had a finer understanding of the assignment, my pace picked up. 

### Final Commentary

Because I am a little out of practice (my current job doesn't require these skills) I experienced a lot of trial and error during the beginning or this project. I really enjoyed diving back into coding, however, and have confirmed that this is what I want to do in my next role. I am craving a position where each day is a challenge to be approached with strategy and resourcefullness and craving a company with a bright, lasting, and clear future for growth. Through this assignment, I believe that I proved my ability to pick up new skills and concepts and apply them in a practical way. 

Not only is this the type of day-to-day that I hope to find for myself, but RadAI is also the type of company I want to work for for a myriad of reasons. Healthtech or health software is an inevitable advancement that the healthcare industry will experience and I want to be at the forefront of this transition. This is the sector/industry where I want to be and I can garauntee that I will put in all the effort needed to see change that needs to happen and be successful. Laslty, I want to acknowledge that in today's job landscape, it is extremely difficult to sitringuish between the hundres od qualified applicants that trickle in to RadAI. What sets me apart, however, is that I have an undergraduate biology degree from a prestigious liberal arts school, whereas most software engineers likely have CS degrees. I think my biology/pre-med background gives me a unique angle though which I see software problems in the health sector. Via my master from UC Berkeley, I was able to hone in on my passion for making healthcare more equitable and accessible by leveraging data analyics, ML, and software. Unline other applicants, I am earl(ier) career and have the time and bandwidth for the start-up hustle. I am super eager and excited about growing at a company like RadAI. I don't see RadAI as a stepping stone in my career, but the destination (sorry for the cliche, but it is true). 
