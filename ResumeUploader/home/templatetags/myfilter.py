from django import template
register = template.Library()

@register.filter(name="remove_special")
def remove_chars(value, arg):
    # print("Value:", value)
    # print("Arg:", arg)
    for character in arg:
        # print("Character:", character)
        value = value.replace(character, "")
    return value