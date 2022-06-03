from django import template

register = template.Library()

@register.filter
def previous_item(data_list, current_index):
    try:
        return data_list[int(current_index) - 1] 
    except:
        return '' 