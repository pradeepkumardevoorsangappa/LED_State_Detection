# Instructions for running Green_LED.py:
1. If Python is not already installed, install it first.
2. Open the command prompt and install the following Python libraries using pip:

    • pip install matplotlib
    • pip install matplotlib-inline
    • pip install numpy
    • pip install opencv-python
    • pip install opencv-contrib-python
    • pip install opencv-python-headless

3. Open the program "Green_LED.py" in your preferred integrated development environment (IDE), such as JupyterLab, PyCharm, or VS Code.
4. If you are using an external camera connected to your laptop, change the video source from '0' to '1'.
    • Or simply, then disable the laptop camera from the  Device manager.
5. If you are using a camera other than the Intel RealSense camera used in this program, install the respective library for your camera using the pip command in the command prompt.
6. Ensure that the robot or camera is in the capturing position before executing the program.
    • To execute the program from the command prompt, navigate to the location where the program is saved and type "python Green_LED.py".

# Instructions for running Red_LED_Detection-with-Location.ipynb:
1. Create the dictionary as per your setup (Assuming the component will be at a fixed location always)
2. Edit the file path where the images are stored
3. Run the program; it will ask for the name of the image (add it with an extension)

# depth_cut.py (Specifically for intel real sense depth cameras)
This is mainly to focus on the ROI, where only the ROI is concentrated and the rest turns into Black Pixel. 
