Updated README.md
# 🖼 Image Resizer Tool

## 📌 Overview
This is a **Python-based Image Resizer Tool** that can **resize** and **convert** multiple images in a batch.  
It uses the **Pillow (PIL)** library for image processing and the **os** module for file handling.  
The script also includes a feature to **auto-generate sample images** for quick testing.

---

## 🚀 Features
- ✅ Batch resize images from a folder
- ✅ Convert images to different formats (JPEG, PNG, WEBP)
- ✅ Set custom width, height, and image quality
- ✅ Automatically generate sample test images
- ✅ Error handling for unsupported files
- ✅ Easy to extend for GUI applications

---

## 📂 Project Structure


image_resizer_tool/
│
├── sample_images/ # Input images for testing
├── output_images/ # Resized & converted images
├── image_resizer.py # Main Python script
└── README.md # Project description


---

## 🛠 Installation
1. Clone this repository or download the code.
2. Install required dependencies:
   ```bash
   pip install pillow

▶ Usage

Open a terminal and navigate to the project folder.

Run the script:

python image_resizer.py


Follow the on-screen prompts:

Enter input folder (default: sample_images)

Enter output folder (default: output_images)

Enter resize width & height

Choose output format (JPEG/PNG/WebP)

Set image quality (1–100)

📷 Example Output
1️⃣ Running the Tool

Replace this with your actual terminal screenshot after running the script.


2️⃣ Before Resizing

Replace this with your sample_images folder screenshot showing original images.


3️⃣ After Resizing

Replace this with your output_images folder screenshot showing resized images.


📚 Interview Preparation (as per task)

What is PIL/Pillow? → Python Imaging Library for processing images.

How to open & save an image? → Image.open() & image.save()

What is resize() method? → Used to change image dimensions.

How to read all files in a directory? → os.listdir()

What is the os module? → Handles file & folder operations.

How to change file formats? → Save with desired extension & format.

What is a pixel? → Smallest unit of an image.

Why use try-except? → To handle errors without stopping execution.

How to make it dynamic? → Take user input for size, format, and folders.

Can this be extended to GUI? → Yes, using Tkinter or PyQt.

📄 License

This project is open-source and free to use for learning and development purposes.

✍ Author

Khalik Khan
B.Tech CSE (Data Science) Student | AI & Backend Development Enthusiast


