from rest_framework import serializers

class JsonResponseSerializer(serializers.Serializer):
    answer = serializers.CharField()
    sources = serializers.ListField(child=serializers.CharField())

