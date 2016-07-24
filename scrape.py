import requests as r
from bs4 import BeautifulSoup
import json
from time import sleep

def get_links():

    yield 'http://www.politifact.com/truth-o-meter/statements/'
    for i in range(2,606):
        yield 'http://www.politifact.com/truth-o-meter/statements/?page={}'.format(i)

def process_info_div(div_as_bs_obj):

    source_q = 'div.statement__body > div.statement__source > a'
    statement_q = 'div.statement__body > p.statement__text > a'
    truth_q = 'div.meter > a > img'

    return {
        'source': div_as_bs_obj.select_one(source_q).text,
        'statment': div_as_bs_obj.select_one(statement_q).text,
        'truth': div_as_bs_obj.select_one(truth_q).get('alt')
    }

def parse_page(html):

    bs_obj = BeautifulSoup(html, 'lxml')
    selector_query = 'body > div > div > div.pfmaincontent > div.content > div > main > section > div.scoretable__item > div.statement'
    info_divs = bs_obj.select(selector_query)

    return [process_info_div(div) for div in info_divs]

def main():

    final_data = []
    for url in get_links():

        print (url)
        html = r.get(url).text
        sleep(10)
        page_data = parse_page(html)

        final_data.append(page_data)
    with open("truth_data.json", 'w') as outfile:
        json.dump(sum(final_data,[]), outfile)

main()
