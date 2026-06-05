# Loom
Loom is an interactive, lightweight graphing calculator built completely from scratch in Python using standard libraries. Loom provides an intuitive interface to visualize algebraic, trigonometric, and logarithmic functions natively in a dark-mode desktop window. Because this engine runs on Python, equations must follow Python's math standards.
1. `main.py` : Acting as the controller, it initializes the application state, manages the zoom/scaling coefficients, and handles data binding between the view and the model.
2. `ui.py`: Built on Python's native `tkinter` framework, this component manages the custom coordinate rendering canvas, physical pixel wrapping bounds, and structural grid layout.
3. `calculator.py`: The calculation core. It converts screen pixel column arrays into mathematical values, processes strings using localized execution environments, and yields coordinate coordinate sets.
