# Sweetwater Design Project
## Overview (TL;DR)
This is the final project for the SDEV 220 class at Ivy Tech, created by Areiahna Cooks, Audrina Ortega, and Henry Barcalow.
The project creates a Django web app that allows musicians to make a record of their practice sessions.

## Communication
### Primary
- Discord: We have a Discord server set up and integrated with the Github repo. The server is automatically
  updated through a webhook whenever changes are made on the repo.
- Github Discussions: The Github repo was created under an organization (SDEV 220) so we could have access to
  Discussions. This allows us to easily reference the repo in our discussion posts and manage issues in the discussion.
- Github Projects: To keep track of our progress, we are using Github Projects as a Kanban board. This allows us
  to review what code we need to start, what code is in progress, and what code is finished.

### Secondary
- MyIvy Inbox: Sometimes we need to chat about what was missed in a class. The MyIvy inbox allows us to quickly
  send messages (similar to email) between students in the class.
- Zoom/Google Meet: Zoom and Google Meet would allow access to video calls and screen sharing, though Discord
  also allows this.
- Email: The trusty, antiquated standard of communication. If all else fails, sending an email probably will too.

## Project Plan
### Client
Our intended client for this project is Sweetwater Music. They are a business located in Fort Wayne, Indiana
providing musical instruments and equipment to musicians.

### Scope
Our project will be a web app built in Django. Users will be able to:
- create practice logs
- delete practice logs
- sort available practice logs by instrument, song, and date
- view practice logs created by other users

### Purpose
The project will allow users to see how much time they have spent practicing music and compare this with other users.
Given enough time, we could add a comment and voting system, allowing users to appreciate and congratulate others,
though this would come with its own host of issues: verification, content reporting, content filtering, post privacy,
spam detection and prevention, etc.

## Collaboration
### Repo
The repository is [https://github.com/SDEV-220/SDEV_220_Final_Project_Sweetwater](https://github.com/SDEV-220/SDEV_220_Final_Project_Sweetwater).
All team members can write and create pull requests. The main branch is protected (one review needed to push code).

### Roles
**Project Manager:** Henry Barcalow

**Front End:** Audrina Ortega, Areiahna Cooks

**Back End:** Audrina Ortega, Henry Barcalow

**Design:** Henry Barcalow, Areiahna Cooks

**Marketing/Pitching:** Audrina Ortega, Henry Barcalow

## Building
### Cloning the Repository
To clone the repository, run the following in git bash:

`git clone https://github.com/SDEV-220/SDEV_220_Final_Project_Sweetwater`

This will clone all the repository files into a new, local folder on your machine.

To install the required packages, first set up a virtual environment:

`python -m venv .venv` (or whatever your virtual environment name of choice is)

Then install the required packages after starting the environment:

`pip install -r requirements.txt`

### Setting Up a Local Environment
To set up the local environment, create an empty .env file in the directory `config/django`.

`touch config/django/.env`

Inside this .env file, you can create configuration for the ENVIRONMENT_TYPE, SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, and DEBUG environment variables. If you don't want to, it will automatically pull the test database from the repository. ENVIRONMENT_TYPE is `'config.django.local'`, `'config.django.production'`, or `'config.django.test'`. I'd recommend just leaving .env empty as the project has default values for development.

After setting up your environment, everything should be good to run. Default superuser is named `admin` with the password `local_admin`. Thus, _**nothing you commit to GitHub is secure**_. Do **NOT** commit personal information to the database.

### Helpful Links

Here is an example of how we will be organizing the data on the homepage.

[https://www.khanacademy.org/computer-programming/music-tracker/5599297716994048](https://www.khanacademy.org/computer-programming/music-tracker/5599297716994048)
