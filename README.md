# 0x00. AirBnB_clone - The console

## Description

A project to build a clone of AirBnB_clone console.


Each task is linked and will help to:
 - Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of my future instances.
 - Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
 - Create all classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel.
 - Create the first abstracted storage engine of the project: File storage.
 - Create all unit tests to validate all my classes and storage engine.


## Command Interpreter

The console is a command interpreter to manage objects of the product:
 - Create a new object (ex: a new User or new Place).
 - Retrieve an object from a file, a database, etc.
 - Do operations on objects (count, compute stats, etc.).
 - Update attributes of an obbject.
 - Destroy an object.
