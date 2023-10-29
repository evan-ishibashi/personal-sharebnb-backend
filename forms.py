from flask_wtf import FlaskForm


class CSRFProtection(FlaskForm):
    """CSRFProtection form, intentionally has no fields."""
