from views import Index, Search, Contacts, About, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList, CopyCourse


routes = {
    '/': Index(),
    '/search/': Search(),
    '/contacts/': Contacts(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}