from rest_framework import serializers

from app.restaurant.models import Food


class FoodSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    kitchen = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Food
        exclude = ('id', 'in_menu')