user_states = {}


def get_user(phone_number: str) -> dict:
    if phone_number not in user_states:
        user_states[phone_number] = {
            "state": "idle",
            "department": None,
            "doctor": None,
            "date": None,
            "time": None,
        }

    return user_states[phone_number]


def set_state(phone_number: str, state: str):
    user = get_user(phone_number)
    user["state"] = state


def get_state(phone_number: str) -> str:
    return get_user(phone_number)["state"]


def update_user(phone_number: str, field: str, value: str):
    user = get_user(phone_number)
    user[field] = value


def clear_state(phone_number: str):
    user_states.pop(phone_number, None)