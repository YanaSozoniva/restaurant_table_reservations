from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size=5 * 1024 * 1024):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.size
        if file_size > self.max_size:
            raise ValidationError("Размер файла, не должен быть больше 5 Mб")


@deconstructible
class ImageFormatValidator:
    def __init__(self, allowed_format=None):
        if allowed_format is None:
            allowed_format = ["png", "jpeg", "jpg"]
        self.allowed_format = allowed_format

    def __call__(self, value):
        file_format = value.name.split(".")[-1].lower()
        if file_format not in self.allowed_format:
            raise ValidationError("Недопустимое расширение файла. Можно загружать только png, jpeg, v")
