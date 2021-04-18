from views import Index, Search, Contacts


routes = {
    '/': Index(),
    '/search/': Search(),
    '/contacts/': Contacts()
}