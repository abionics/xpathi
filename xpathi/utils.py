def _format_parameter(value, special: bool = True) -> str:
    if not isinstance(value, str):
        return str(value)
    if value.startswith('@') and special:
        return value
    if value in ['text()', 'name()'] and special:
        return value
    return f'"{value}"'
