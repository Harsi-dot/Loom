# main.py
import tkinter as tk
from ui import CalculatorUI
from calculator import generate_graph_points

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        
        self.ui = CalculatorUI(self.root, self.handle_plot)
        
        
        self.scale_x = 40
        self.scale_y = 40

       
        self.root.update_idletasks()
        self.handle_plot()

    def handle_plot(self):
        
        expr = self.ui.entry.get()
        
        
        self.ui.draw_grid()
        
        
        w = self.ui.canvas.winfo_width() if self.ui.canvas.winfo_width() > 1 else self.ui.canvas_width

       
        points = generate_graph_points(
            expr, w, self.ui.origin_x, self.ui.origin_y, self.scale_x, self.scale_y
        )

       
        self.ui.draw_curve(points)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Controller()
    app.run()
