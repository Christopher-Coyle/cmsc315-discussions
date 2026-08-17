"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SmartDevice:
    device_category = "Smart Home Device"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return (
            f"Device: {self.name}, Location: {self.location}, "
            f"Category: {self.device_category}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SecurityCamera(SmartDevice):
    manufacturer = "SecureHome Technologies"

    def __init__(self, name, location, resolution, settings=None):
        super().__init__(name, location)
        self.resolution = resolution
        self.recording = False
        self.settings = (
            settings
            if settings is not None
            else {"alerts": ["motion"], "night_vision": True}
        )

    def start_recording(self):
        self.recording = True

    def stop_recording(self):
        self.recording = False

    def display_info(self):
        return (
            f"Device: {self.name}, Location: {self.location}, "
            f"Resolution: {self.resolution}, Recording: {self.recording}, "
            f"Manufacturer: {self.manufacturer}"
        )

    # Student-created extension:
    # This method provides a simple operational status summary.
    def status_report(self):
        alert_types = ", ".join(self.settings["alerts"])
        return (
            f"{self.name} status -> Recording: {self.recording}, "
            f"Night vision: {self.settings['night_vision']}, "
            f"Alerts: {alert_types}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    front_camera = SecurityCamera("Front Camera", "Front Door", "4K")
    garage_camera = SecurityCamera("Garage Camera", "Garage", "1080p")

    print("Class variable through class:")
    print(SecurityCamera.manufacturer)

    print("\nSame class variable through an object:")
    print(front_camera.manufacturer)

    # Add an attribute only to front_camera's instance namespace.
    front_camera.install_date = "2026-08-15"

    print("\nFront camera instance namespace:")
    print(front_camera.__dict__)

    print("\nGarage camera instance namespace:")
    print(garage_camera.__dict__)

    print("\nSelected SecurityCamera class namespace entries:")
    for key in (
            "manufacturer",
            "__init__",
            "start_recording",
            "stop_recording",
            "display_info",
            "status_report",
    ):
        print(f"{key}: {SecurityCamera.__dict__[key]}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = SecurityCamera(
        "Backyard Camera",
        "Backyard",
        "4K",
        {"alerts": ["motion", "person"], "night_vision": True},
    )

    shallow_camera = copy(original)
    deep_camera = deepcopy(original)

    # A shallow copy creates a new outer object, but nested mutable data
    # remains shared. Therefore, changing the original nested alerts list
    # is also visible through shallow_camera.
    #
    # A deep copy recursively duplicates nested mutable data. Therefore,
    # deep_camera keeps its own independent copy of the alerts list.
    original.settings["alerts"].append("vehicle")

    print("Original settings:")
    print(original.settings)

    print("\nShallow-copy settings:")
    print(shallow_camera.settings)

    print("\nDeep-copy settings:")
    print(deep_camera.settings)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nParent object:")
    thermostat = SmartDevice("Hallway Thermostat", "Hallway")
    print(thermostat.display_info())

    print("\nChild object:")
    camera = SecurityCamera("Entry Camera", "Front Door", "4K")
    print(camera.display_info())

    camera.start_recording()
    print(camera.display_info())

    # Student-created extension demonstration.
    print(camera.status_report())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()