# form django.form import form (X)
# 장고는 내부적으로 django/forms/__init__.py에서 ModelForm을 미리 꺼내놓습니다.
# 그래서 우리는 django.forms만 불러와도 바로 쓸 수 있죠.
# 하지만 django.forms.forms라고 명시해버리면,
# 장고는 "어? 그 안에는 Form만 있고 ModelForm은 없는데?"라고 반응하며 에러를 냅니다.

from django import forms
from logs.models import BodyLog

# 용도 : BodyLog 모델을 바탕으로 입력창을 만들기 위해

class BodyLogForm(forms.ModelForm):
    class Meta:
        model = BodyLog
        fields = ['height', 'weight', 'image_front', 'image_side', 'image_back', 'note']