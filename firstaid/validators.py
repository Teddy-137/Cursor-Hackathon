from django.core.exceptions import ValidationError
import json


def validate_json_array(value):
    """
    Validates that the value is a valid JSON array.
    """
    if not isinstance(value, list):
        raise ValidationError("Value must be a JSON array (list).")

    # Additional validation can be added here if needed
    # For example, ensuring all items are strings
    for item in value:
        if not isinstance(item, str):
            raise ValidationError("All items in the array must be strings.")
