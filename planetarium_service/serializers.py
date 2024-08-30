from rest_framework import serializers

from planetarium_service.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Ticket,
    Reservation
)


class ShowThemeSerializer(serializers.ModelSerializer):
    astronomyshow = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="title"
    )

    class Meta:
        model = ShowTheme
        fields = ("id", "name", "astronomyshow")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "showtheme")


class ShowThemeRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTheme
        fields = ("id", "name", "astronomyshow")


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ShowSessionSerializer(serializers.ModelSerializer):
    planetarium_dome = PlanetariumDomeSerializer(many=False, read_only=True)
    astronomy_show = AstronomyShowSerializer(many=False, read_only=True)

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_shows", "planetarium_dome", "show_time")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    show_session = ShowSessionSerializer(many=False, read_only=True)
    reservation = ReservationSerializer(many=False, read_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "reservation")
