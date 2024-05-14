import tkinter as tk
from tkinter import ttk

def open_filters():
    from filters import filters_window
    root.destroy()
    filters_window()

def open_edgedetectors():
    from edge_detection import edge_detectors
    root.destroy()
    edge_detectors()

def open_morphological_operations():
    from morphological_operations import morphological_operations_window
    root.destroy()
    morphological_operations_window()

def open_segmentation_window():
    from segmentaion import segmentation_window
    root.destroy()
    segmentation_window()

def main_window():
    global root
    root = tk.Tk()
    root.title("Image Processing Project")

    # Set window dimensions
    window_width = 800
    window_height = 768

    # Calculate window position to center it on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set window geometry
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create a label for the top
    top_label = ttk.Label(root, text="Image Processing Project", font=("Arial", 36))
    top_label.pack(side=tk.TOP, pady=(100, 0))  # Adjust top padding

    # Create a frame for the buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(expand=True, padx=20, pady=(0, 20))  # Adjust horizontal and bottom padding

    # Create buttons
    button1 = ttk.Button(button_frame, text="Filters", style="Fancy.TButton", command=open_filters)
    button2 = ttk.Button(button_frame, text="Edge Detectors", style="Fancy.TButton", command= open_edgedetectors)
    button3 = ttk.Button(button_frame, text="Morphological Operations", style="Fancy.TButton", command= open_morphological_operations)
    button4 = ttk.Button(button_frame, text="Segmentation", style="Fancy.TButton", command=open_segmentation_window)

    # Pack buttons
    button1.pack(fill=tk.X, pady=10)
    button2.pack(fill=tk.X, pady=10)
    button3.pack(fill=tk.X, pady=10)
    button4.pack(fill=tk.X, pady=10)

    # Configure style for the buttons
    style = ttk.Style()
    style.configure("Fancy.TButton",
                    foreground="black",
                    background="blue",
                    font=("Arial", 12),
                    padding=25)

    root.mainloop()

if __name__ == "__main__":
    main_window()
