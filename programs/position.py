class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")
        
        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        # Both works, but the second one is more elegant
        # return f"{self.__class__.__name__}(latitude={self.latitude}, logitude={self.longitude})"
        return f"{type(self).__name__}(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return format(self)

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitude_hemisphere}"
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.latitude == other.latitude and self.longitude == other.longitude

    # def __hash__(self):
    #     return ((self.latitude, self.longitude))


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


if __name__ == "__main__":
    oslo = Position(60.0, 10.7)
    print(oslo)
    print(repr(oslo))
    print(str(oslo))
    print(format(oslo))

    mauna_kea = EarthPosition(19.82, -155.47)
    print(mauna_kea)
    print(repr(mauna_kea))

    olympus_mons = MarsPosition(19.82, -155.47)
    print(olympus_mons)
    print(repr(olympus_mons))