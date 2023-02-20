Özön, Derin, 22111170

Thura, Aw, 22108220

Project for Assistance Systems

Günther the library bot

https://mygit.th-deg.de/diminished7/sas-voice-assistant

# Project Description
Günther is a chat bot designed to help you with the process of finding a book from the libray database of THD.
More info about the design and documentation can be found in the [Wiki](https://mygit.th-deg.de/diminished7/sas-voice-assistant/-/wikis/home)

# Installation
	pip install -r requirements.txt

# Usage
Running the `main.py` file will open a local webserver at http://localhost:5000/ and spawn the rasa backend as a subprocess. This might take a minute to run so it is a good oppurtunity to grab another cup of coffee. The message `Rasa server is up and running` indicates that everything is fine and ready to use. <br> NOTICE: The program might not run at python installations higher than version 3.9. <br> NOTICE: The backend might not work on some installations of windows due to CORS issues. I recorded a [video](https://youtu.be/F-lMMT_KItg) of the frontend just in case it doesnt run because of browser security precautions. Also you can run it in the terminal by running `rasa run actions` first, then running `rasa shell` in a seperate terminal.

# Implementation of the Exercises

## Implemented
	• For the planned application, answer the questions about “the right fit”
	• Create 1 system persona and 3 user personas.
	• Find Use cases for your application and document them with a diagram and a description for each.
	• Identify 5 critical user journeys and document them.
	• Document the technical prerequisites for the project.
	• Create several sample dialogs according to the procedure described. Document this in your project documentation
	• Starting with one dialog, convert your dialogs into a flow!

## Not Implemented
	• None

# Work done

Aw Thura - Cleaning the data and creating the rasa model <br>
Derin Ozon - Creating the frontend and connecting it to the model