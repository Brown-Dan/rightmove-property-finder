# 🏠 RightMove Enhanced Property Filter 🏠

RightMove is a platform for finding properties, but it has some limitations. For example, you can't filter listings by **ground rent**, **service charge**, or **minimum lease length**. Additionally, many listings include phrases like **"investors only"**, **"cash only"**, or **"auction"**, which aren't relevant if you're looking for a home to live in.

---

## 🚀 How It Works

The tool uses a combination of search parameters and custom filters to retrieve and filter property listings from RightMove. Here's an example of how to use it:

```python
# Define your search parameters
search_params = SearchParamsBuilder() \
    .set_min_bedrooms(2) \
    .set_min_price(150000) \
    .set_max_price(190000) \
    .build()

# Define your custom filters
filter_params = FilterParamsBuilder() \
    .set_max_ground_rent(200) \
    .set_max_service_charge(1600) \
    .set_min_lease_length(100) \
    .set_forbidden_words(["investors only", "cash only", "auction", "tenanted"]) \
    .build()

# Retrieve and filter properties
properties = list(map(
    lambda property_data: retrieve_properties_by_id_and_filter(property_data["id"], filter_params),
    get_properties(search_params.get_url())
))

# Output the filtered properties
print(properties)
```

---

## 🔧 Key Features

1. **Ground Rent Filter**: Exclude properties with ground rent above a specified amount.
2. **Service Charge Filter**: Exclude properties with service charges above a specified amount.
3. **Lease Length Filter**: Exclude properties with lease lengths below a specified number of years.
4. **Forbidden Words Filter**: Exclude properties that contain phrases like "investors only", "cash only", or "auction".

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rightmove-enhanced-filter.git
   cd rightmove-enhanced-filter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

---

## 📝 Example Use Case

Let's say you're looking for a 2-bedroom property in Manchester with:
- A price range of £150,000 to £190,000
- Ground rent no more than £200 per year
- Service charge no more than £1,600 per year
- A minimum lease length of 100 years
- No "investors only", "cash only", or "auction" listings

Using this tool, you can easily filter out irrelevant listings and focus on properties that meet your needs.

---
