![wikipedia-translator](https://socialify.git.ci/prakharrathi25/wikipedia-translator/image?descriptionEditable=Translate%20Wikipedia%20Article%20content&font=Bitter&language=1&name=1&owner=1&pattern=Charlie%20Brown&stargazers=1&theme=Light)

# Wikipedia Translation Application

This application allows a user to enter an article title on Wikipedia. The application collects article data from Wikipedia and lets the users translate the article content into other languages. The application is built using Django and HTML Templates. The application is hosted on Python Anywhere. 

Check it out [here](http://prakharrathi25.pythonanywhere.com/)

##  How to Run Locally 

* Clone the repository 

`git clone https://github.com/prakharrathi25/wikipedia-translator.git` 

* Install dependencies

`pip install -r requirements.txt`

* Run the application

`python manage.py runserver`

## Application Flow 

1. User enters the article title in the search bar on the project page along with the target language. 
2. The application fetches the article data from Wikipedia and displays the article content in the translation page.
3. The user can translate the article content into other languages.
4. The user can save the translated article content in the translation page.

## Application Demo

https://user-images.githubusercontent.com/38958532/165505012-c7a00c96-4d62-4c96-8b2f-36e2a592ad8b.mp4


## Application Testing Credentials 

You can use these credentials to test the application locally. Currently, I have not given the feature to create new users so you need to use the credentials of an existing user.

**Superadmin credentials** 
- **username** - admin 
- **password** - admin

**Manager Credentials**
- **username** - manager
- **password** - not-man-123

**Annotator Credentials** 
- **username** - annotator 
- **password** - not-annot-123