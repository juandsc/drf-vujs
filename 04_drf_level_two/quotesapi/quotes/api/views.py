from rest_framework import generics
from rest_framework.generics import get_object_or_404

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminOrReadOnly


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-created_at')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        quote_author = self.request.user
        serializer.save(quote_author=quote_author)


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]