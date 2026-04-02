def check_severity(text):
    text = text.lower()

    emergency_words = ["chest pain", "not breathing", "unconscious", "heavy bleeding"]
    medium_words = ["high fever", "vomiting", "fracture", "burn"]
    
    for word in emergency_words:
        if word in text:
            return "HIGH - Seek immediate medical help"

    for word in medium_words:
        if word in text:
            return "MEDIUM - Visit doctor soon"

    return "LOW - Home care should be enough"