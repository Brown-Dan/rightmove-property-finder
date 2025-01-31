class FilterParams:
    def __init__(self, max_service_charge, max_ground_rent, min_lease_length):
        self.max_service_charge = max_service_charge
        self.max_ground_rent = max_ground_rent
        self.min_lease_length = min_lease_length

    def get_max_service_charge(self):
        return self.max_service_charge

    def get_max_ground_rent(self):
        return self.max_ground_rent

    def get_min_lease_length(self):
        return self.min_lease_length

    def __str__(self):
        return f"Max Service Charge: {self.max_service_charge}, Max Ground Rent: {self.max_ground_rent}, Min Lease Length: {self.min_lease_length}"


class FilterParamsBuilder:
    def __init__(self):
        self.max_service_charge = None
        self.max_ground_rent = None
        self.min_lease_length = None

    def set_max_service_charge(self, max_service_charge):
        self.max_service_charge = max_service_charge
        return self

    def set_max_ground_rent(self, max_ground_rent):
        self.max_ground_rent = max_ground_rent
        return self

    def set_min_lease_length(self, min_lease_length):
        self.min_lease_length = min_lease_length
        return self

    def build(self):
        if self.max_service_charge is None or self.max_ground_rent is None or self.min_lease_length is None:
            raise ValueError("All parameters must be set")
        return FilterParams(self.max_service_charge, self.max_ground_rent, self.min_lease_length)
