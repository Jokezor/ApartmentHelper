import math

import scrapy

from utils import write_to_csv_file


class ClosingPricesSpider(scrapy.Spider):
    name = 'closingprices'
    start_urls = [
        'https://www.booli.se/slutpriser/vasastan/115349',
    ]
    current_page = 0
    listings = []

    def parse(self, response):
        index = 0
        extra_info_ind = 0
        percent_ind = 0

        max_listings = int(response.css('div div div div span::text').extract()[response.css('div div div div span::text').extract().index(' av ') + 1])
        last_page = math.ceil(max_listings / 35)

        for listing in response.css('div div a div'):
            try:
                address = response.css('div div a div h4::text')[index].extract()
                price = response.css('div div a div h4::text')[index+1].extract()
                percent_increase = response.css('div div a div div::text')[percent_ind].extract()
                size = response.css('div div a div p::text')[extra_info_ind].extract()
                area = response.css('div div a div p::text')[extra_info_ind + 1].extract()
                sqm_price = response.css('div div a div p::text')[extra_info_ind + 2].extract()
                date_sold = response.css('div div a div p::text')[extra_info_ind + 3].extract()

                try:
                    price = int(price.split('kr')[0].replace(' ', ''))
                    self.listings.append({'address': address, 'price': price, 'size': size, 'date_sold': date_sold, 'sqm_price': sqm_price, 'area': area, 'percent_increase': percent_increase})
                except ValueError:
                    pass

            except IndexError:
                pass

            index += 2
            percent_ind += 1
            extra_info_ind += 4

        self.current_page += 1
        next_page = f'https://www.booli.se/slutpriser/vasastan/115349?page={self.current_page}'
        print(self.current_page)
        if self.current_page <= last_page:
            yield response.follow(next_page, self.parse)
        else:
            if write_to_csv_file(self.listings):
                print(f"Succesfully scraped {self.current_page} pages and saved it into csv file.")
            else:
                print("There was some issue with writing to the csv file.")
