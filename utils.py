from jinja2 import Environment, FileSystemLoader
import os

environment = Environment(loader=FileSystemLoader("templates/"))

def render(template_name, context={}):

    template = environment.get_template(template_name)
    return template.render(context)


def static(path):
    static_urls = []
    for file_name in os.listdir(path):
        static_urls.append(f'/{path}{file_name}/')
    return static_urls


def static_view(file, static_root):
    if file in os.listdir(static_root):
        with open(f'{static_root}{file}') as f:
            return f.read()
