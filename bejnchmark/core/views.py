from django.shortcuts import render


def templatetags(request, depth, count):
    return render(request, 'templatetags.html', {
        'count': range(int(count)),
        'depth': int(depth),
        'level': 0,
    })


def includes(request, depth, count):
    return render(request, 'includes.html', {
        'count': range(int(count)),
        'depth': int(depth),
        'level': 0,
    })
