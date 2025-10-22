"""
Shared utility functions
"""

def validate_data(data):
    """Validate incoming data structure"""
    if not isinstance(data, dict):
        return False
    if "source" not in data or "type" not in data:
        return False
    print(f"Validated data from {data['source']}")
    return True

def transform_data(data):
    """Common data transformation logic"""
    data["processed"] = True
    return data
