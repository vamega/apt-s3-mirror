from debian.deb822 import Release, Packages
import requests

BASE_REPO = "https://dl.bintray.com/vamega/personal-debian-server/"
distribution = 'stretch'
release_file_url = BASE_REPO + 'dists/' + distribution + '/Release'

resp = requests.get(release_file_url)

if resp.status_code == 200:
    release = Release(resp.content)
    items = [l for l in release['SHA256'] if l['name'].endswith('Packages')]
    print(items)


useful_keys = [
    'Package',
    'Version',
    'Filename',
    'SHA1',
    'SHA256',
    'Size',
]

for item in items:
    package_url = BASE_REPO + 'dists/' + distribution + '/' +item['name']
    resp = requests.get(package_url)
    if resp.status_code == 200:
        for package in Packages.iter_paragraphs(resp.content):
            subsection = {k: package[k] for k in useful_keys}
            print(subsection)


