from rest_framework import serializers
from .models import Rectangle, Diamond, Square, Triangle


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ("id", "sideLeft", "sideTop", "sideRight",
                  "sideBottom", "area", "perimeter")
        read_onlyfields = ("id", "area", "perimeter")

    def validate(self, data):
        # Check that all sides are equal
        if not (data['sideLeft'] == data['sideTop'] == data['sideRight'] == data['sideBottom']):
            raise serializers.ValidationError(
                "All sides have to be equal for a square")
        return data


class RectangleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rectangle
        fields = ("id", "sideLeft", "sideTop", "sideRight",
                  "sideBottom", "area", "perimeter")
        read_onlyfields = ("id", "area", "perimeter")

    def validate(self, data):
        # Check that all sides are equal
        if not (data['sideLeft'] == data['sideRight'] and data['sideTop'] == data['sideBottom']):
            raise serializers.ValidationError(
                "Parallel sides' length have to be equal")
        return data


class DiamondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diamond
        fields = (
            "id",
            "sideLeft",
            "sideTop",
            "sideRight",
            "sideBottom",
            "diagonalLength_1",
            "diagonalLength_2",
            "area",
            "perimeter",
        )
        read_onlyfields = ("id", "area", "perimeter")

    def validate(self, data):
        # Check that all sides are equal
        if not (data['sideLeft'] == data['sideRight'] and data['sideTop'] == data['sideBottom']):
            raise serializers.ValidationError(
                "Alternate sides' length have to be equal")
        return data


class TriangleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triangle
        fields = (
            "id",
            "side1",
            "side2",
            "side3",
            "baseLength",
            "height",
            "area",
            "perimeter",
        )
        read_onlyfields = ("id", "area", "perimeter")

    def validate(self, data):
        if data['height'] > max(data['side1'], data['side2'], data['side3']):
            raise serializers.ValidationError(
                "Height cannot be more than all 3 sides of triangle")
        if not(data['baseLengt'] in {data['side1'], data['side2'], data['side3']}):
            raise serializers.ValidationError(
                "baseLength have to be equal to one of the side")


class RectangleAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rectangle
        fields = ("id", "sideLeft", "sideTop", "area")
        read_onlyfields = ("id", "sideLeft", "sideTop", "area")


class DiamondAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diamond
        fields = ("id", "diagonalLength_1", "diagonalLength_2", "area")
        read_onlyfields = ("id", "diagonalLength_1",
                           "diagonalLength_2", "area")


class TriangleAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triangle
        fields = ("id", "baseLength", "height", "area")
        read_onlyfields = ("id", "baseLength", "height", "area")


class QuadrilateralPerimeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rectangle
        fields = ("id", "sideLeft", "sideTop",
                  "sideRight", "sideBottom", "perimeter")
        read_onlyfields = ("id", "sideLeft", "sideTop",
                           "sideRight", "sideBottom", "perimeter")


class TrianglePerimeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triangle
        fields = ("id", "side1", "side2", 'side3', "perimeter")
        read_onlyfields = ("id", "side1", "side2", 'side3', "perimeter")
