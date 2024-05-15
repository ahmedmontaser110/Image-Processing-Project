import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import importlib


def open_main_window():
    from main import main_window
    segmentation_win.destroy()
    main_window()


def apply_threshold_segmentation():
    global original_image
    global current_image

    threshold_value = 127

    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)

    # Apply binary thresholding
    _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Convert the thresholded image to format that tkinter can display
    current_image = ImageTk.PhotoImage(image=Image.fromarray(thresholded_image))

    # Update the image display
    image_label.configure(image=current_image)


def apply_edge_detection_segmentation():
    global original_image
    global current_image

    # Convert the original image to OpenCV format
    cv_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2BGR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray_image, (3, 3), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold1=30, threshold2=100)

    # Convert the edges image back to RGB format
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    # Convert the edge-detected image to format that tkinter can display
    current_image = ImageTk.PhotoImage(image=Image.fromarray(edges_rgb))

    # Update the image display
    image_label.configure(image=current_image)


def get_original_image():
    global original_image
    global current_image
    # Reload the original image
    original_image = Image.open("image.jpg")  
    original_image = original_image.resize((640, 480))  # Resize the image to fit within the frame
    # Convert the image to format that tkinter can display
    current_image = ImageTk.PhotoImage(image=original_image)
    # Update the image display
    image_label.configure(image=current_image)


def segmentation_window():
    global original_image
    global image_label
    global segmentation_win
    # Create the main window
    segmentation_win = tk.Tk()

    # Set the dimensions of the window
    window_width = 1024
    window_height = 768

    # Calculate the screen width and height
    screen_width = segmentation_win.winfo_screenwidth()
    screen_height = segmentation_win.winfo_screenheight()

    # Calculate the position of the window to center it on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the geometry of the window
    segmentation_win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set the title of the window
    segmentation_win.title("Image Processing Project")

    # Create a label for the filters
    filters_label = ttk.Label(segmentation_win, text="Segmentation", font=("Arial", 36), padding=30)
    filters_label.pack(side=tk.TOP, pady=10)

    # Create a frame for buttons
    button_frame = ttk.Frame(segmentation_win)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=70, pady=(110, 80))


    # Create buttons
    button1 = ttk.Button(button_frame, text="Threshold Segmentation", style="Fancy.TButton", command=apply_threshold_segmentation)
    button3 = ttk.Button(button_frame, text="Edge Detection Segmentation", style="Fancy.TButton", command=apply_edge_detection_segmentation)
    button4 = ttk.Button(button_frame, text="Original Image", style="Fancy.TButton", command=get_original_image)
    button5 = ttk.Button(button_frame, text="Back To Main", style="Fancy.TButton", command=open_main_window)

    # Pack buttons
    button1.pack(fill=tk.X, pady=10)
    button3.pack(fill=tk.X, pady=10)
    button4.pack(fill=tk.X, pady=10)
    button5.pack(fill=tk.X, pady=10)

    # Create a frame for the image
    image_frame = tk.Frame(segmentation_win, bd=2, relief="ridge")  # Add a dashed border with a little padding
    image_frame.place(relx=0.65, rely=0.5, anchor=tk.CENTER, width=640, height=480)  # Place the frame on the right side

    # Load and resize the image using Pillow
    original_image = Image.open("image.jpg") 
    original_image = original_image.resize((640, 480))  # Resize the image to fit within the frame

    # Convert the image to a format that tkinter can display
    current_image = ImageTk.PhotoImage(image=original_image)

    # Create a label to display the image
    image_label = tk.Label(image_frame, image=current_image)
    image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Add padding around the image

    # Create a style object
    style = ttk.Style()

    # Configure the style for the buttons
    style.configure("Fancy.TButton",
                    foreground="black",
                    background="blue",
                    font=("Arial", 12),
                    padding=10)

    # Run the Tkinter event loop
    segmentation_win.mainloop()
