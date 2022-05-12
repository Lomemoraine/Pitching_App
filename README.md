# Raine Pitching App
## Author

* Lorraine Chepkemoi
## Contact info
* slack profile[Lorraine Chepkemoi]

## Description

An application that allows users to post one minute pitches. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on thems

## User Stories

* A user would like to see the pitches other people have posted..
* A user would like to vote on the pitch they liked and give it a downvote or upvote in the application.
* A user would like to be signed in for me to leave a comment.
* A user would like to receive a welcoming email once I sign up.
* A user would like to comment on the different pitches and leave feedback.
* A user would like to receive a welcoming email once I sign up
* A user would like to submit a pitch in any category.
* A user would like to view the different categories



## Setup instruction

#### Ensure you have the following installed on your machine 
* python3.7 or later 
* flask
* pip
* Flask_Script
* virtual enviroment
* Postgress database(SQLALchemy)
#### Dependencies

* All dependencies are listed in the requirements.txt file

#### Clone

* git clone ``````
* cd Pitching_App
* Open in your preferred IDE(Vs Code ,Pycharm,atom)
### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:
        $ chmod +x start.sh
        $ ./start.sh

## Behaviour Driven Development
* The user sees a landing page with two buttons to  make a pitch and another one to view existing pitches.
* A user can view pages that have been made in various categories.
* A logged in user is able to like the pitches they love only<strong> ONCE</strong>.
* A logged in user can dislike a pitch they do not like only<strong> ONCE</strong>
* A logged in user can view comments made on each pitch and leave their comments as well.
* On the landing page also,a user sees the sign in link on the navigation bar.
* A user signs into the system by clicking the sign in nav link ,if they have no account yet,they will   have an option to sign up
* On clicking the pitch here button,the users creates a pitch if they are logged in,if not,they  will be asked to login first.
* A logged in user is able to see their profile through the profile nav link.
* The profile page allows users to upload their favourite profile picture and edit their bio.
* A user is able to see the pitches they have made in their profile page.



## Test Driven Development
* All the tests can be runned by typing the following command on the terminal
       $Python3 manage.py test
## Technologies Used
* python3.9
* Flask 
* Css and Boostrap
* jinja templates
* PostgreSQL
## Known Bugs
* There are no known bugs yet
## License
* *MIT License:*
.