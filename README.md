# SmartMan - ChatGPT CLI

## Overview

**SmartMan** is a Command-Line Interface (CLI) application that allows you to interact with OpenAI's GPT-4 model directly from your terminal. This tool is designed to provide a rich text interface using the `rich` library, which enhances the terminal experience with colorful, styled text, Markdown rendering, and more.

## Features

- **Interactive CLI**: Chat with GPT-4 directly in your terminal.
- **Rich Text Display**: Responses are rendered in beautiful Markdown with syntax highlighting.
- **Context Management**: Start a new conversation context anytime with the `/newcontext` command.
- **Figlet Titles**: Displays a stylish title and author name using Figlet ASCII art.
- **Graceful Exit**: Exit the application cleanly with `/quit` or a keyboard interrupt (Ctrl+C).

## Dependencies

The application requires the following Python packages:

- `openai`: Interact with OpenAI's API.
- `rich`: For rendering rich text, syntax highlighting, and Markdown in the terminal.
- `pyfiglet`: For creating ASCII art banners.
- `termcolor`: For colored terminal text.
- `readline`: For enhanced command-line editing and history.

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Environment Variables

- **OPENAI_API_KEY**: Set this environment variable with your OpenAI API key to authenticate requests.

## Usage

1. **Run the Script**:
   Start the CLI application by running the script.

   ```bash
   python smartman.py
   ```

2. **Interact with GPT-4**:
   Type your queries after the `>` prompt and press Enter. The model will respond with formatted text displayed in your terminal.

3. **Special Commands**:
   - `/newcontext`: Clears the current conversation and starts a new one.
   - `/quit`: Exits the application.

4. **Graceful Exit**:
   - Press `Ctrl+C` at any time to exit the application.

## Example

```bash
> What is the capital of France?
```

This will display the response in a styled format with Markdown rendering.

## Customization

- **Titles and Author**:
   The script uses Figlet fonts (`rectangles`, `small`, `straight`) to display the title and author information. You can customize the fonts or text by modifying the Figlet instances.

- **Color Scheme**:
   The terminal text colors are defined using `termcolor`. Adjust the `colored_text1`, `colored_text2`, and `colored_text3` variables to change the color scheme.

## License

This project is licensed under the MIT License.

---

Enjoy using SmartMan, your CLI companion for interacting with GPT-4! 🚀

---

