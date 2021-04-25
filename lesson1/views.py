from templ import render


class Index:

    def __call__(self, request):
        return '200 OK', render('Index.html')


class Search:

    def __call__(self, request):
        return '200 OK', render('Search.html')


class Contacts:

    def __call__(self, request):
        return '200 OK', render('Contacts.html')


class Not_found_404_view:

    def __call__(self, request):
        return '404 WHAT', render('404.html')
