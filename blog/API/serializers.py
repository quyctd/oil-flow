from rest_framework import serializers

from blog import models

class QuestionSerializer(serializers.ModelSerializer):
    """A Serializer for Question objects."""

    class Meta:
        model = models.Question
        fields = '__all__'

