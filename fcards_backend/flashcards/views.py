from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from flashcards import models, serializers


class DeckViewSet(viewsets.ModelViewSet):
    queryset = models.Deck.objects.all()
    serializer_class = serializers.DeckSerializer



class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = models.Flashcard.objects.all()
    serializer_class = serializers.FlashcardSerializer