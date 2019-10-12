import re
import json
import requests
from config import platforms, packages


# Extract

if __name__ == '__main__':
    maintainers = {}
    for platform in packages:
        for package in packages[platform]:
            response = requests.get('https://raw.githubusercontent.com/frictionlessdata/%s/master/.github/issue_template.md' % package['repo'])
            maintainer = re.findall(r'\@(\w*)', response.text)[0]
            maintainers[package['repo']] = maintainer
    with open('scripts/maintainers.json', 'w') as file:
        json.dump(maintainers, file, indent=4, ensure_ascii=False)
