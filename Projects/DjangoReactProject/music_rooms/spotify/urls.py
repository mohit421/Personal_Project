from django.urls import path
# from .views import AuthURL, spotify_callback, IsAuthenticated, CurrentSong
from .views import  *

urlpatterns = [
    path('get-auth-url', AuthURL.as_view(), name='get-auth-url'),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('current-song', CurrentSong.as_view()),
    path('pause',PauseSong.as_view(),name='spotify-pause'),
    path('play',PlaySong.as_view(),name='spotify-play'),
    path('skip',SkipSong.as_view(),name='spotify-skip'),
    path('prev', PrevSong.as_view(), name='previous-song'),
    path('volume/', ModifyVolume.as_view(), name='modify-volume'),
    path("repeat/", RepeatCurrentSong.as_view(), name="repeat_song"),
]
