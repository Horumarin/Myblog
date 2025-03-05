from django.urls import path
from .views import HomeView, ViewPage, PostTetail

app_name = "techmap"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("view_page/<int:pk>/", ViewPage.as_view(), name="view_page"),
    path("post_detail/<int:pk>/", PostTetail.as_view(), name="post_detail"),
]
