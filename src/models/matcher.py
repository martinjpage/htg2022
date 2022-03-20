import src.services.constants as const


class Matcher:
    def __init__(self, datastore, config):
        self._datastore = datastore
        self._config = config

    def match_offers(self):
        orderbook = self._datastore.read_orderbook()

        buyer_mask = orderbook[self._config.role] == const.buyer
        supplier_mask = orderbook[self._config.role] == const.supplier
        if not buyer_mask.any():
            print('Currently there are no buy offers in the orderbook. No match can be made at present.')
            return False
        if not supplier_mask.any():
            print('Currently there are no sell offers in the orderbook. No match can be made at present.')
            return False

        buyers = orderbook[buyer_mask]
        suppliers = orderbook[supplier_mask]

        for index, buyer in buyers.sort_values(self._config.price, ascending=False).iterrows():
            valid_suppliers = suppliers[suppliers[self._config.price] <= buyer[self._config.price]]
            if valid_suppliers.size > 0:
                selected_supplier = valid_suppliers.loc[valid_suppliers[self._config.price].idxmax()]
                final_price = max(selected_supplier[self._config.price], buyer[self._config.price])
                return {"supplier_index": selected_supplier.name, 'buyer_index': index,
                        'supplier_username': selected_supplier[self._config.meter_id],
                        'buyer_username': buyer[self._config.meter_id],
                        'energy_requested': buyer[self._config.energy],
                        'energy_available': selected_supplier[self._config.energy],
                        'price': final_price}
        return {}
