from backend.state import get_state, set_state, clear_state, update_user, get_user


def generate_response(phone_number: str, message: str) -> str:
    message = message.lower().strip()
    state = get_state(phone_number)

    # Start / reset conversation
    if message in ["hi", "hello", "hey", "start"]:
        clear_state(phone_number)
        return (
            "Hello! Welcome to Mini MediCare Pro.\n\n"
            "How can I help you today?\n"
            "1. Book an appointment\n"
            "2. View doctors\n"
            "3. Emergency\n"
            "4. Help"
        )

    # Emergency
    if "emergency" in message:
        return (
            "EMERGENCY\n\n"
            "If this is a medical emergency, please contact "
            "your local emergency service or go to the nearest hospital immediately."
        )

    # Start appointment
    if "appointment" in message or "book" in message:
        clear_state(phone_number)
        set_state(phone_number, "choosing_department")
        return (
            "Appointment Booking\n\n"
            "Please choose a department:\n"
            "1. General Medicine\n"
            "2. Cardiology\n"
            "3. Pediatrics\n"
            "4. Dermatology"
        )

    # Choose department
    if state == "choosing_department":
        departments = {
            "1": "General Medicine",
            "2": "Cardiology",
            "3": "Pediatrics",
            "4": "Dermatology",
        }
        if message in departments:
            department = departments[message]
            update_user(phone_number, "department", department)
            set_state(phone_number, "choosing_doctor")
            return (
                f"You selected {department}.\n\n"
                "Please enter the doctor's name."
            )
        return "Please choose a valid department: 1, 2, 3, or 4."

    # Choose doctor
    if state == "choosing_doctor":
        doctor = message.title()
        update_user(phone_number, "doctor", doctor)
        set_state(phone_number, "choosing_date")
        return (
            f"Doctor selected: {doctor}\n\n"
            "Please enter your preferred appointment date."
        )

    # Choose date
    if state == "choosing_date":
        date = message
        update_user(phone_number, "date", date)
        set_state(phone_number, "choosing_time")
        return (
            f"Date selected: {date}\n\n"
            "Please enter your preferred appointment time."
        )

    # Choose time
    if state == "choosing_time":
        time = message
        update_user(phone_number, "time", time)
        set_state(phone_number, "confirming")
        user = get_user(phone_number)
        return (
            "Please confirm your appointment:\n\n"
            f"Department: {user['department']}\n"
            f"Doctor: {user['doctor']}\n"
            f"Date: {user['date']}\n"
            f"Time: {user['time']}\n\n"
            "Type YES to confirm or NO to cancel."
        )

    # Confirm appointment
    if state == "confirming":
        if message == "yes":
            user = get_user(phone_number)
            department = user["department"]
            doctor = user["doctor"]
            date = user["date"]
            time = user["time"]
            clear_state(phone_number)
            return (
                "Appointment confirmed successfully!\n\n"
                f"Department: {department}\n"
                f"Doctor: {doctor}\n"
                f"Date: {date}\n"
                f"Time: {time}\n\n"
                "Thank you for choosing Mini MediCare Pro."
            )
        if message == "no":
            clear_state(phone_number)
            return (
                "Appointment cancelled.\n\n"
                "You can type 'Book appointment' whenever you want to try again."
            )
        return "Please reply with YES or NO."

    # Doctors
    if "doctor" in message:
        return (
            "Available departments:\n"
            "1. General Medicine\n"
            "2. Cardiology\n"
            "3. Pediatrics\n"
            "4. Dermatology"
        )

    # Help
    if message == "help":
        return (
            "I can help you with:\n\n"
            "• Book an appointment\n"
            "• Find doctors/departments\n"
            "• Emergency information\n\n"
            "Type your request to continue."
        )

    return (
        "I didn't understand that.\n\n"
        "Try typing:\n"
        "• Hi\n"
        "• Book appointment\n"
        "• Doctors\n"
        "• Emergency\n"
        "• Help"
    )