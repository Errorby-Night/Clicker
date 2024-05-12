# Click For Sound

## Installation

1. First, ensure you have Python installed on your system.

2. If not, download and install Python from the official website.

3. Once Python is installed, follow these steps:

    - Open a terminal or command prompt.
    
    - Navigate to the directory where you've cloned or downloaded the MouseClickSound project.
    
    - Install the required dependencies by running the following command:
        ```bash
        cd MouseClickSound
        pip install -r requirements.txt
        ```

4. After installing the dependencies, you have two options to make the program start at startup:

    a. **Add to Startup (Windows)**:
        - Press `Win + R` to open the Run dialog.
        - Type `shell:startup` and press Enter. This will open the Startup folder.
        - Copy the `.bat` file from the MouseClickSound directory to this Startup folder.
        
    b. **Manually Start (Any OS)**:
        - Every time you start the computer, open a terminal or command prompt.
        - Navigate to the MouseClickSound directory.
        - Run the following command:
    ```bash 
    python main.py
    ```