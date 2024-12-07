from django.urls import path
from . import views

app_name = 'FeedApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile',views.profile, name='profile'), # adding profile , when user login, go ahed and fill up the information
    path('myfeed',views.myfeed, name='myfeed'), # adding my feed
    path('new_post/',views.new_post, name='new_post'), # adding new post
    path('comments/<int:post_id>/',views.comments, name='comments'), # adding new post
    path('friendsfeed',views.friendsfeed, name='friendsfeed'), # adding friendsfeed  view
    path('friends/',views.friends, name='friends'), # adding friends  view
    ]

    