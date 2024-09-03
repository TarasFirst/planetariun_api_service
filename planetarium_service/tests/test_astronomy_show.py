from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from planetarium_service.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
)
from planetarium_service.serializers import (
    AstronomyShowListSerializer,
    AstronomyShowDetailSerializer,
)

ASTRONOMY_SHOW_URL = reverse("planetarium_service:astronomyshow-list")
SHOW_SESSION_URL = reverse("planetarium_service:showsession-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample astronomy_show",
        "description": "Sample description",
        "duration": 90,
    }
    defaults.update(params)

    return AstronomyShow.objects.create(**defaults)


def sample_show_session(**params):
    planetarium_dome = PlanetariumDome.objects.create(
        name="Blue", rows=20, seats_in_row=20
    )

    defaults = {
        "show_time": "2024-05-06 10:00:00",
        "astronomy_show": None,
        "planetarium_dome": planetarium_dome,
    }
    defaults.update(params)

    return ShowSession.objects.create(**defaults)


def detail_url(astronomy_show_id):
    return reverse("planetarium_service:astronomyshow-detail", args=[astronomy_show_id])


class UnauthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_shows(self):
        sample_astronomy_show()
        sample_astronomy_show()

        res = self.client.get(ASTRONOMY_SHOW_URL)

        astronomy_shows = AstronomyShow.objects.order_by("id")
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_filter_astronomy_shows_by_show_themes(self):
        show_theme_1 = ShowTheme.objects.create(name="ShowTheme 1")
        show_theme_2 = ShowTheme.objects.create(name="ShowTheme 2")

        astronomy_show_1 = sample_astronomy_show(title="astronomy_show 1")
        astronomy_show_2 = sample_astronomy_show(title="astronomy_show 2")

        astronomy_show_1.show_themes.add(show_theme_1)
        astronomy_show_2.show_themes.add(show_theme_2)
        astronomy_show_3 = sample_astronomy_show(title="Astronomy show without show theme")

        res = self.client.get(
            ASTRONOMY_SHOW_URL, {"show_themes": f"{show_theme_1.id},{show_theme_2.id}"}
        )

        serializer1 = AstronomyShowListSerializer( astronomy_show_1)
        serializer2 = AstronomyShowListSerializer( astronomy_show_2)
        serializer3 = AstronomyShowListSerializer( astronomy_show_3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)


    def test_filter_astronomy_shows_by_title(self):
        astronomy_show_1 = sample_astronomy_show(title="AstronomyShow")
        astronomy_show_2 = sample_astronomy_show(title="Another AstronomyShow")
        astronomy_show_3 = sample_astronomy_show(title="No match")

        res = self.client.get(ASTRONOMY_SHOW_URL, {"title": "Show"})

        serializer1 = AstronomyShowListSerializer(astronomy_show_1)
        serializer2 = AstronomyShowListSerializer(astronomy_show_2)
        serializer3 = AstronomyShowListSerializer(astronomy_show_3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_retrieve_astronomy_show_detail(self):
        astronomy_show = sample_astronomy_show()
        astronomy_show.show_themes.add(ShowTheme.objects.create(name="ShowTheme"))

        url = detail_url(astronomy_show.id)
        res = self.client.get(url)

        serializer = AstronomyShowDetailSerializer(astronomy_show)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_astronomy_show_forbidden(self):
        payload = {
            "title": "astronomy_show",
            "description": "Description",
            "duration": 90,
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminAstronomyShowApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_astronomy_show(self):
        payload = {
            "title": "astronomy_show",
            "description": "Description",
            "duration": 90,
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        astronomy_show = AstronomyShow.objects.get(id=res.data["id"])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(astronomy_show, key))

    def test_create_astronomy_show_with_show_themes(self):
        show_theme_1 = ShowTheme.objects.create(name="Stars")
        show_theme_2 = ShowTheme.objects.create(name="Earth")
        payload = {
            "title": "Universe",
            "show_themes": [show_theme_1.id, show_theme_2.id],
            "description": "From the Earth to the Stars.",
            "duration": 128,
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        astronomy_show = AstronomyShow.objects.get(id=res.data["id"])
        show_themes = astronomy_show.show_themes.all()
        self.assertEqual(show_themes.count(), 2)
        self.assertIn(show_theme_1, show_themes)
        self.assertIn(show_theme_2, show_themes)
