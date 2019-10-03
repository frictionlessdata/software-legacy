from jinja2 import Template

# Platforms

platforms = [
    'python',
    'javascript',
    'ruby',
    'java',
]

# Packages

packages = {
    'python': [
        {'name': 'tabulator', 'repo': 'tabulator-py'},
        {'name': 'tableschema', 'repo': 'tableschema-py'},
        {'name': 'tableschema-bigquery', 'repo': 'tableschema-bigquery-py'},
        {'name': 'tableschema-elasticsearch', 'repo': 'tableschema-elasticsearch-py'},
        {'name': 'tableschema-pandas', 'repo': 'tableschema-pandas-py'},
        {'name': 'tableschema-sql', 'repo': 'tableschema-sql-py'},
        {'name': 'tableschema-spss', 'repo': 'tableschema-spss-py'},
        {'name': 'datapackage', 'repo': 'datapackage-py'},
        {'name': 'goodtables', 'repo': 'goodtables-py'},
    ],
    'javascript': [
        {'name': 'tableschema', 'repo': 'tableschema-js'},
        {'name': 'tableschema-ui', 'repo': 'tableschema-ui'},
        {'name': 'datapackage', 'repo': 'datapackage-js'},
        {'name': 'datapackage-ui', 'repo': 'datapackage-ui'},
    ],
    'ruby': [
        {'name': 'tableschema', 'repo': 'tableschema-rb'},
        {'name': 'datapackage', 'repo': 'datapackage-rb'},
    ],
    'java': [
        {'name': 'tableschema', 'repo': 'tableschema-java'},
        {'name': 'datapackage', 'repo': 'datapackage-java'},
    ],
}

# Render

with open('scripts/status.md') as file:
    template = Template(file.read())
    document = template.render(platforms=platforms, packages=packages)
    print(document)
