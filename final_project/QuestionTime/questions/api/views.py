from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwargs_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwargs_slug)

        if  question.answers.filter(author=request_user).exists():
            raise ValidationError('Ya has respondido esta pregunta!!')

        serializer.save(author=request_user, question=question)


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwargs_slug = self.kwargs.get('slug')
        answers = Answer.objects.filter(question__slug=kwargs_slug)
        return answers.order_by('-created_at')
    
