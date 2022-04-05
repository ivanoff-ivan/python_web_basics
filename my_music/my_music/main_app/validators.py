from django.core.exceptions import ValidationError


def validate_input(text):
    for ch in text:
        if not ch.isalnum():
            if ch != "_":
                raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
