from django.contrib import admin

from django.contrib import admin
from .models import BodyLog

# models.py는 데이터베이스 설계도, admin.py는 관리자용 대시보드 설정 파일
# 용도: 실제 사용자가 보는 화면(Front-end)을 만들기 전에, 개발자가 DB에 데이터가 잘 들어갔는지 확인하고 직접 수정/삭제하기 위해 사용합니다.
# 작동 원리: 장고는 기본적으로 관리자 페이지를 제공하는데, 모델(BodyLog)은 관리자 페이지에 자동으로 나타나지 않습니다. 그래서 admin.py에서 "이 모델을 관리자 페이지에 등록(register)해줘!"라고 선언
# 커스터마이징: list_display 같은 설정을 통해 "목록 화면에서 어떤 항목들을 보여줄지" 결정합니다. bmi처럼 계산된 값도 여기서 보여주도록 설정 가능

@admin.register(BodyLog)
class BodyLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'height', 'weight', 'bmi')