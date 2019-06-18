from django.urls import path
from job.api.views import (
    JobOfferListCreateAPIView, JobOfferDetailAPIView
)

urlpatterns = [
    path(
        'joboffers/', JobOfferListCreateAPIView.as_view(),
        name='joboffer-list'
    ),
    path(
        'joboffers/<int:pk>', JobOfferDetailAPIView.as_view(),
        name='joboffer-detail'
    )
]
