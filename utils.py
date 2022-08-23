from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader("templates/"))

def render(template_name, context={}):

    template = environment.get_template(template_name)
    return template.render(context)
