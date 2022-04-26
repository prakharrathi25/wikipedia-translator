from pyexpat import model
from django.db import models
from wikipediaapi import Wikipedia

# Create your models here.
class Language(models.Model):
    """ This class holds the details of the allowed languages in the application.

    Fields:
        language_code: The language code of the language.
        language_name: The name of the language.
    """

    language_code = models.CharField(max_length=2)
    language_name = models.CharField(max_length=100)

    # Change the display to the language name 
    def __str__(self):
        return self.language_name


class Project(models.Model):
    """ Model which holds the details a project. A project in this application can be defined as 
        a translation task for a given pair of Wikipedia article and target language. 

    Fields:
        article_title: The title of the Wikipedia article.
        target_language: The target language of the article.
    """

    # Define the project model fields 
    article_title = models.CharField(max_length=100)
    target_language = models.ForeignKey(Language, on_delete=models.CASCADE)


    def get_article_summary(self): 
        """Function to get the summary of the article using the Wikipedia API 
            
            Returns:
                intro: The summary of the article or False if the title doesn't exist 
            """
        
        # Collect the search term 
        search_title = self.article_title

        # Check if the page exists
        page_details = Wikipedia().page(search_title)
        if page_details.exists():
            # Get the summary of the article
            intro = page_details.summary
            return intro

            print(intro) # testing 
        else: 
            return False

class Sentence(models.Model): 
    """ Model which holds the details of a sentence. A sentence is a part of a Wikipedia article which is tokenized.

    Fields:
        project_id: The ID of the project to which the sentence belongs 
        original_sentence: The original sentence tokenized from from the Wikipedia article.
        translated_sentence: The translated sentence in the target language.
    """

    # Define the sentence model fields 
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    original_sentence = models.CharField(max_length=5000)
    translated_sentence = models.CharField(max_length=5000)