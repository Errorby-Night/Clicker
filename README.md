# ![Logo](ebdg2re4cgjlw3dr95w.svg) Clicker

## Description

This Python script plays click and release sounds upon specific button presses. It requires click sounds in `.wav` format placed in the `sounds` folder and release sounds in `release_sounds` folder. The script can be configured to run on system startup and exited using a designated hotkey.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Errorby-Night/Clicker
    ```

2. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Place click and release sounds in the respective folders.

4. Modify the `.bat` file according to file locations.

5. Press `Win+R`, type `shell:startup`, and paste the `.bat` file in the startup folder.

6. The script will now run on PC startup. To initiate click sounds, press the default hotkey `Ctrl+Shift+Y`, and use `` to quit.

## FAQ

**Q: Can I use other sound formats besides `.wav`?**

A: Currently, the script only supports `.wav` format for click and release sounds.

**Q: How can I change the hotkey for starting and quitting the script?**

A: You can modify the script to use a different hotkey by editing the source code where the hotkey is defined.

**Q: Is it possible to change the volume of the click sounds?**

A: Yes, you can adjust the volume by modifying the sound files themselves or by using audio editing software.

**Q: Can this script be run on operating systems other than Windows?**

A: This script is specifically designed for Windows operating systems and may not work on others without modification.
