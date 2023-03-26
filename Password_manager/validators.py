def validate_user_choice(choice: str) -> None:
    if not choice.isdigit():
        raise ValueError('Choice must be a digit.')

    elif choice not in map(str, range(1, 7)):
        raise ValueError('Choice must be within the range of 1 to 6.')

