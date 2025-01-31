import re

import requests, json
from bs4 import BeautifulSoup

from FilterParams import FilterParamsBuilder
from SearchParams import SearchParamsBuilder

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 "
                  "Safari/537.36"}


def get_properties(search_link):
    request = requests.get(search_link, headers=headers)
    content_as_json = json.loads(request.content)
    return content_as_json["properties"]


def retrieve_properties_by_id_and_filter(property_id, filter_params):
    property_link = f"https://www.rightmove.co.uk/properties/{property_id}"
    request = requests.get(property_link, headers=headers)

    soup = BeautifulSoup(request.content, 'html.parser')
    content = soup.find_all('script')
    ad_information_script = content[len(content) - 1]

    if ad_information_script:
        match = re.search(r"const adInfo = ({.*?}}})", ad_information_script.string, re.DOTALL)
        if match:
            json_str = match.group(1)
            data = json.loads(json_str)
            property_data = data["propertyData"]
            living_costs = property_data["livingCosts"]
            tenure = property_data["tenure"]
            annual_service_charge = living_costs["annualServiceCharge"]
            ground_rent = living_costs["annualGroundRent"]
            lease_length = tenure["yearsRemainingOnLease"]

            if filter_params.contains_forbidden_words(property_data["text"]["description"]):
                return

            if annual_service_charge is None or ground_rent is None or lease_length is None:
                return

            if filter_params.get_max_service_charge() > float(annual_service_charge) > 0 \
                    and filter_params.get_max_ground_rent() > float(ground_rent) > 0 \
                    and filter_params.get_min_lease_length() < float(lease_length):
                print(property_link)


# TODO ADD WALKING DISTANCE TO POSTCODE PARAM
if __name__ == "__main__":
    search_params = SearchParamsBuilder().set_min_bedrooms(2).set_min_price(150000).set_max_price(200000).build()
    filter_params = FilterParamsBuilder().set_max_ground_rent(300).set_max_service_charge(1800).set_min_lease_length(
        100).set_forbidden_words(["investors only", "cash only", "auction", "tenanted"]).build()
    list(map(lambda property_data: retrieve_properties_by_id_and_filter(property_data["id"], filter_params),
             get_properties(search_params.get_url())))
