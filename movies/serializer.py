from rest_framework import serializers
from movies.models import Movie, Rating_choices

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(choices=Rating_choices.choices, default=Rating_choices.G, required=False,)
    synopsis = serializers.CharField(required=False)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)