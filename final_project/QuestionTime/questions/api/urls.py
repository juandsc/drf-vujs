from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api.views import (AnswerCreateAPIView, AnswerListAPIView,
                                 QuestionViewSet)

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'questions/<slug:slug>/answer/', AnswerCreateAPIView.as_view(),
        name='create-answer'
    ),
    path(
        'questions/<slug:slug>/answers/', AnswerListAPIView.as_view(),
        name='answer-list'
    ),
]
