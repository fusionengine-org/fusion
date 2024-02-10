# Contributing rules
We are happy and welcome if you want to contribute to fusion engine. But please consider a few details before continuing:
1. Branch: Please when working on your fork, work in the dev branch, because we only will accept commits to the dev branch. It will later be released with the next version of fusion.
2. Explain: Please explain why this should be considered and merged. That will make our life easier.
3. Test: Please test your code before even opening a new pull request. 
4. Documentation: Please, if your adding something new, like a feature, please document everything. 
5. Format: Please, run black for formatting of the code.

## Not following these rules
If we see a pull request that doesn't follow these rules, we will tell you that, and close the pull request. 
We allow you to re-open a new pull request, but we expect you to have your code fixed.
So make sure that you followed [the rules](#contributing-rules)

## Some technologies we are using
- PDM: We are using pdm for our main interaction with the library.
- pyproject.toml: Pythons way for setting up a project. A replacement for setup.py
- pygame-ce: Used for windowing and events
- FusionGL (ctypes): Used for rendering everything. Its a custom wrapper around OpenGL for python
- pymunk: Will be used for physics
- black: We are using black to format code

## How to setup the work environment
If you want to contribute, you got to setup the work environment, so you can develop fusion the right way. First, install PDM using pip:
```bash
pip install --user pdm
```
PDM will manage everything for us, like virtual enviorments, packages and scripts.

Then, fork [the repository](https://github.com/fusionengine-org/fusion) to your profile.

Then, clone your forked github repository:
```bash
git clone https://github.com/your_username_/fusion.git
cd fusion-engine
```
Then, change the branch to the dev branch to follow rule #1:
```bash
git checkout dev
```

After that we need to run a special PDM command for creating the venv with the dev dependencies:
```bash
pdm install --dev
```
This will create a .venv, with all dependencies needed and will install a editable version of fusion engine. This will have the same effect as `pip install -e .`.

To test if it works properly, run one of the example using PDM:
```bash
pdm run example1
```

If you want to test documentation code, run the mkdocs command for starting a local server with the documentation. Run it with:
```bash
pdm run docs
```

If you want to run some specific files, then just run:
```bash
pdm run your_file.py
```

## Pull Request
If you're ready with your changes, then you must follow a few steps before pull requesting.
First, run black using PDM to format your code:
```bash
pdm run lint
```

Then make sure your pull request code works without erroring and you followed the [contribution rules](#contributing-rules)

After all of this, you can create a pull request and one of our main organisation members will look at it.