from django.contrib import admin

from planetarium_service.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Ticket,
    Reservation
)


admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(PlanetariumDome)
admin.site.register(ShowSession)
admin.site.register(Reservation)
admin.site.register(Ticket)
