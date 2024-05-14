import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

def open_main_window():
    from main import main_window
    morphological_operations_win.destroy()
    main_window()


# Define the image processing functions
def apply_erosion():
    global original_image
    global current_image
    
    # Convert the current image to a numpy array
    image_np = np.array(original_image)
    
    # Convert the image to grayscale if it's not already in grayscale
    if len(image_np.shape) == 3:
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image_np
    
    # Apply erosion
    kernel = np.ones((5,5),np.uint8)  # Define a 5x5 kernel
    erosion_image = cv2.erode(gray_image, kernel, iterations=1)
    
    # Convert the result back to RGB if necessary
    if len(image_np.shape) == 3:
        erosion_image_rgb = cv2.cvtColor(erosion_image, cv2.COLOR_GRAY2RGB)
    else:
        erosion_image_rgb = erosion_image
    
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(erosion_image_rgb))
    image_label.configure(image=current_image)


def apply_dilation():
    global original_image
    global current_image
    
    # Convert the current image to a numpy array
    image_np = np.array(original_image)
    
    # Convert the image to grayscale if it's not already in grayscale
    if len(image_np.shape) == 3:
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image_np
    
    # Apply dilation
    kernel = np.ones((5,5),np.uint8)  # Define a 5x5 kernel
    dilation_image = cv2.dilate(gray_image, kernel, iterations=1)
    
    # Convert the result back to RGB if necessary
    if len(image_np.shape) == 3:
        dilation_image_rgb = cv2.cvtColor(dilation_image, cv2.COLOR_GRAY2RGB)
    else:
        dilation_image_rgb = dilation_image
    
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(dilation_image_rgb))
    image_label.configure(image=current_image)


def apply_open():
    global original_image
    global current_image
    
    # Convert the current image to a numpy array
    image_np = np.array(original_image)
    
    # Convert the image to grayscale if it's not already in grayscale
    if len(image_np.shape) == 3:
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image_np
    
    # Apply opening (erosion followed by dilation)
    kernel = np.ones((5,5),np.uint8)  # Define a 5x5 kernel
    opening_image = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)
    
    # Convert the result back to RGB if necessary
    if len(image_np.shape) == 3:
        opening_image_rgb = cv2.cvtColor(opening_image, cv2.COLOR_GRAY2RGB)
    else:
        opening_image_rgb = opening_image
    
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(opening_image_rgb))
    image_label.configure(image=current_image)

def apply_close():
    global original_image
    global current_image
    
    # Convert the current image to a numpy array
    image_np = np.array(original_image)
    
    # Convert the image to grayscale if it's not already in grayscale
    if len(image_np.shape) == 3:
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    else:
        gray_image = image_np
    
    # Apply closing (dilation followed by erosion)
    kernel = np.ones((5,5),np.uint8)  # Define a 5x5 kernel
    closing_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)
    
    # Convert the result back to RGB if necessary
    if len(image_np.shape) == 3:
        closing_image_rgb = cv2.cvtColor(closing_image, cv2.COLOR_GRAY2RGB)
    else:
        closing_image_rgb = closing_image
    
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(closing_image_rgb))
    image_label.configure(image=current_image)

def apply_hough_circle_transform():
    global original_image
    global current_image
    
    # Convert the current image to a numpy array
    image_np = np.array(original_image)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Apply Hough Transform for circle detection
    circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)
    
    # Draw detected circles on the original image
    hough_image = np.copy(image_np)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            # Draw the outer circle
            cv2.circle(hough_image, center, radius, (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(hough_image, center, 2, (0, 0, 255), 3)
    
    # Convert the result back to RGB
    hough_image_rgb = cv2.cvtColor(hough_image, cv2.COLOR_BGR2RGB)
    
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(hough_image_rgb))
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

def morphological_operations_window():
    global image_label
    global original_image
    global morphological_operations_win
    # Create the main window
    morphological_operations_win = tk.Tk()

    # Set the dimensions of the window
    window_width = 1024
    window_height = 768

    # Calculate the screen width and height
    screen_width = morphological_operations_win.winfo_screenwidth()
    screen_height = morphological_operations_win.winfo_screenheight()

    # Calculate the position of the window to center it on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the geometry of the window
    morphological_operations_win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set the title of the window
    morphological_operations_win.title("Image Processing Project")

    # Create a label for the filters
    filters_label = ttk.Label(morphological_operations_win, text="Morphological Operations", font=("Arial", 36), padding=30)
    filters_label.pack(side=tk.TOP, pady=10)

    # Create a frame for buttons
    button_frame = ttk.Frame(morphological_operations_win)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=70, pady=(15, 80))


    # Create buttons
    button1 = ttk.Button(button_frame, text="Erosion", style="Fancy.TButton", command=apply_erosion)
    button2 = ttk.Button(button_frame, text="Dilation", style="Fancy.TButton", command=apply_dilation)
    button3 = ttk.Button(button_frame, text="Open", style="Fancy.TButton", command=apply_open)
    button4 = ttk.Button(button_frame, text="Close", style="Fancy.TButton", command=apply_close)
    button5 = ttk.Button(button_frame, text="Hough Circle Transform", style="Fancy.TButton", command=apply_hough_circle_transform)
    button6 = ttk.Button(button_frame, text="Original Image", style="Fancy.TButton", command=get_original_image)
    button7 = ttk.Button(button_frame, text="Back To Main", style="Fancy.TButton", command= open_main_window)

    # Pack buttons
    button1.pack(fill=tk.X, pady=10)
    button2.pack(fill=tk.X, pady=10)
    button3.pack(fill=tk.X, pady=10)
    button4.pack(fill=tk.X, pady=10)
    button5.pack(fill=tk.X, pady=10)
    button6.pack(fill=tk.X, pady=10)
    button7.pack(fill=tk.X, pady=10)

    # Create a frame for the image
    image_frame = tk.Frame(morphological_operations_win, bd=2, relief="ridge")  # Add a dashed border with a little padding
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
    morphological_operations_win.mainloop()
