import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

def open_main_window():
    from main import main_window
    edge_detector_window.destroy()
    main_window()

# Define the image processing functions
def apply_roberts_edge_detector():
    global original_image
    global current_image
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)
    # Apply Roberts edge detector
    roberts_image = cv2.Canny(gray_image, 100, 200)  # You can adjust the threshold values as needed
    # Convert back to RGB
    roberts_image_rgb = cv2.cvtColor(roberts_image, cv2.COLOR_GRAY2RGB)
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(roberts_image_rgb))
    image_label.configure(image=current_image)


def apply_prewitt_edge_detector():
    global original_image
    global current_image
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)
    # Apply Prewitt edge detector
    prewitt_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    prewitt_magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
    prewitt_image = cv2.normalize(prewitt_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(prewitt_image))
    image_label.configure(image=current_image)


def apply_sobel_edge_detector():
    global original_image
    global current_image
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)
    # Compute the horizontal and vertical gradients using Sobel operators
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    # Compute the magnitude of gradients
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    # Normalize the gradient magnitude image
    sobel_image = cv2.normalize(sobel_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(sobel_image))
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


def edge_detectors():
    global original_image
    global image_label
    global edge_detector_window
    # Create the main window
    edge_detector_window = tk.Tk()

    # Set the dimensions of the window
    window_width = 1024
    window_height = 768

    # Calculate the screen width and height
    screen_width = edge_detector_window.winfo_screenwidth()
    screen_height = edge_detector_window.winfo_screenheight()

    # Calculate the position of the window to center it on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the geometry of the window
    edge_detector_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set the title of the window
    edge_detector_window.title("Image Processing Project")

    # Create a label for the filters
    filters_label = ttk.Label(edge_detector_window, text="Edge Detection", font=("Arial", 36), padding=30)
    filters_label.pack(side=tk.TOP, pady=10)

    # Create a frame for buttons
    button_frame = ttk.Frame(edge_detector_window)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=70, pady=80)


    # Create buttons
    button1 = ttk.Button(button_frame, text="Roberts edge detector", style="Fancy.TButton", command=apply_roberts_edge_detector)
    button2 = ttk.Button(button_frame, text="Prewitt edge detector", style="Fancy.TButton", command=apply_prewitt_edge_detector)
    button3 = ttk.Button(button_frame, text="Sobel edge detector", style="Fancy.TButton", command=apply_sobel_edge_detector)
    button4 = ttk.Button(button_frame, text="Original Image", style="Fancy.TButton", command=get_original_image)
    button5 = ttk.Button(button_frame, text="Back To Main", style="Fancy.TButton", command=open_main_window)

    # Pack buttons
    button1.pack(fill=tk.X, pady=10)
    button2.pack(fill=tk.X, pady=10)
    button3.pack(fill=tk.X, pady=10)
    button4.pack(fill=tk.X, pady=10)
    button5.pack(fill=tk.X, pady=10)

    # Create a frame for the image
    image_frame = tk.Frame(edge_detector_window, bd=2, relief="ridge")  # Add a dashed border with a little padding
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
    edge_detector_window.mainloop()
