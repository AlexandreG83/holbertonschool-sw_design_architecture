#!/usr/bin/env python3

from __future__ import annotations


class Bus:
    def mode(self) -> str:
        return "road"


class Train:
    def mode(self) -> str:
        return "rails"


class Bike:
    def mode(self) -> str:
        return "lane"


class Scooter:
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self) -> None:
        self._vehicles: dict[str, type] = {}
        self._load_defaults()

    def _load_defaults(self) -> None:
        self._vehicles.update({
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        })

    def register_kind(self, vehicle_name: str, vehicle_cls: type) -> None:
        self._vehicles[vehicle_name] = vehicle_cls

    def create(self, vehicle_type: str) -> object:
        vehicle_class = self._vehicles.get(vehicle_type)

        if vehicle_class is None:
            raise ValueError(
                f"Vehicle type not supported: {vehicle_type}"
            )

        return vehicle_class()


def main() -> None:
    factory = VehicleFactory()

    for kind in ("bus", "train", "bike"):
        print(factory.create(kind).mode())

    factory.register_kind("scooter", Scooter)

    scooter = factory.create("scooter")
    print(scooter.mode())


if __name__ == "__main__":
    main()