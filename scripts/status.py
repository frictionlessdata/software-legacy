from jinja2 import Template

# Platforms

platforms = [
    'python',
    'javascript',
    'ruby',
    'php',
    'java',
    'go',
    'julia',
    'clojure',
    'r',
]

# Packages

packages = {
    'python': [
        {'name': 'tabulator', 'repo': 'tabulator-py'},
        {'name': 'tableschema', 'repo': 'tableschema-py'},
        {'name': 'tableschema-bigquery', 'repo': 'tableschema-bigquery-py'},
        {'name': 'tableschema-ckan-datastore', 'repo': 'tableschema-ckan-datastore-py'},
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
        {'name': 'goodtables', 'repo': 'goodtables-js'},
        {'name': 'goodtables-ui', 'repo': 'goodtables-ui'},
    ],
    'ruby': [
        {'name': 'tableschema', 'repo': 'tableschema-rb'},
        {'name': 'datapackage', 'repo': 'datapackage-rb'},
    ],
    'php': [
        {'name': 'tableschema', 'repo': 'tableschema-php'},
        {'name': 'datapackage', 'repo': 'datapackage-php'},
    ],
    'java': [
        {'name': 'tableschema', 'repo': 'tableschema-java'},
        {'name': 'datapackage', 'repo': 'datapackage-java'},
    ],
    'go': [
        {'name': 'tableschema-go', 'repo': 'tableschema-go'},
        {'name': 'datapackage-go', 'repo': 'datapackage-go'},
    ],
    'julia': [
        {'name': 'TableSchema.jl', 'repo': 'TableSchema.jl'},
        {'name': 'DataPackage.jl', 'repo': 'DataPackage.jl'},
    ],
    'clojure': [
        {'name': 'tableschema', 'repo': 'tableschema-clj'},
        {'name': 'datapackage', 'repo': 'datapackage-clj'},
    ],
    'r': [
        {'name': 'tableschema.r', 'repo': 'tableschema-r'},
        {'name': 'datapackage.r', 'repo': 'datapackage-r'},
    ],
}

# Render

with open('scripts/status.md') as file:
    template = Template(file.read())
    document = template.render(platforms=platforms, packages=packages)
    print(document)
