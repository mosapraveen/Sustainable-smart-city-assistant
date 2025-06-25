def ask_assistant(question):
    mock_responses = {
        "energy": "🌍 Smart cities use smart grids, IoT sensors, and AI to monitor and reduce energy consumption in buildings and transport.",
        "waste": "🗑️ AI-powered bins and waste-tracking systems help smart cities improve recycling and reduce landfill use.",
        "water": "🚰 Smart sensors detect leaks and optimize water usage across urban infrastructure.",
        "air": "🌫️ Cities use IoT devices to monitor air quality and apply pollution-reducing policies accordingly.",
        "transport": "🚉 Smart cities use real-time tracking, electric buses, and adaptive traffic lights to improve transport efficiency.",
    }

    lowered = question.lower()
    for keyword in mock_responses:
        if keyword in lowered:
            return mock_responses[keyword]


    return (
        "🤖 Smart cities use technology such as sensors, automation, and AI systems "
        "to enhance sustainability, efficiency, and urban living quality."
    )
