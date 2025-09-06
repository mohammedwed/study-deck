from django.db import models

# Create your models here.

class Deck(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE,related_name='cards')
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question[:30]}..."