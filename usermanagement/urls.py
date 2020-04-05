from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user-list$', UserListView.as_view({
        "get": "list",
    })),
]