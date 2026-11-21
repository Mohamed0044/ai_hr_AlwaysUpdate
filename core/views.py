from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .serializers import DepartmentSerializer, JobPositionSerializer, CandidateSerializer
from .models import ScreeningResult, InterviewQuestionSet
from .serializers import ResumeSerializer, ScreeningResultSerializer, InterviewQuestionSetSerializer

@api_view(['POST'])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_job_position(request):
    serializer = JobPositionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_resume(request):
    serializer = ResumeSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'HEAD'])
def screening_result_detail(request, pk):
    result = get_object_or_404(ScreeningResult.objects.select_related('candidate', 'job_position'), pk=pk)
    serializer = ScreeningResultSerializer(result)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'HEAD'])
def interview_question_set_detail(request, pk):
    question_set = get_object_or_404(InterviewQuestionSet.objects.select_related('candidate', 'job_position'), pk=pk)
    serializer = InterviewQuestionSetSerializer(question_set)
    return Response(serializer.data, status=status.HTTP_200_OK)
