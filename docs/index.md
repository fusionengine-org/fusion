

<h1 align="center">🚀 Fusion Engine</h1>
<p align="center">
<a href="https://pypi.org/project/fusion-engine"><img alt="PyPI" src="https://img.shields.io/pypi/v/fusion-engine"></a>
<a href="https://pypi.org/project/fusion-engine"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fusion-engine"></a>
<a href="https://pypi.org/project/fusion-engine"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/fusion-engine?color=blue"></a>
</p>


<p align="center">
  <img src="https://user-images.githubusercontent.com/106883655/233103547-5693b2a3-22b9-4b68-ac2a-7220f16d48df.png" alt="logo">
</p>


Fusion is a free open-source game engine for creating graphical applications using the PySDL2 library and the programming language Python. It provides a simple coding interface for creating windows, rendering graphics, and handling user input. It is an engine to create games fast and easy!

## 📚 This Website

We made this website only for the docs, and nothing more. Here you can find the docs for the Fusion Engine API. Please keep in mind Fusion Engine is unfinished.

## 📖 Wiki

Welcome to the Fusion Engine wiki!
Here you will find everything you need to start with Fusion Engine! For examples, you can find them on the example page, and for the API, look into the API page.
Because Fusion Engine is under development, this wiki won't be updated frequently, and some pages might be unfilled.

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

### 💻 Using it for Your Project

To install it run this:

```bash
  pip install fusion-engine
```

Then import:

```python
  import fusionengine as engine
```

And after that you need to create a object of our engine to run functions of it:

```python
  main = engine.Main()
```

Click next to go to the next page!

[Next](wiki/api.md)
