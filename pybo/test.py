from django.test import TestCase

from pybo.models import Question
from django.utils import timezone

for i in range(300):
    q=Question(
        subject = f'테스트 데이터입니다: [{i:03d}]',
        content = f'테스트 데이터의 내용입니다:[{ㅑ:03d}]'
    )
    q.save()