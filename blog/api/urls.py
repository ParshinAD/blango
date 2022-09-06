from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# to get requests.get("http://127.0.0.1:8000/api/v1/posts/", headers={"Authorization": "Token 81082614a73f331b122ba93dbdb5951b44cf21d4"}) <Response [200]>