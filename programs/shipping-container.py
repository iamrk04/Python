import ISO6346


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return ISO6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )
    
    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUE_FT3 = 100

    @property
    def celsius(self):
        return self._celsius

    # property has to be defined first, then only setter can be defined, 
    @celsius.setter         # celsius here has to be same as the name of property
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Tempearture too hot!")
        self._celsius = value        

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        # if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Tempearture too hot!")
        # No need of above check as we have self encapsulation below
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return ISO6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32
    
    @staticmethod
    def _f_to_c(farenheit):
        return (farenheit - 32) * 5 / 9

    @property
    def farenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self.celsius)

    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratorShippingContainer.FRIDGE_VOLUE_FT3


class HeatedRefrigeratorShippingContainer(RefrigeratorShippingContainer):

    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if value < HeatedRefrigeratorShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature to cold!")
        super()._set_celsius(value)


c = ShippingContainer.create_empty("YML", length_ft=20)
print("BIC:\t", c.bic)
print("Volume:\t", c.volume_ft3)

r = RefrigeratorShippingContainer.create_empty("ESC", length_ft=20, celsius=2.0)
print("BIC:\t", r.bic)
print("Volume:\t", r.volume_ft3)

h = HeatedRefrigeratorShippingContainer.create_empty("ESC", length_ft=20, celsius=2.0)
print("BIC:\t", h.bic)
print("Volume:\t", h.volume_ft3)