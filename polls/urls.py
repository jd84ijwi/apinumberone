
from django.urls import include, re_path, path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from .views import polls_list, polls_detail
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path('', polls_list, name='polls_list'),
    path('<int:pk>/', polls_detail, name='polls_detail'),
    path('polls/', PollList.as_view(), name='polls_listt'),
    path('<int:pk>', PollDetail.as_view, name='polls_detail'),
    path('<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', views.obtain_auth_token, name='login')

]



