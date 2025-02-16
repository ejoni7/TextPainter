# **Tkinter User Registration and GUI Customization App**  

This project is a **Tkinter-based** Python application that provides user registration, login, and a multi-window interface with extensive customization options.  

## **Features**  

### **1. User Registration and Login**  
- Users can register by entering their details.  
- The data is stored in a file for future logins.  
- Upon successful login, the user is redirected to the main interface.  

### **2. Multi-Window Interface**  
After login, three separate windows open with different functionalities:  

#### **Window 1: Label Customization**  
- A label is displayed that can be moved in any direction using buttons.  
- Resize the label dynamically.  
- Change the label’s text color and background color.  
- Change the window background color.  
- Display the **HEX code** of the selected colors in real time.  

#### **Window 2: Label Management**  
- Create new labels dynamically.  
- Update or delete existing labels.  
- Change the text of any label.  
- Switch between multiple labels easily.  
- The position, size, and color of all labels are saved and restored upon the next login.  

#### **Window 3: Favorite Colors**  
- Users can save their favorite colors.  
- Saved colors can be used as:  
  - Window background.  
  - Label background.  
  - Label text color.  
- Users can manually enter a HEX color code and preview the color instantly.  
- Previously saved colors are available for future use.  

### **3. Screenshot Functionality**  
- A button to take screenshots in **JPG format**.  
- A button to take screenshots in **PDF format**.  
- If the required directories or files don’t exist, they are automatically created.  
- Screenshots are saved separately for each user.  

## **Requirements**  
- **Python 3.12**  
- **Tkinter** (built-in)  
- **Pillow** (for screenshots)  

## **Usage**  
1. Run the app and register a new user.  
2. Log in to access the customizable interface.  
3. Use the different windows to manage labels, change colors, and save preferences.  
4. Take screenshots as needed.
