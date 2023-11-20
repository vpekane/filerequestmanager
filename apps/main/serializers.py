from rest_framework import serializers


class fileSerializer(serializers.Serializer):
    files = serializers.CharField()
    # id = serializers.CharField(max_length=50)
    # title = serializers.CharField(max_length=50)