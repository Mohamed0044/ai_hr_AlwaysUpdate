from django.urls import path
from .views import (
    CreateDepartmentView,
    CreateJobPositionView,
    CreateCandidateView,
)
from .views import (
    UploadResumeView,
    ScreeningResultDetailView,
    InterviewQuestionSetDetailView,
)

urlpatterns = [
    path(
        'departments/',
        CreateDepartmentView.as_view(),
        name='create_department',
    ),
    path(
        'job-positions/',
        CreateJobPositionView.as_view(),
        name='create_job_position',
    ),
    path(
        'candidates/',
        CreateCandidateView.as_view(),
        name='create_candidate',
    ),
        path(
        'resumes/',
        UploadResumeView.as_view(),
        name='upload_resume',
    ),
    path(
        'screening-results/<int:pk>/',
        ScreeningResultDetailView.as_view(),
        name='screening_result_detail',
    ),
    path(
        'interview-question-sets/<int:pk>/',
        InterviewQuestionSetDetailView.as_view(),
        name='interview_question_set_detail',
    ),
]