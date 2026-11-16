from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .serializers import (
    DepartmentSerializer,
    JobPositionSerializer,
    CandidateSerializer,
)
from .models import ScreeningResult, InterviewQuestionSet
from .serializers import (
    ResumeSerializer,
    ScreeningResultSerializer,
    InterviewQuestionSetSerializer,
)


class CreateDepartmentView(APIView):
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class CreateJobPositionView(APIView):
    def post(self, request):
        serializer = JobPositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class CreateCandidateView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

class UploadResumeView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ResumeSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class ScreeningResultDetailView(APIView):
    def get(self, request, pk):
        result = get_object_or_404(
            ScreeningResult.objects.select_related(
                'candidate',
                'job_position',
            ),
            pk=pk,
        )
        serializer = ScreeningResultSerializer(result)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class InterviewQuestionSetDetailView(APIView):
    def get(self, request, pk):
        question_set = get_object_or_404(
            InterviewQuestionSet.objects.select_related(
                'candidate',
                'job_position',
            ),
            pk=pk,
        )
        serializer = InterviewQuestionSetSerializer(question_set)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )