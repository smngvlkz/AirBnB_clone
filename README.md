# 0x00. AirBnB Clone - The Console

## Description

This project is a clone of the AirBnB website. The first step towards building a full web application: the AirBnB clone. This step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Command Interpreter

The console works in both interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt **"(hbnb) "** and waits for the user for input.

To start the console, simply run:

```bash
./console.py
```

In non-interactive mode:

```bash
echo "help" | ./console.py
```

## Commands

The console supports the following commands:

- `create`: Creates a new object (ex: a new User or a new Place)
- `show`: Prints the string representation of an instance based on the class name and id
- `destroy`: Deletes an instance based on the class name and id
- `all`: Prints all string representation of all instances based or not on the class name
- `update`: Updates an instance based on the class name and id by adding or updating attribute

Type `help <command>` in the console for more info on each command.

## Tests

All code is tested with the **unittest** module. To run tests, navigate to the project root directory and run:

```bash
python3 -m unittest discover tests
```

## Additional Features and Steps taken to achieve the overrall functionality of the console

- **Create BaseModel from dictionary**: I created a method to generate a dictionary representation of an instance (`to_dict()`). Now I can re-create an instance with this dictionary representation.

- **Store first object**: Now I can recreate a BaseModel from another one by using a dictionary representation. I convert the dictionary representation to a JSON string.

- **Console 0.0.1**: I implemented a command interpreter for the clone. You can use it to manage your objects. It supports commands like `quit`, `EOF`, `help`, and it also has a custom prompt `(hbnb)`. An empty line + ENTER doesn’t execute anything.

- **Console 0.1**: I updated the command interpreter to include more commands: `create`, `show`, `destroy`, `all`, `update`. Each command has specific error handling for missing or incorrect arguments.

- **First User**: I added a User class that inherits from BaseModel. It has public class attributes for email, password, first_name, and last_name. I've also updated FileStorage to correctly serialize and deserialize User, and updated the command interpreter to allow `show`, `create`, `destroy`, `update` and `all` to be used with User.

- **More classes**: I added more classes that inherit from BaseModel: State, City, Amenity, Place, and Review. Each class has specific attributes.

- **Console 1.0**: I updated FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity, and Review. We've also updated the command interpreter to allow actions: `show`, `create`, `destroy`, `update` and `all` with all classes created previously.

- **All instances by class name**: I updated the command interpreter to retrieve all instances of a class by using: `<class name>.all()`.

- **Count instances**: I updated the command interpreter to retrieve the number of instances of a class: `<class name>.count()`.

- **Show**: I updated the command interpreter to retrieve an instance based on its ID: `<class name>.show(<id>)`.

- **Destroy**: I updated the command interpreter to destroy an instance based on his ID: `<class name>.destroy(<id>)`.

- **Update**: I updated the command interpreter to update an instance based on his ID: `<class name>.update(<id>, <attribute name>, <attribute value>)`.

- **Update from dictionary**: I updated the command interpreter to update an instance based on his ID with a dictionary: `<class name>.update(<id>, <dictionary representation>)`.


