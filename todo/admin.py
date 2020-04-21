from django.contrib import admin
from .models import Todo # . = 현재 디렉토리 .. = 상위 디렉토리 (폴더)


# Register your models here. 너의 모델을 넣어라

admin.site.register(Todo)
