# Online classes application

This application is a simple simulation of online courses where you can create a class that is made of teacher and course, this application will allow you to create a course and add an instructor, after that you can create a class by selecting one of the courses and instructor for this course.
this is a simple application made only for learning purposes to demonstrate my understanding of the FSND course.

## Test Live Aaplication
- this application is hosted in [https://capstone-project-fsrb.herokuapp.com], if you click this link you will see 404 that's because this application has no home page you can test GET endpoints where you can list all the tables data as a public user, you can list three tables using these endpoints
[https://capstone-project-fsrb.herokuapp.com/Classes]
[https://capstone-project-fsrb.herokuapp.com/Teachers]
[https://capstone-project-fsrb.herokuapp.com/Courses]

- for other endpoints where you can add data and delete or edit data, you need to log in as either administrator or administer-assistant and to log in, you can go to [https://capstoner.us.auth0.com/authorize?audience=onclasses&response_type=token&client_id=grDrK6yNQ3q3SX9ogWr0SieC3Rp1zscy&redirect_uri=https://capstone-project-fsrb.herokuapp.com]

 **the tokens for each user will be provided when submitting the project, and you can test it using postman collection to test other endpoints**

- to logou from the application go to this link [https://capstoner.us.auth0.com/v2/logout?client_id=grDrK6yNQ3q3SX9ogWr0SieC3Rp1zscy&returnTo=https://capstone-project-fsrb.herokuapp.com/logout]


## Getting Started
this application is python base with the use of Flask platform, follow the instructions to run the application in **local environment**.

#### Python 3.7
 install the latest version of python.

#### Installing Dependencies
 you can install all the required packages using the requirements text file, once you create your virtual environment for this project you can add this command using bash to install dependencies to your virtual environment.

 ```bash
pip install -r requirements.txt
```
##### Key Dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

### run the server
within your created virtual environment in the project directory and after installing the dependencies, execute these commands in bash:

```bash
export FLASK_APP=app.py
flask run --reload
```
### application components
There are 8 endpoints for this application each of serving a function and for specific users.
**Users**
- administrator: can perform all task and have access to all endpoints, which are
_add course_
_add teacher_
 _add class_
 _edir class_
 _remove class_
- administrator - assistant: can perform only 3 tasks, means he has permission for 3 endpoints, which are
 _add class_
 _edir class_
 _remove class_

- the GET endpoints are accessible by all users include public users.
---------------------------------------------------------------------

**endpoint**

- GET '/Teachers' :
  display all the teachers in the database.
  Request Arguments: None
  Returns: return a JSON object that contains all the teachers and success status indicate the success of the request.

- GET '/Courses' :
  display all the courses in the database.
  Request Arguments: None
  Returns: return a JSON object that contains all the courses and success status indicate the success of the request.

- GET '/Classes' :
  display all the classes in the database.
  Request Arguments: None
  Returns: return a JSON object that contains all the classes and success status indicate the success of the request.

- POST '/Teachers':
 add a new teacher to the database
 Request Arguments: JSON contains the teacher info, name, and email phone and a brief bio with an image of the instructor.
 Returns: a JSON object that returns the new teacher, and status that indicates the success of the post request.


- POST '/Courses':
 add a new course to the database
 Request Arguments: JSON contains the Courses info, name, and brief description with an image of the course.
 Returns: a JSON object that returns the new course, and status that indicates the success of the post request.

- POST '/Classes':
 add new classes to the database
 Request Arguments: JSON contains the class info, name and start date, and course id, teacher id.
 Returns: a JSON object that returns the new class, and status that indicates the success of the post request.

- DELETE '/Classes/classes_id':
 delete a selected class from the database
 Request Arguments: an integer that represents the classes_id.
 Returns: a JSON that returns the id of deleted class, and status that indicates the success of the deletion request.


- PATCH '/Classes/classes_id':
 edit the selected class from the database
 Request Arguments: an integer that represents the classes_id.
 Returns: JSON that returns the id of the selected class, and status that indicates the success of the patch request.

 **Database**
there are three tables for this application, teachers and courses and classes:

- teachers: information of the instructor who will give the course.
_name_
_email_
_image-link_
_phone_
_profile_

- courses: information about the available course.
_name_
_description_
_image-link_
_duration_

- classes: contain course and the instructor who will give the courses.
_name_
_start-time_
_teacher-id_
_course-id_

**Error Handling**
-The errors weil be return as JSON in this Format
{  "success": False,
   "error": code of the error,
   "message": "the message of the error"
}
 _5_ types of errors will be handeld
 -404 :Not Found
 -422 :Unprocessable
 -403 :Forbidden
 -400 Bad Request
 -500 Internal Server Error

### Testing
To run the tests ,run
```
dropdb capstoneDB_test
createdb capstoneDB_test
python test.py