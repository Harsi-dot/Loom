# ui.py
import tkinter as tk

class CalculatorUI:
    def __init__(self, root, plot_callback):
        self.root = root
        self.root.title("Loom Graphing Calculator")
        self.root.geometry("800x500")
        self.root.configure(bg="#1e1e2e")

        
        self.plot_callback = plot_callback

      
        self.control_frame = tk.Frame(root, bg="#1e1e2e", padx=15, pady=15)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas_frame = tk.Frame(root, bg="#11111b")
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        
        self.canvas_width = 550
        self.canvas_height = 450
        self.canvas = tk.Canvas(self.canvas_frame, width=self.canvas_width, height=self.canvas_height, bg="#11111b", highlightthickness=0)
        self.canvas.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

        
        self.origin_x = self.canvas_width // 2
        self.origin_y = self.canvas_height // 2

       
        tk.Label(self.control_frame, text="Graphing Engine", font=("Arial", 14, "bold"), fg="#cdd6f4", bg="#1e1e2e").pack(pady=(0, 15))
        tk.Label(self.control_frame, text="Enter Equation f(x):", fg="#a6adc8", bg="#1e1e2e", font=("Arial", 10)).pack(anchor="w")

        self.entry = tk.Entry(self.control_frame, font=("Courier New", 12), width=22, bg="#313244", fg="#cdd6f4", insertbackground="white")
        self.entry.insert(0, "math.sin(x) * 2")
        self.entry.pack(pady=(0, 15))

       
        self.plot_btn = tk.Button(self.control_frame, text=" Plot Graph", font=("Arial", 11, "bold"), bg="#a6e3a1", fg="#11111b", activebackground="#94e2d5", command=self.plot_callback, cursor="hand2")
        self.plot_btn.pack(fill=tk.X, pady=5)

    def draw_grid(self):
        
        self.canvas.delete("all")
        w = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else self.canvas_width
        h = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else self.canvas_height
        
        self.origin_x = w // 2
        self.origin_y = h // 2

        
        spacing = 40
        for i in range(0, w, spacing):
            self.canvas.create_line(i, 0, i, h, fill="#252538", width=1)
        for i in range(0, h, spacing):
            self.canvas.create_line(0, i, w, i, fill="#252538", width=1)

        
        self.canvas.create_line(0, self.origin_y, w, self.origin_y, fill="#585b70", width=2)
        self.canvas.create_line(self.origin_x, 0, self.origin_x, h, fill="#585b70", width=2)

    def draw_curve(self, points):
        
        h = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else self.canvas_height
        
        if len(points) > 1:
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i+1]
                
                
                if 0 <= y1 <= h and 0 <= y2 <= h:
                    self.canvas.create_line(x1, y1, x2, y2, fill="#89b4fa", width=3, smooth=True)
