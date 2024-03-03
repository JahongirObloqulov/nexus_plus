from django import template

register = template.Library()


@register.filter(name='new_split')
# def new_split(text, delimiter="", item=1):
#     """
#     Custom template filter to split a string into a list based on a delimiter.
#
#     Usage:
#     {{ value|split }}
#     or
#     {{ value|split:"|" }}
#     """
#     resutl = text.split(delimiter)
#     return resutl[:item] + '.'
def new_split(string, count):
    count_str = 1
    result = ""
    for i in string:
        if count_str >= count and i == " ":
            result = string[:count_str]
            break
        elif count_str >= count and i != " ":
            result = string[:count]

        count_str += 1
    return result
