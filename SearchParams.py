class SearchParams:
    def __init__(self, min_bedrooms, min_price, max_price):
        self.min_bedrooms = min_bedrooms
        self.min_price = min_price
        self.max_price = max_price

    def get_min_bedrooms(self):
        return self.min_bedrooms

    def get_min_price(self):
        return self.min_price

    def get_max_price(self):
        return self.max_price

    def get_url(self):
        base_url = (
            "https://www.rightmove.co.uk/api/_mapSearch?locationIdentifier=REGION%5E94019"
            "&minBedrooms={min_bedrooms}&maxPrice={max_price}&minPrice={min_price}"
            "&numberOfPropertiesPerPage=499&radius=0.0&sortType=2&index=0"
            "&propertyTypes%5B0%5D=flat&includeSSTC=false&viewType=MAP"
            "&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&viewport"
            "=-2.28871%2C-2.20657%2C53.4564%2C53.5021&isFetching=false"
        )
        return base_url.format(
            min_bedrooms=self.min_bedrooms,
            min_price=self.min_price,
            max_price=self.max_price
        )


class SearchParamsBuilder:
    def __init__(self):
        self.min_bedrooms = None
        self.min_price = None
        self.max_price = None

    def set_min_bedrooms(self, min_bedrooms):
        self.min_bedrooms = min_bedrooms
        return self

    def set_min_price(self, min_price):
        self.min_price = min_price
        return self

    def set_max_price(self, max_price):
        self.max_price = max_price
        return self

    def build(self):
        if self.min_bedrooms is None or self.min_price is None or self.max_price is None:
            raise ValueError("All parameters (min_bedrooms, min_price, max_price) must be set")
        return SearchParams(self.min_bedrooms, self.min_price, self.max_price)
