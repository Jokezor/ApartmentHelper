import scrapy


class ClosingPricesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.booli.se/slutpriser/vasastan/115349',
    ]

    def parse(self, response):
        print("css dsfjdfsdfifsddfo", response.css, "fdskdsfhsdfkshfd")

        listings = {}
        index = 0
        percent_ind = 0
        date_ind = 3
        sqm_price_ind = 2
        size_ind = 0

        for listing in response.css('div div a div'):
            try:
                address = response.css('div div a div h4::text')[index].extract()
                price = response.css('div div a div h4::text')[index+1].extract()
                percent_increase = response.css('div div a div div::text')[percent_ind].extract()
                size = response.css('div div a div p::text')[size_ind].extract()
                sqm_price = response.css('div div a div p::text')[sqm_price_ind].extract()
                date_sold = response.css('div div a div p::text')[date_ind].extract()


                try:
                    price = int(price.split('kr')[0].replace(' ', ''))
                except ValueError:
                    pass

                print("\nTITLE:!!!!!!", address, "\n", price, "\n\n",
                "listings:", index/2, "percent:", percent_increase, "date sold", date_sold, "size", size, "sqm price", sqm_price)
            except IndexError:
                pass

            index += 2
            percent_ind += 1
            date_ind += 4
            size_ind += 4
            sqm_price_ind += 4


