from datetime import datetime

from django.db.models import Count, F
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from planetarium_service.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Ticket,
    Reservation
)
from planetarium_service.serializers import (
    ShowThemeSerializer,
    AstronomyShowSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer,
    TicketSerializer,
    ReservationSerializer,
    ShowThemeRetrieveSerializer,
    AstronomyShowRetrieveSerializer,
    ShowSessionRetrieveSerializer,
)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeRetrieveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShowThemeSerializer

        # if self.action in ["retrieve", "create", "update", "partial_update"]:
        #     return ShowThemeRetrieveSerializer
        return ShowThemeRetrieveSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowSerializer

        return AstronomyShowRetrieveSerializer
        # if self.action in ["retrieve", "create", "update", "partial_update"]:
        #     return ShowThemeRetrieveSerializer


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionSerializer

        return ShowSessionRetrieveSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
