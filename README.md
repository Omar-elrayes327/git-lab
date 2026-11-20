# Friendly Greeting App

A small Python command-line app that prints a greeting. You can choose a name,
print the greeting in uppercase, or repeat it.

## Requirements

- Python 3

The app uses only Python's standard library; no package installation is needed.

## Usage

Run the app from the project directory:

```text
python app.py
```

By default, it prints:

```text
Hello, world!
```

Provide a name as an optional positional argument:

```text
python app.py Omar
```

Use `--uppercase` to capitalize the greeting:

```text
python app.py Omar --uppercase
```

Use `--times N` to print it more than once. `N` must be a positive integer:

```text
python app.py Omar --times 3
```

Options can be combined:

```text
python app.py Omar --uppercase --times 2
```

For all available arguments, run:

```text
python app.py --help
```