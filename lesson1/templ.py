# import os
# from jinja2 import Template


# def render(template_name, folder='templates', **kwargs):

#     file_path = os.path.join(folder, template_name)
#     with open(file_path, encoding='utf-8') as f:
#
#         template = Template(f.read())
#
#     return template.render(**kwargs)
#
#
# if __name__ == '__main__':
#     # Пример использования
#     output_test = render('authors.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
#     print(output_test)


from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)