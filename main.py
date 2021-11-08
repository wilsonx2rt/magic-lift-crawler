import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
chrome = ua.chrome
headers = {'User-Agent': ua.chrome}

site_map_index_url = 'https://magiclift.ch/sitemap_index.xml'

sitemap_index_dict = {}
site_urls = []


def call_url(target_url):
    return requests.get(target_url, headers=headers)


def get_xml_tags(target_sitemap_url, target):
    response = call_url(target_sitemap_url)
    xml = response.text
    soup = BeautifulSoup(xml, 'lxml')
    return soup.find_all(target)


for sitemap in get_xml_tags(site_map_index_url, 'sitemap'):
    sitemap_index_dict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

sub_site_map_urls = sitemap_index_dict.keys()

for sitemap_url in sub_site_map_urls:
    for url in get_xml_tags(sitemap_url, 'url'):
        site_urls.append(url.findNext("loc").text)

for url in site_urls:
    call_url(url).content
    call_url(url).content
