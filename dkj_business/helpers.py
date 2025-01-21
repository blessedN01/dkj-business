import re
from wtforms.validators import ValidationError


def validate_password(form, field):
    """Validate form.data strength."""
    if len(field.data) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', field.data):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', field.data):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r'\d', field.data):
        raise ValidationError("Password must contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', field.data):
        raise ValidationError("Password must contain at least one special character.")
    return None  # Password is valid
