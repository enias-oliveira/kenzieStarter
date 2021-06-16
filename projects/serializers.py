from rest_framework import serializers
from .models import Project

from categories.serializers import SubcategorySerializer
from locations.serializers import LocationSerializer
from creators.serializers import CreatorSerializer


class ProjectSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()
    location = LocationSerializer()
    creator = CreatorSerializer()

    class Meta:
        model = Project
        fields = "__all__"
