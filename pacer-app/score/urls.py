from django.urls import path
from .views import ScoreView

urlpatterns = [
    path("get_score/", ScoreView.as_view(), name="get_score"),
]