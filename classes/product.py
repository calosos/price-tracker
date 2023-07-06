class Product:
    def __init__(self, name, price, link):
        """
        Initialize a Product object
        :param name: The name of the product
        :param price: The price of the product
        :param link: The link to the product
        """
        self._name = name
        self._price = price
        self._link = link

    @property
    def name(self):
        """
        Get the name of the product
        :return: The name of the product
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Set the name of the product
        :param name: The name of the product
        """
        self._name = name

    @property
    def price(self):
        """
        Get the price of the product
        :return: The price of the product
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Set the price of the product
        :param price: The price of the product
        """
        self._price = price

    @property
    def link(self):
        """
        Get the link to the product
        :return: The link to the product
        """
        return self._link

    def show_info(self):
        """
        Display the information of the product.
        """
        print(f"Product: {self._name}")
        print(f"Price: {self._price}")
        print(f"Link: {self._link}")
