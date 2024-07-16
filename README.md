# Voice-Controlled Application Launcher

This Python script allows you to open your macOS applications using voice commands. It listens for a specific activation phrase and then responds to your voice commands to open applications.

## Features

- Uses Google Web Speech API to recognize voice commands.
- Supports text-to-speech feedback using the `say` command on macOS.
- Can open any application with `.app` extension located in the `/Applications` directory .


## Requirements

- macOS
- Python 3.x
- `speech_recognition` library
- `pyaudio` library
- Internet connection (for Google's speech recognition service)

## Installation

1. **Install Python 3.x** if not already installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the repository** (or copy the script to your local machine).

3. **Navigate to the directory** where the script is located.

4. **Install required Python libraries** using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**: Navigate to to the directory where the script is located and run the following.
    ```bash
    python3 jarvis.py
    ```

2. **Speak the activation phrase** ("jarvis" by default).

3. **Issue a voice command** to open an application. For example, saying "open Safari" will open the Safari browser if it's installed in the `/Applications` directory.

4. **To exit the program**, say "goodbye".

## Script Breakdown

### Imports

- `speech_recognition` for recognizing speech.
- `os` for interacting with the operating system.
- `subprocess` for running system commands.
- `re` for handling regular expressions.

### Functions

- `say(text)`: Uses the `say` command to convert text to speech.
- `search_voice_commands(query)`: Searches for a matching voice command in the list of applications.
- `execute_command(query)`: Executes the system command corresponding to the voice command.
- `activate(phrase='jarvis')`: Listens for the activation phrase to start the voice command process.

### Main Loop

The script runs continuously, listening for the activation phrase. Once activated, it listens for a command and attempts to execute the corresponding system command to open an application.

## Customization

- **Change the activation phrase**: Modify the `phrase` parameter in the `activate` function.
- **Add more commands**: Extend the `voice_commands` dictionary or modify the script to dynamically add commands.

## Notes

- Ensure your microphone is properly configured and accessible.
- The `say` command is specific to macOS. If you're using a different operating system, you'll need to replace or modify this function.

## Contributing

Feel free to submit issues or pull requests to contribute to this project.
