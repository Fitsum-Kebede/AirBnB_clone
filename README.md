# AirBnB clone project

![AirBnB](utils/images/65f4a1dd9c51265f49d0_hu98d6ceda137062fd4edf4a7d705e7570_76537_700x0_resize_box_3.png)
## Welcome to the AirBnB clone project!

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [The console](#The-console)
- [Setup and Usage](#setup-and-usage)


# Introduction:
Welcome to the Airbnb Clone Project! This application is designed to
replicate the core functionalities of the popular accommodation booking platform,
Airbnb. The project aims to provide familiar and intuitive functionalities for:
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

This README is a guide through the features, technologies used, setup instructions, and more.

# Features

**Users(class)**: The following are to be used by the user:
           - show - ()
           - create - ()
           - destroy - ()
           - update
           - all - ()
**Console(command interpreter)**: Manages the objects of User class.
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Technologies Used
- **Frontend**: (Nothing yet)
- **Backend**: Python
- **Database**: File Storage.
- **Version Control**: Git, GitHub
- Here is the flow of the backend.

  
![](utils/images/815046647d23428a14ca_hu68774d5216c48b4f424f088e55e7a2ed_118703_700x0_resize_box_3.png)

# The console
The console is a command-line interpreter that allows users to manage and manipulate instances of various classes in an application. The primary purpose of this script is to provide a way to interact with and manipulate objects by executing specific commands. The script operates within a command loop, where users can enter commands to create, retrieve, update, and delete instances of different classes.


# Setup and Usage
The command interpreter supports a variety of operations for managing objects within the application. It enables users to interact with the data model in a structured way. Below are the key operations that can be performed using this command interpreter:
* Create: Create a new instance of a specified class.
* Show: Retrieve and display information about a specific instance based on its class and ID.
* Destroy: Delete a specific instance based on its class and ID.
* All: Display information about all instances or instances of a specific class.
* Update: Update attributes of a specific instance based on its class and ID.
* Count: Count the number of instances of a specific class.
* Quit/Exit: Terminate the command interpreter.

## Setup

Setting up an Airbnb console involves preparing the environment, importing necessary modules,
and then interacting with the classes and methods you've implemented in your project. Here's a step-by-step
guide along with clear examples:

Open a terminal on your system and clone the repo.
```
$ git clone https://github.com/Fitsum-Kebede/AirBnB_clone.git
```
Use the cd command to navigate to the root directory of your Airbnb project.
```
$ cd AirBnB_clone
```
## Usage

Run the console to manage instances
```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
The following are classes and operation that be performed on the classes using the console.
### classes
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review
### console commands
- create
- show
- destroy
- all
- update
- count

# create
Creates a new instance of a class, saves it (to the JSON file) and prints the id
```
(hbnb) create BaseModel
b65f6cd1-b671-4367-be06-43a02c3bc858
(hbnb) create User
d007cb77-50ed-4ae0-bfbe-68d6246c65b3
(hbnb) create State
1d8f655d-4aef-44f7-ab55-d4bd59918708
(hbnb) create City
dd02d053-3500-4156-b4eb-b7223cc40ec3
(hbnb) create Amenity
a63bc346-24fe-4cde-99ca-a608eb862811
(hbnb) create Place
6c94d8c2-07f4-4de5-905d-a3b988fe06e3
(hbnb) create Review
3eec0a79-415e-47bf-906d-e1a8594daae8
(hbnb) all
["[BaseModel] (b65f6cd1-b671-4367-be06-43a02c3bc858) {'id': 'b65f6cd1-b671-4367-be06-43a02c3bc858', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418067), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418116)}", "[User] (d007cb77-50ed-4ae0-bfbe-68d6246c65b3) {'id': 'd007cb77-50ed-4ae0-bfbe-68d6246c65b3', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79387), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79439)}", "[State] (1d8f655d-4aef-44f7-ab55-d4bd59918708) {'id': '1d8f655d-4aef-44f7-ab55-d4bd59918708', 'created_at': datetime.datetime(2023, 8, 14, 4, 34, 9, 219814), 'updated_at': datetime.datetime(2023, 8, 14, 4, 34, 9, 219875)}", "[City] (dd02d053-3500-4156-b4eb-b7223cc40ec3) {'id': 'dd02d053-3500-4156-b4eb-b7223cc40ec3', 'created_at': datetime.datetime(2023, 8, 14, 4, 34, 19, 255961), 'updated_at': datetime.datetime(2023, 8, 14, 4, 34, 19, 256009)}", "[Amenity] (a63bc346-24fe-4cde-99ca-a608eb862811) {'id': 'a63bc346-24fe-4cde-99ca-a608eb862811', 'created_at': datetime.datetime(2023, 8, 14, 4, 34, 30, 918674), 'updated_at': datetime.datetime(2023, 8, 14, 4, 34, 30, 918730)}", "[Place] (6c94d8c2-07f4-4de5-905d-a3b988fe06e3) {'id': '6c94d8c2-07f4-4de5-905d-a3b988fe06e3', 'created_at': datetime.datetime(2023, 8, 14, 4, 34, 43, 521618), 'updated_at': datetime.datetime(2023, 8, 14, 4, 34, 43, 521690)}", "[Review] (3eec0a79-415e-47bf-906d-e1a8594daae8) {'id': '3eec0a79-415e-47bf-906d-e1a8594daae8', 'created_at': datetime.datetime(2023, 8, 14, 4, 34, 50, 933325), 'updated_at': datetime.datetime(2023, 8, 14, 4, 34, 50, 933378)}"]
(hbnb)
```
# show
Prints the string representation of an instance based on the class name and id.
- It can either be used as **show \<class name\> \<id\>** or **\<class name\>.show(\<id\>)**.
- example:
```
(hbnb) show BaseModel b65f6cd1-b671-4367-be06-43a02c3bc858
[BaseModel] (b65f6cd1-b671-4367-be06-43a02c3bc858) {'id': 'b65f6cd1-b671-4367-be06-43a02c3bc858', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418067), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418116)}
(hbnb) BaseModel.show("b65f6cd1-b671-4367-be06-43a02c3bc858")
[BaseModel] (b65f6cd1-b671-4367-be06-43a02c3bc858) {'id': 'b65f6cd1-b671-4367-be06-43a02c3bc858', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418067), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 39, 418116)}
(hbnb) show User d007cb77-50ed-4ae0-bfbe-68d6246c65b3
[User] (d007cb77-50ed-4ae0-bfbe-68d6246c65b3) {'id': 'd007cb77-50ed-4ae0-bfbe-68d6246c65b3', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79387), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79439)}
(hbnb) User.show("d007cb77-50ed-4ae0-bfbe-68d6246c65b3")
[User] (d007cb77-50ed-4ae0-bfbe-68d6246c65b3) {'id': 'd007cb77-50ed-4ae0-bfbe-68d6246c65b3', 'created_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79387), 'updated_at': datetime.datetime(2023, 8, 14, 4, 33, 50, 79439)}
(hbnb)
```
# destroy
Deletes an instance based on the class name and id (save the change into the JSON file).
- It can either be used as **destroy \<class name\> \<id\>** or **\<class name\>.destroy(\<id\>)**.
- example:
```
(hbnb) create User
ddf5d0ec-9100-45d8-abba-fb6b126f376f
(hbnb) create User
6e202fc2-4f80-4425-ae03-684726dda42f
(hbnb) create User
0eb1d258-b314-490e-aee3-a0f935e98814
(hbnb) create User
4b05a6ba-8670-40cf-9dfd-036a3257b2a6
(hbnb) create User
de05db82-07fc-47ce-953e-3be6a737d495
(hbnb) User.count()
6
(hbnb) destroy User ddf5d0ec-9100-45d8-abba-fb6b126f376f
(hbnb) User.count()
5
(hbnb) destroy User ddf5d0ec-9100-45d8-abba-fb6b126f376f
** no instance found **
(hbnb) destroy User 6e202fc2-4f80-4425-ae03-684726dda42f
(hbnb) destroy User 6e202fc2-4f80-4425-ae03-684726dda42f
** no instance found **
(hbnb) User.count()
4
(hbnb) User.destroy("0eb1d258-b314-490e-aee3-a0f935e98814")
(hbnb) User.destroy("0eb1d258-b314-490e-aee3-a0f935e98814")
** no instance found **
(hbnb) User.destroy("4b05a6ba-8670-40cf-9dfd-036a3257b2a6")
(hbnb) User.destroy("4b05a6ba-8670-40cf-9dfd-036a3257b2a6")
** no instance found **
(hbnb) 
```

# contributors
- **Mcnores-Samuel** <samuelmcnores1@gmail.com>
- **fitsum-kebede** <fitsuminfome@gmail.com>

