import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

def open_main_window():
    from main import main_window
    filters_win.destroy()
    main_window()

# Define the image processing functions
def apply_hpf():
    global original_image
    global current_image
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Apply High Pass Filter
    hpf_image = cv2.subtract(gray_image, blurred_image)
    # Convert back to RGB
    hpf_image_rgb = cv2.cvtColor(hpf_image, cv2.COLOR_GRAY2RGB)
    # Update the current image
    current_image = ImageTk.PhotoImage(image=Image.fromarray(hpf_image_rgb))
    image_label.configure(image=current_image)

def apply_mean_filter():
    global original_image
    global current_image
    # Convert the image to numpy array
    img_array = np.array(original_image)
    # Apply mean filter
    mean_filtered_image = cv2.blur(img_array, (5, 5))
    # Convert back to PIL image
    mean_filtered_image_pil = Image.fromarray(mean_filtered_image)
    # Convert the image to format that tkinter can display
    current_image = ImageTk.PhotoImage(image=mean_filtered_image_pil)
    # Update the image display
    image_label.configure(image=current_image)

def apply_median_filter():
    global original_image
    global current_image
    # Convert the image to numpy array
    img_array = np.array(original_image)
    # Apply median filter
    median_filtered_image = cv2.medianBlur(img_array, 5)
    # Convert back to PIL image
    median_filtered_image_pil = Image.fromarray(median_filtered_image)
    # Convert the image to format that tkinter can display
    current_image = ImageTk.PhotoImage(image=median_filtered_image_pil)
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

def filters_window():
    global image_label
    global original_image
    global filters_win
    # Create the main window
    filters_win = tk.Tk()

    # Set the dimensions of the window
    window_width = 1024
    window_height = 768

    # Calculate the screen width and height
    screen_width = filters_win.winfo_screenwidth()
    screen_height = filters_win.winfo_screenheight()

    # Calculate the position of the window to center it on the screen
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the geometry of the window
    filters_win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set the title of the window
    filters_win.title("Image Processing Project")

    # Create a label for the filters
    filters_label = ttk.Label(filters_win, text="Filters", font=("Arial", 36), padding=30)
    filters_label.pack(side=tk.TOP, pady=10)

    # Create a frame for buttons
    button_frame = ttk.Frame(filters_win)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(110, 70), pady=80)


    # Create buttons
    button1 = ttk.Button(button_frame, text="HPF", style="Fancy.TButton", command=apply_hpf)
    button2 = ttk.Button(button_frame, text="Mean Filter", style="Fancy.TButton", command=apply_mean_filter)
    button3 = ttk.Button(button_frame, text="Median Filter", style="Fancy.TButton", command=apply_median_filter)
    button4 = ttk.Button(button_frame, text="Original Image", style="Fancy.TButton", command=get_original_image)
    button5 = ttk.Button(button_frame, text="Back To Main", style="Fancy.TButton", command= open_main_window)

    # Pack buttons
    button1.pack(fill=tk.X, pady=10)
    button2.pack(fill=tk.X, pady=10)
    button3.pack(fill=tk.X, pady=10)
    button4.pack(fill=tk.X, pady=10)
    button5.pack(fill=tk.X, pady=10)

    # Create a frame for the image
    image_frame = tk.Frame(filters_win, bd=2, relief="ridge")  # Add a dashed border with a little padding
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
    filters_win.mainloop()
