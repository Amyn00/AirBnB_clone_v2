# 0x02. AirBnB clone - MySQL

<img src="https://github.com/Amyn00/AirBnB_clone/blob/master/images/hbnb.png" height="200" width="1000"/>

## Description
The AirBnB Clone project is a simplified replica of the popular vacation rental platform Airbnb. It is designed to demonstrate the functionality of a command-line-based property rental system, where users can create, manage, and book properties.

## Command Interpreter

The command interpreter is a text-based interface that allows users to interact with the AirBnB Clone system. It provides a set of commands to manage properties, users, and bookings. These commands include creating new properties, viewing property details, booking properties, and more.

### How to Start

To start the AirBnB Clone command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Amyn00/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the commande interpreter:
   ```bash
   ./console.py
   ```

### How to Use
Once the command interpreter is running, you can use various commands to interact with the AirBnB Clone system. Here are some common commands:

* `create`: Create a new property or user.
* `show`: Display details of a property or user.
* `all`: List all properties or users.
* `book`: Book a property for a specific date range.
* `quit`: Exit the command interpreter.
For detailed information on available commands and their usage, you can use the help command within the interpreter.

**Examples**
Here are some examples of how to use the AirBnB Clone command interpreter:
1. Creating a new property:
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
2. Showing instance:
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
3. Listing all instances:
```bash
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
```
