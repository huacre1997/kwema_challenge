from rest_framework import serializers


class BacteriaSerializer(serializers.Serializer):
    days = serializers.IntegerField(required=True)
    maturation_period = serializers.IntegerField(required=True)
    life_expectancy = serializers.IntegerField(required=True)
    reproduction_rate = serializers.IntegerField(required=True)

    def validate_days(self, attrs):
        if attrs < 0:
            raise serializers.ValidationError('days cannot be negative')
        return attrs
    def validate_maturation_period(self, attrs):
        if attrs < 0:
            raise serializers.ValidationError('maturation_period cannot be negative')
        return attrs
    def validate_life_expectancy(self, attrs):
        if attrs < 0:
            raise serializers.ValidationError('life_expectancy cannot be negative')
        return attrs
    def validate_reproduction_rate(self, attrs):
        if attrs < 0:
            raise serializers.ValidationError('reproduction_rate cannot be negative')
        return attrs
    