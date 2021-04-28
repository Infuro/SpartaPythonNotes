import json

'''
pet_data = {"name":"Bob","food":"carrots"}

pet_data_json_str = json.dumps(pet_data)

with open("new_json_file.json", "w") as jsonfile:
    json.dump(pet_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    pet = json.load()
'''

class RatesParser:
    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        self.gbp = self.rates["GBP"]

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)

rates_reader = RatesParser("exchange_rates.json")
print(rates_reader.base)
print(rates_reader.gbp)