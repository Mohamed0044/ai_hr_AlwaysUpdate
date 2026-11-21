from django.db import models
from django.core.exceptions import ValidationError
from .screening_result import ScreeningResult

class InterviewQuestionSet(models.Model):
    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.PROTECT,
        related_name='interview_question_sets',
    )
    job_position = models.ForeignKey(
        'JobPosition',
        on_delete=models.PROTECT,
        related_name='interview_question_sets',
    )
    screening_result = models.ForeignKey(
        'ScreeningResult',
        on_delete=models.PROTECT,
        related_name='interview_question_sets',
    )
    technical_questions = models.JSONField(default=list, blank=True)
    behavioral_questions = models.JSONField(default=list, blank=True)
    follow_up_questions = models.JSONField(default=list, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-generated_at']

    def __str__(self):
        return (
            f'Interview: {self.candidate.full_name} - '
            f'{self.job_position.title}'
        )

    def clean(self):
        super().clean()

        if not self.screening_result_id:
            return

        result = ScreeningResult.objects.filter(
            pk=self.screening_result_id
        ).first()

        if result is None:
            return

        errors = {}

        if self.candidate_id != result.candidate_id:
            errors['candidate'] = (
                'Candidate must match the screening result.'
            )

        if self.job_position_id != result.job_position_id:
            errors['job_position'] = (
                'Job position must match the screening result.'
            )

        if errors:
            raise ValidationError(errors)