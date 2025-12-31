from django.db import models
from django.conf import settings

class BodyLog(models.Model):
    # --- 권한 및 시간 ---
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="기록을 소유한 사용자"
    )
    date = models.DateField(
        auto_now_add=True,
        help_text="기록 날짜"
    )

    # --- 신체 데이터 ---
    height = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="키 (cm)"
    )
    weight = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="몸무게 (kg)"
    )

    # --- 눈바디 사진 (간결한 경로 설정) ---
    # 장고가 자동으로 날짜별 폴더를 생성해주도록 설정했습니다.
    image_front = models.ImageField(
        upload_to='body_images/%Y/%m/%d/front/',
        blank=True, null=True,
        help_text="정면 사진"
    )
    image_side = models.ImageField(
        upload_to='body_images/%Y/%m/%d/side/',
        blank=True, null=True,
        help_text="측면 사진"
    )
    image_back = models.ImageField(
        upload_to='body_images/%Y/%m/%d/back/',
        blank=True, null=True,
        help_text="후면 사진"
    )

    # --- 메모 ---
    note = models.TextField(
        blank=True, null=True,
        help_text="기타 메모"
    )

    def __str__(self):
        return f"{self.user.username} - {self.date}"