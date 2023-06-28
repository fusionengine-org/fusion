# Fusion Engine

![logo](https://user-images.githubusercontent.com/106883655/233103547-5693b2a3-22b9-4b68-ac2a-7220f16d48df.png)

Fusion is a game engine for creating graphical applications using the PySDL2 library and the programming language Python. It provides a simple coding interface for creating windows,
rendering graphics, and handling user input. It is and engine to create
games fast and easy!

## Development

Keep in mind that this project is in work, so if you want to see code,
then it is in dev branch but there is no 'full version' of this project!
I'm working hard to make first alpha version of it!

First make sure you have everything installed, see chapter Installation.
Currently, in the folder example is a file called example.py This the file where you put your code in and import the engine file. Later it will become a library, but for now it is easier to develop the engine like this To run it just run the ```make example```

## Installation

#### Setup (easiest)

To get this into your project, you just get this repository into your
directory by running these command:

```bash
  git clone https://github.com/dimkauzh/fusion-engine
  cd fusion-engine
```

You need to have Python installed.
Make sure you have these apps/libraries installed: PySDL2 and PySDL2-DLL.
The easiest way to do that is to use our toolchain, here is how:

```bash
  make setup
```

This will create a virtual enviorment with PySDL2, PySDL2-DLL and PyInstaller

If you want to run the example, then just run this command:

```bash
 make example
```

For different examples, you add ```EXAMPLE=2``` and you change the number to the number of the example file

#### Own Install

If you want the libraries for yourself, then run these commands:

```bash
  pip install pysdl2
  pip install pysdl2-dll
```

## Community

Our community is just growing, so if you want to help us with the project,
it will be very helpful!
We have a discord server at this link (<https://discord.gg/Smg3CK4ZMc>)
Need to contact us? Just DM the Owner or CEO in discord and we will try to react as fast as possible

## Documentation

See at [The wiki of the project](https://github.com/dimkauzh/fusion-engine/wiki) (Still in work!)

## Coming features
We are working hard to implement very basic and complex stuff so our engine becomes more rigid. These features are worked on or will be worked on:
- Fysics system using PyMunk
- Delta-Time (Finished!)
- Set FPS functions
- Pip package
- Ui
- If you have more ideas, please tell us them in our discord group!

## About

Fusion Engine is currently (6/14/2023) build with Python and some Python libraries:

- PySDL2 is used for rendering and windowing
- PySDL2-DLL is used by PySDL2 for SDL2 binaries
- PyMunk is used for fysics simulation
- CX-Freeze is used for building executables

### Future of this engine

Because this project only began 1 may 2023, we don't have a big progress because I, Dimkauzh am the only developer, and we have one person that is working on discord moderating (Finn) and BIG Thanks to him for doing that. The original project began in C, but it's entirely rewritten in Python for it's big userbase and ease of use (productivity). This is actually also my EuroPython project.

Our cool ideas:

- Make a full GUI app (With something like Kyvi)

## 🚀 About Me

A 13 year old game developer with much passion about game development. So I made this project to grow my programming skills and just make a tool that I can use for myself or a tool for other people to help them develop games.
