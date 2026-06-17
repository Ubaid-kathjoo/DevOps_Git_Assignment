\# Flask Assignment 3 - Flask API and MongoDB Atlas Integration



\## Objective



The objective of this assignment is to learn Flask API development, JSON responses, frontend form handling, MongoDB Atlas integration, and error handling.



\---



\## Features Implemented



\### 1. Flask API Route



\* Created a Flask application.

\* Added an `/api` route.

\* Stored data in a backend JSON file (`data.json`).

\* Read data from the file and returned it as a JSON response.



\### 2. MongoDB Atlas Form Submission



\* Created a frontend form using HTML.

\* Collected user details (Name and Email).

\* Connected Flask application with MongoDB Atlas.

\* Inserted submitted data into MongoDB Atlas.

\* Redirected users to a success page after successful submission.

\* Displayed errors on the same page if submission failed.



\---



\## Technologies Used



\* Python 3

\* Flask

\* PyMongo

\* MongoDB Atlas

\* HTML

\* Git Bash

\* VS Code

\* GitHub



\---



\## Project Structure



Flask\_Assignment\_3/



├── app.py



├── data.json



├── requirements.txt



├── templates/



│ ├── index.html



│ └── success.html



├── screenshots/



└── README.md



\---



\## Installation



Create virtual environment:



python -m venv venv



Activate virtual environment:



source venv/Scripts/activate



Install dependencies:



pip install flask pymongo dnspython



Run application:



python app.py



\---



\## Author



Ubaid Kathjoo



