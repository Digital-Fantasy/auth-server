from .Exceptions import BioTooLong


def validate_phone_number(phone_number: str):
    print("You don't validate phone numbers yet...")
    if phone_number is None:
        return None

def validate_nickname(nickname, default=None):
    print("You don't validate nickanames yet...")
    if nickname is None:
        nickname = default
    return nickname

def validate_picture(url: str, default=None):
    print("You don't validate pictures yet...")
    if url is None:
        url = default
    return url

def validate_username(username:str, defaul=None):
    print("You don't validate usernames yet...")
    if username is None:
        username = defaul
    return username

def validate_name(name: str, default=None):
    print("You don't validate names yet...")
    if name is None:
        name = default
    return name


def validate_bio(bio: str, max_length=500):
    if bio is None:
        bio = "No bio set yet"
    if len(bio) > max_length:
        raise BioTooLong(len(bio), max_length, f"Bio is too long. Max character length is: {max_length}. Your bio has {len(bio)} characters.")
    return bio
