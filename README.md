# 🎮 Fusion Engine

## Introduction

![logo](https://user-images.githubusercontent.com/106883655/233103547-5693b2a3-22b9-4b68-ac2a-7220f16d48df.png)

Fusion is a game engine for creating graphical applications using the PySDL2 library and the programming language Python. It provides a simple coding interface for creating windows,
rendering graphics, and handling user input. It is and engine to create
games fast and easy!

### 💻 Development

Keep in mind that this project is in work, so if you want to see code,
then it is in dev branch but there is no 'full version' of this project!
We're working hard to make first alpha version of it!

## 💾 Installation

### Using PyPi

To install our package, run this:

```bash
  pip install fusion-engine
```

Our PyPI package is at this [link](<https://pypi.org/project/fusion-engine/>)

### Install from source

if you want to install the package from source then you do it like this:

```bash
 git clone https://github.com/dimkauzh/fusion-engine.git
 cd fusion-engine
 python setup.py install
```

### Developer build

if you want to get the latest changes then follow this instruction:

```bash
 git clone https://github.com/dimkauzh/fusion-engine.git
 cd fusion-engine
 python setup.py install_dev
```

### Run example

If you want to run the example, then just run this command:

```bash
 git clone https://github.com/dimkauzh/fusion-engine.git
 cd fusion-engine
 python examples/example1.py
```

For different examples, you change the number to the number of the example file

## 👥 Community

Our community is just growing, so if you want to help us with the project,
it will be very helpful!
We have a discord server at this [link](https://discord.gg/Smg3CK4ZMc).
Need to contact us? Just DM the Owner or CEO in discord and we will try to react as fast as possible

### ❤️ Special thanks to these people

- Zenthm (Contributing)
- XCarCedo (Contributing)
- Techsplosion (Bug hunter)
- FBS_Gamer (Discord server)

And our community of course!

## 📃 Documentation

See at [our website](https://dimkauzh.github.io/fusion-engine/)

## 📯 Coming features

### 🛠️ Features we are working on

We are working hard to implement very basic and complex stuff so our engine becomes more rigid. These features are worked on or will be worked on:

- [x] Engine
  - [x] Window
    - [x] Create window
    - [x] Get data from window
  - [x] Draw shapes
  - [x] Draw images
  - [x] Input
  - [x] Storage system
  - [x] Rendering options
  - [x] Delta-Time
  - [x] Pip package and SetupTools
  - [x] Cython
    - [x] Implement cython for extra speed
    - [x] Dev version without cython
  - [ ] Vectors (stores x and y coordinates)
    - [x] Create vector
    - [ ] Vector build into entity (vectors but with width and height)
  - [ ] Physics system using PyMunk
    - [x] Gravity
    - [x] Rendering
    - [ ] Collision system
    - [ ] Physics shapes
  - [ ] GUI library
    - [x] Text
    - [x] Drawing (Build in draw function)
    - [x] Buttons
    - [ ] And more...
  - [ ] Sound system
    - [ ] Sound player
    - [ ] File support
    - [ ] And more...
- [ ] CLI
  - [ ] Create CLI to build your game
  - [ ] Creates a full project
  - [ ] Will create a full project dir

### 🔩 Features that maybe will be implemented

- [ ] UI (Using own GUI library)
  - [ ] Menu
  - [ ] Create project
  - [ ] Editor
  - [ ] Code editor build in
  - [ ] Run game

💡 - If you have more ideas, please tell us them in our [discord group](https://discord.gg/Smg3CK4ZMc) or create an issue!

## License

See [Licence here](LICENCE.md)

## 🗄️ About

### ⚙️ Engine

Fusion Engine is currently (6/14/2023) build with Python and some Python libraries:

- PySDL2 is used for rendering and windowing
- PySDL2-DLL is used by PySDL2 for SDL2 binaries
- Cython for compiling and speed-up
- PyMunk is used for physics simulation
- Custom UI library based on PySDL2 for UI
- Setuptools for PyPi package
- Json for storing data

This project began May 1, 2023. The original project began in C, but it's entirely rewritten in Python for it's big userbase and ease of use (productivity). This is actually also my EuroPython 2023 project.

### 🇺🇦 Ukraine

We as fusion team support Ukraine and we hope it will win. Fusion engine is dedicated to Ukraine fighting the Russian invasion.
🇺🇦 Please support Ukraine! 🇺🇦

## 🚀 About Me

A 13-year-old game developer with much passion about game development. So I made this project to grow my programming skills and just make a tool that I can use for myself or a tool for other people to help them develop games.
