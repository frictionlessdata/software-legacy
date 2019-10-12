from jinja2 import Template
from config import platforms, packages, maintainers

# Render

if __name__ == '__main__':
    with open('scripts/status.md') as file:
        template = Template(file.read())
        document = template.render(
            platforms=platforms,
            packages=packages,
            maintainers=maintainers)
        print(document)
