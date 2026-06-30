full_dot = '●'
empty_dot = '○'
def create_character(name, s, i, c):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"
    
    stats = [s, i, c]
    if any(not isinstance(x, int) for x in stats):
        return "All stats should be integers"
    if any(x < 1 for x in stats):
        return "All stats should be no less than 1"
    if any(x > 4 for x in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    max_slot = 10
    return_value = name
    return_value += f"\nSTR {full_dot * s}{empty_dot * (max_slot - s)}"
    return_value += f"\nINT {full_dot * i}{empty_dot * (max_slot - i)}"
    return_value += f"\nCHA {full_dot * c}{empty_dot * (max_slot - c)}"

    return return_value

