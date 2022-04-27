from pyexpat import model
from django.db import models
from wikipediaapi import Wikipedia
import pysbd

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
    is_tokenized = models.BooleanField(default=False)

    # Change the display to the article title
    def __str__(self):
        return self.article_title + '-' + str(self.id)


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
    translated_sentence = models.CharField(max_length=5000, default="No Translation Found (Add your translation here)")

    @staticmethod
    def get_sentences(project_id): 

        """Function to get the sentences associated with a project. 

        Returns:
            result (list): List of sentences associated with a project
        """

        result = []
        sentences = Sentence.objects.filter(project_id=project_id)
        for sentence in sentences: 
            result.append(sentence.original_sentence)
        
        return result


    @staticmethod
    def tokenize_intro_text(text, project): 
        """Function to tokenize the input text and save it into the Sentence model. 

            Args:
                text: The text to be tokenized. 

            Returns:
                tokens: The list of tokens in the text. 
            """

        # Tokenize the text and create a sentence for it 
        seg = pysbd.Segmenter(language="en", clean=True)
        tokenized_sentences = seg.segment(text)

        # Save the tokenized sentences into the Sentence model
        for sentence in tokenized_sentences:
            sentence_obj = Sentence(project_id=project, original_sentence=sentence)
            sentence_obj.save()

        return tokenized_sentences