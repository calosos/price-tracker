import requests
from bs4 import BeautifulSoup


class AmazonScraper:
    @staticmethod
    def search_prices(product):
        """
        Search and retrieve the price of a product from Amazon
        :param product: The Product object to search the price for
        """
        # Construct the search URL for the product on Amazon
        search_url = f"https://www.amazon.com/s?k=ñ{product.get_name().replace(' ', '+')}"

        # Send a GET request to the search URL and get the response
        response = requests.get(search_url)

        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.text, 'html.parser')
