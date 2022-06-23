from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import ShortUrlForm


def index(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        shorted_url = form.save()
        data = {
            'shorted_url': shorted_url
        }
        return render(request, 'webapp/new_url.html', data)
    form = ShortUrlForm()

    context = {'form': form}
    return render(request, 'webapp/index.html', context)


def get_shorted_url(request, param):
    url = ShortUrl.objects.filter(url_context=param).first()

    if url is None:
        return render(request, 'webapp/not_found.html', context={'url': param})
    url.increment_shares()
    return redirect(url.original_url)


def show_all_shorted_urls(request):
    if request.method == 'POST':
        delete(request, request.POST.get('id'))

    shorted_urls = ShortUrl.objects.all()

    views = []
    for url in shorted_urls:
        view = {
            'shorted_url': url.shorted_url,
            'shares': url.shares,
            'id': url.id
        }

        views.append(view)

    context = {'urls': views}

    return render(request, 'webapp/urls.html', context)

def delete(request, id):
    shorted_url = ShortUrl.objects.filter(id=id)

    if shorted_url is None:
        redirect(render(request, 'webapp/error.html'))

    shorted_url.delete()
    return redirect('webapp .views.show_all_shorted_urls')
