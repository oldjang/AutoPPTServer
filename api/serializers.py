from rest_framework import serializers
from .models import Template


class TemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Template  # 指定的模型类
        fields = ('pk', 'image_url','template_url')
