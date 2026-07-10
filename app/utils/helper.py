import re

# def get_str_from_food_dict(food_dict: dict):
#     result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
#     return result

def get_str_from_food_dict(food_dict: dict):
    items = [f"{int(value)} {key}" for key, value in food_dict.items()]

    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string

    return ""