# polling/urls.py copied from the course content
# there was no urls.py in my poll directory nor my polling directory

from django.urls import path
from poll.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="poll_index"),
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
]