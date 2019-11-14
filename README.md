# AirBnB_clone
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
# <a href="https://ibb.co/n0F13LS"><img src="https://www.pngkey.com/png/full/60-605967_airbnb-logo-png.png" alt="Sin-ti-tulo-1" width="100" height="80" border="0"></a> Airbnb console

<a href="https://holbertonschool.com"><img src="https://i.ibb.co/RyBcXY6/cherry72.png" align="right" width="200" height="200" alt="cherry72" border="0"></a>

## General Description
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
By this project we have learned how to create a console which classes allows us
to handle information like Users, places, states, cities and others ones.

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

* A website (the front-end) that shows the final product to everybody: static and dynamic

* A database or files that store data (data = objects)

* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Console Objectives

 * Create our data model
 * Manage (create, update, destroy, etc) objects via a console / command interpreter
 * Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine
will give us an abstraction between “My object” and “How they are stored and
persisted”. This means: from our console code (the command interpreter itself)
and from the front-end and RestAPI you will build later, We won’t have to pay
attention (take care) of how our objects are stored.

This abstraction will also allow us to change the type of storage easily without
updating all of your codebase.

The console will be a tool to validate this storage engine

## Table of contents
* [Requirements](#requirements)
* [Instalation](#instalation)
* [Execution](#execution)
* [Written in](#written-in)
* [Example of use](#example-of-use)
* [Files and functions](#files-and-functions)
* [Authors](#authors)
## Requirements
* Ubuntu 14.04 LTS
* Python Scripts:
  - Shebang: 
    ```sh
    #!/usr/bin/python3
    ```
  - PEP 8
  - Documentation:
    ```sh
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
    ```sh
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    ```
    ```sh
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    ```
    ```sh
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    ```
* Python Unit Tests
  - Folder tests
  - Unittest module
  - Extension: .py
  - Test execution:
    ```sh
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base_model.py
    python3 -c 'print(__import__("my_module").__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
     ```
  
## Instalation
*  Clone this repository:
```sh
https://github.com/Doniben/AirBnB_clone.git
```
* Inside the repository:
* Execute:
```sh
./console.py 
```
## Written in
* GNU Emacs 24.3.1
* Python 3.4.3
## Example of use
```sh
(hbnb) help
```
<a href="https://ibb.co/SvgJHZ5"><img src="https://i.ibb.co/ryhvqXF/Screen-Shot-2019-11-13-at-10-05-18-PM.png" alt="Screen-Shot-2019-11-13-at-10-05-18-PM" border="0"></a>

```sh
(hbnb) Create User
```
```sh
show User 1881b0a8-91c9-4da2-b584-757697ccee56
```
<a href="https://ibb.co/82BdVV9"><img src="https://i.ibb.co/BjPrRRB/Screen-Shot-2019-11-13-at-10-10-24-PM.png" alt="Screen-Shot-2019-11-13-at-10-10-24-PM" border="0"></a>

All commands and builtins that you can use are in the help command.

### Authors

 - [Jose Marulanda](https://github.com/JoseMarulanda) - 967@holbertonschool.com
 - [Doniben Jimenez](https://github.com/Doniben) - 921@holbertonschool.com
