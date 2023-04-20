from rest_framework import serializers
from movies.models import Movie, Rating_choices, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(choices=Rating_choices.choices, default=Rating_choices.G, required=False,)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj):
        return obj.title.title

    def get_buyed_by(self, obj):
        return obj.buyed_by.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)