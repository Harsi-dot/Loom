# calculator.py
import math

def evaluate_expression(expression, x_val):
  
    try:
      
        return eval(expression, {"math": math, "x": x_val})
    except Exception:
       
        return None

def generate_graph_points(expression, canvas_width, origin_x, origin_y, scale_x, scale_y):
  
    points = []
    
    for pixel_x in range(canvas_width):
      
        x = (pixel_x - origin_x) / scale_x
        
        
        y_val = evaluate_expression(expression, x)
        
        if y_val is not None:
        
            pixel_y = origin_y - (y_val * scale_y)
            points.append((pixel_x, pixel_y))
            
    return points
