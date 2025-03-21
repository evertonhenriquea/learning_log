from django.db import models

class Topic(models.Model):
    #Assunto que o usuario está aprendendo.
    text = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        #Retorna uma string do do modelo.
        return self.text
    

