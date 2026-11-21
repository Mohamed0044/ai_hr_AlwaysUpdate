from django.urls import path

from .views import (
    create_department,
    create_job_position,
    create_candidate,
    upload_resume,
    screening_result_detail,
    interview_question_set_detail,
)


urlpatterns = [
    path(
        'departments/',
        create_department,
        name='create_department',
    ),
    path(
        'job-positions/',
        create_job_position,
        name='create_job_position',
    ),
    path(
        'candidates/',
        create_candidate,
        name='create_candidate',
    ),
    path(
        'resumes/',
        upload_resume,
        name='upload_resume',
    ),
    path(
        'screening-results/<int:pk>/',
        screening_result_detail,
        name='screening_result_detail',
    ),
    path(
        'interview-question-sets/<int:pk>/',
        interview_question_set_detail,
        name='interview_question_set_detail',
    ),
]