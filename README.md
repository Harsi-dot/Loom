# Loom
Loom is an interactive, lightweight graphing calculator built completely from scratch in Python using standard libraries. Loom provides an intuitive interface to visualize algebraic, trigonometric, and logarithmic functions natively in a dark-mode desktop window. Because this engine runs on Python, equations must follow Python's math standards.
1. `main.py` : Acting as the controller, it initializes the application state, manages the zoom/scaling coefficients, and handles data binding between the view and the model.
2. `ui.py`: Built on Python's native `tkinter` framework, this component manages the custom coordinate rendering canvas, physical pixel wrapping bounds, and structural grid layout.
3. `calculator.py`: The calculation core. It converts screen pixel column arrays into mathematical values, processes strings using localized execution environments, and yields coordinate coordinate sets.
Loom is built for hackability! Hack Club members can fork the codebase and pick up the following development vectors from our tracking issues pipeline:
•	Feature/Safe-Parser: Migrating the math module evaluation from a localized wrapper approach to a fully sandboxed token parser (abstract syntax trees) to rule out illegal code strings entirely.
•	Feature/Dynamic-Zoom: Implementing mouse scrolling scroll listeners (<Button-4> / <Button-5>) to modify canvas scale constants and re-trigger plots dynamically.
•	UI/Button-Pad: Adding an automated layout grid on the left interface sidebar for direct button input entry fields.
