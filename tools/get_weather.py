def get_weather(location: str, unit: str = "celsius") -> str:
    """Mock weather function"""
    return f"The weather in {location} is 22°{unit[0].upper()}, sunny"