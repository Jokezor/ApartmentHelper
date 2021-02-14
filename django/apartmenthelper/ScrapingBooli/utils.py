import csv


def write_to_csv_file(listings: list) -> bool:
    pricing_columns = ['address', 'price', 'size', 'date_sold', 'sqm_price', 'area', 'percent_increase']

    with open('listings.csv', 'w+') as csvfile:
        file_writer = csv.DictWriter(csvfile, fieldnames=pricing_columns)
        file_writer.writeheader()

        try:
            for listing in listings:
                file_writer.writerow(listing)
            return True
        except ValueError:
            return False
