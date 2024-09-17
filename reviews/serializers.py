from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manufacturers = Manufacturer.objects.filter(country=instance)
        representation["manufacturers"] = [
            {"name": manufacturer.name}
            for manufacturer in manufacturers
        ]

        return representation


class ManufacturerSerializer(serializers.ModelSerializer):

    count_comments = serializers.SerializerMethodField()
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ["name", "country", "count_comments", "cars"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        countries = Country.objects.filter(manufacturer=instance)
        representation["country"] = [
            {"name": country.name}
            for country in countries
        ]
        return representation

    def get_count_comments(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()

    def get_cars(self, obj):
        cars = Car.objects.filter(manufacturer=obj)
        return CarSerializer(cars, many=True).data



class CarSerializer(serializers.ModelSerializer):
    count_comments = serializers.SerializerMethodField()
    all_comments = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['name', 'manufacturer', 'year_of_release',
                  'year_of_completion', 'count_comments', 'all_comments']

    def get_count_comments(self, obj):
        return Comment.objects.filter(car=obj).count()

    def get_all_comments(self, obj):
        comments = Comment.objects.filter(car=obj)
        return CommentSerializer(comments, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        manufacturers = Manufacturer.objects.filter(car=instance)
        representation["manufacturer"] = [
            {"name": manufacturer.name}
            for manufacturer in manufacturers
        ]
        return representation

    def to_internal_value(self, data):
        resource_data = data['name']

        return super().to_internal_value(resource_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self, data):
        if len(data["comment"]) > 500:
            raise serializers.ValidationError("Не более 500 символов.")
        return data
