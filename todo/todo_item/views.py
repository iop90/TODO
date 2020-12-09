from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Подарок для жены', 'is_done': True, 'date': '02.12.2020'},
        {'name': 'Подарок для тещи', 'is_done': False},
        {'name': 'Подарок для Шурика', 'is_done': True},
        {'name': 'Подарок для Лехи', 'is_done': False}
    ],
    'user_name': 'Admin',
    'list_name': 'Подарки на НГ'
}


def item_view(request):
    context = data
    return render(request, 'list.html', context)
