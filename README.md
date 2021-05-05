
[![Build Status](https://travis-ci.com/cybsafe/phishtray.svg?branch=master)](https://travis-ci.com/cybsafe/phishtray)
[![Coverage Status](https://coveralls.io/repos/github/cybsafe/phishtray/badge.svg?branch=master)](https://coveralls.io/github/cybsafe/phishtray?branch=master)

# This Files only run in Windows OS.


# Phishtray Installation


## Prerequisites

1. Install `docker` - https://docs.docker.com/install/
2. Copy the following lines to your `hosts` file: You can find `hosts` file in `C:\Windows\System32\drivers\etc`. If you can not find `hosts` file then search in C drive `hosts`.

        # Phishtray
        127.0.0.1               phishtray.local

3. Create two env files in the frontend folder. One called `.env.development.local` and the other called `.env.local`. Then you should have to Write/Copy and Paste below content in both the files.  

        REACT_APP_HOST_BACKEND=http://phishtray.local:9000
        REACT_APP_HOST_FRONTEND=http://phishtray.local:3000
        REACT_APP_NAME=Emtray


## Install directory in your file. 
0. Open Terminal in Visual Studio Code. 
1. Go into the local docker directory `cd docker/local`
2. Build and bring up the images running `docker-compose up -d --build`
3. Bash in to the django container using `docker-compose exec django bash`  
then create a superuser `py3 manage.py createsuperuser --email your@email.here`
4. Run the static files command `py3 manage.py collectstatic`

# Run the project


0. make sure you've completed the prereqs
1. Navigate to http://phishtray.local:9000/admin and create an Exercise with emails
2. Copy the exercise UUID
3. In your local terminal, from the phishtray folder, `cd frontend` and `yarn start`
4. Navigate to http://phishtray.local:3000/welcome/<exercise:uuid>/ to start the exercise

# Extra steps Only for testing.

## Running tests
Run bash inside the django container using `docker-compose exec django bash`
then run the following test command `py3 manage.py test`

## Running Django Server
1. **Normal** - To run the server normally `make django-run`
2. **Debug** - To run the server in debug mode `make django-debug` (This will allow a tool like PyCharm to actually start the web server within the container)


## Working Within The Container
Within the container you should use Python 3 which can be called via `py3` or `python3.6` commands, `python` refers to Python 2.7 which is the system default. 

## If you need any help contact me or put comment.
