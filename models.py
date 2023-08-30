from django.contrib import admin
from django.utils.http import format_html
from django.utils import timezone
from dgango.contrib.auth import get_user_model


class Advertisement(models.Model):
@@ -20,6 +21,15 @@ def created_date(self):
                '<span style="color: green; font-weight: bold;">Сегодня в {}'
            )
        return self.create_at.strtime('%d:%m:%Y')


    @admin.display(description='изображение')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">'. url=self.image.url
            )

    def str(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'