from rest_framework import serializers
from .models import Deck,Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"

class DeckSerializer(serializers.ModelSerializer):
    cards = FlashcardSerializer(many=True,read_only=True)

    class Meta:
        model = Deck
        fields = "__all__"
