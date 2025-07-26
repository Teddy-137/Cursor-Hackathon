from rest_framework import serializers
from .models import Condition, Symptom


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = [
            "id",
            "name",
            "description",
            "severity_level",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class SymptomSerializer(serializers.ModelSerializer):
    conditions = ConditionSerializer(many=True, read_only=True)

    class Meta:
        model = Symptom
        fields = [
            "id",
            "name",
            "description",
            "conditions",
            "severity_level",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
