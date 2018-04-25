from django import template


from menu.models import Item
register = template.Library()


@register.inclusion_tag('tree_menu.html', takes_context=True)
def draw_menu(context, menu_name):


    try:
        item_queryset = Item.objects.filter(menu_id=menu_name)
        item_queryset_values = item_queryset.values()

        root_item = [item for item in item_queryset_values.filter(parent_item=None)]
        selected_item_id = int(context['request'].GET[menu_name])
        selected_item = item_queryset.get(id=selected_item_id)

        parent_item = selected_item
        selected_item_id_list = get_selected_item_id_list(parent_item, root_item, selected_item_id)

        for item in root_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(item_queryset_values, item['id'], selected_item_id_list)

        result_dict = {'items': root_item,}

    except:
        selected_item_id = None
        result_dict = {'items':[item for item in Item.objects.filter(menu_id=menu_name, parent_item=None).values()]}

    result_dict['menu_name'] = menu_name
    result_dict['other_querystring'] = get_querystring(context, menu_name)

    return result_dict


def get_querystring(context, menu_name):
    querystring_args = []

    for key in context['request'].GET:
        if key != menu_name:
            querystring_args.append(key + '=' + context['request'].GET[key])

    querystring = ('&').join(querystring_args)

    return querystring


def get_child_items(item_queryset_values, current_item_id, selected_item_id_list):
    item_list = [item for item in item_queryset_values.filter(parent_item_id=current_item_id)]

    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(item_queryset_values, item['id'], selected_item_id_list)

    return item_list


def get_selected_item_id_list(parent_item, root_item, selected_item_id):
    selected_item_id_list = []

    while parent_item:
        selected_item_id_list.append(parent_item.id)
        parent_item = parent_item.parent_item

    if not selected_item_id_list:
        for item in root_item:
            if item['id'] == selected_item_id:
                selected_item_id_list.append(selected_item_id)

    return selected_item_id_list