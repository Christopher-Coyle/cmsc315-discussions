# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Implementation Summary

I implemented a `SmartDevice` parent class and a `SecurityCamera` child class. The parent class stored shared device information, while the child class inherited that functionality and added camera-specific state and behavior. I used method overriding so `SecurityCamera.display_info()` reported additional camera details.

I demonstrated class and instance namespaces by accessing a class variable through both the class and an object, adding an attribute to only one instance, and examining `__dict__` for the objects and class. I also demonstrated shallow and deep copying using nested mutable data in the camera's `settings` dictionary. The shallow copy shared the nested alerts list with the original object, while the deep copy maintained an independent copy.

As a student-created extension, I added a `status_report()` method that summarized recording status, night-vision status, and configured alert types.

## Reflection

While completing this assignment, I learned how inheritance, namespaces, method overriding, and object copying work together in Python. The namespace demonstration helped me see the difference between data stored on an individual object and data or methods stored at the class level. The copying exercise was especially useful because a shallow copy can appear independent while still sharing nested mutable data with the original object.

Compared with procedural programming, OOP introduces more structure and some additional overhead because classes, objects, and relationships must be designed before the program is implemented. That overhead can be worthwhile when an application grows. Shared behavior can be placed in a parent class, specialized behavior can be added in child classes, and changes can be isolated to the component responsible for them. This improves maintainability and reusability.

A practical use for this design would be a smart-home or IoT management system. Future device types could inherit common behavior from `SmartDevice` while implementing their own specialized methods without rewriting the entire application.

## Files

- `unit1_discussion.py` - completed Python implementation
- `README.md` - implementation documentation and reflection

## Verification

The program was run after implementation to verify that the parent and child objects, inheritance behavior, namespace demonstration, shallow-copy behavior, deep-copy behavior, and student-created extension executed correctly.