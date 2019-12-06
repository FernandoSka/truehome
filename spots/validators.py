from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_m2(value):
    if not 0 < value < 99999:
        raise ValidationError(
            _('%(value)s may be in range 0-99999'),
            params={'value': value},
        )