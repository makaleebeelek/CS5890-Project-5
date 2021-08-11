# CS5890-Project-5
## A note about SparkNLP
We spent multiple days trying to get the Healthcare SparkNLP from John Snow Labs to work. Each group member ran into errors trying to follow the instructions provided by John Snow Labs and could not find any way to get it to work. Instead of using SparkNLP, we created our own functions and work arounds to be able to complete this project.


## What you need to run this project:
1. python
2. django
3. re
4. scispacy
5. spacy
6. pandas
7. numpy

## How to run (assuming you have python):
1. Make sure Django is installed. Best way to check is to run `$ python -m django --version`. If it gives you an error, you do not have django installed. Run `$ python -m pip install django` to install django
2. Change your directory to the location of the project. Make sure you are in the same folder as manage.py. Example: `$ cd .../FinalProject/FinalProject/`
3. Migrate the project by running `$ python manage.py migrate`
4. Run the server locally by running `$ python manage.py runserver`
5. The output will give you an address to go to, open any browser and paste that address into the search bar
6. Tada! It should work!

## Where specific code is located:
Most of the code is located in the `.../relevantCode` directory. The code for the HTML, CSS, and Django is all located in the `.../FinalProject/` directory.
* The sentiment analysis and topic modeling is located in `.../relevantCode/group_5_Project-2.ipynb`
* The highlight function is located in `.../relevantCode/highlight_function.ipynb`
* The regex for redacted personal information is located in `.../relevantCode/RemoveNamePattern.ipynb`
* The html is located in `.../FinalProject/Project5/templates/Project5/index.html`
* The css is located in `.../FinalProject/Project5/static/css/style.css`
* The code applied to the website to make the buttons, textbox, highlighting on the webpage function is in `.../FinalProject/Project5/views.py`
* We could not upload the entire MIMIC-III files, but portions of them can be found at `.../FinalProject/Project5/NOTEEVENTS-0.csv`, `.../FinalProject/Project5/NOTEEVENTS-1.csv`, `.../FinalProject/Project5/NOTEEVENTS-2.csv`
