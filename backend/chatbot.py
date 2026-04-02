def health_chatbot(query):
    query = query.lower()

    if "fever" in query:
        return "Possible fever. Take Paracetamol, drink fluids, rest."

    elif "headache" in query:
        return "Headache: Take Ibuprofen/Paracetamol and stay hydrated."

    elif "cold" in query or "cough" in query:
        return "Cold/Cough: Steam inhalation, warm fluids, antihistamine."

    elif "stomach pain" in query:
        return "Stomach pain: Take antacid and avoid spicy food."

    elif "burn" in query:
        return "Burn: Run cool water for 10 minutes and apply burn ointment."

    elif "cut" in query:
        return "Cut: Clean wound, apply antiseptic and bandage."

    elif "chest pain" in query:
        return "Chest pain may be serious. Please press SOS immediately."

    else:
        return "Please describe symptoms clearly. Consult doctor if serious."