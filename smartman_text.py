# -*- coding: utf-8 -*-
import os
from openai import OpenAI
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from termcolor import colored
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

import pyperclip

import readline
import threading
import time

conversation_log = [{"role": "system", "content": "You are ChatGPT, a helpful assistant."}]

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console(color_system="256", emoji=True)
app = QApplication([])
def spinner():
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(spinner_gen):
    while not spinner_done:
        print(f"\rThinking... {next(spinner_gen)}", end="", flush=True)
        time.sleep(0.1)
    print("\r" + " " * 15, end="\r")

def open_multiple_files():
    files, _ = QFileDialog.getOpenFileNames(None, "Select Files")
    return files

def query_chatgpt(prompt):
    global spinner_done
    spinner_done = False
    spinner_gen = spinner()
    spinner_thread = threading.Thread(target=show_spinner, args=(spinner_gen,))
    spinner_thread.start()
    conversation_log.append({"role": "user", "content": prompt})
    chat_completion = client.chat.completions.create(
            messages=conversation_log,
            model="gpt-4o",
    )
    spinner_done = True
    spinner_thread.join()
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    has_files = False
    while True:
        try:
            os.system("clear")
            print("╔══════════════════════════╗")
            print("║         SmartMan         ║")
            print("║       ChatGPT CLI        ║")
            print("║    By: TheStoneRabbit    ║")
            print("╚══════════════════════════╝\n")
            prompt = input("> ")
            if prompt == "/newcontext":
                conversation_log = [{"role": "system", "content": "You are ChatGPT, a helpful assistant."}]
                os.system("clear")
                print("New context created.")
                sleep(2)
                continue
            elif prompt == "/quit":
                break
            elif prompt == "/upload":
                has_files = True
                selected_files = open_multiple_files()
                console.clear()
                print("Files uploaded. Press the enter key to continue.")
                prompt = input("> ")
            else:
                if has_files:
                    start_text = "Below are the files you need to analyze."
                    for file in selected_files:
                        with open(file, "r") as f:
                            data = f.read()
                            name = file.split("/")[-1]
                            start_text += f"\n{name}: \n\n```\n{data}\n```\n\n"
                    response = query_chatgpt(f'{prompt}\n\n{start_text}')
                    has_files = False
                else:
                    response = query_chatgpt(prompt)
                markdown = response
                text_to_copy = ""
                count = 0

                for text_portion in range(1, len(markdown.split("```"))):
                    if(text_portion % 2 == 1):
                        count += 1
                        portion = markdown.split("```")[text_portion]
                        portion_pieces = portion.splitlines()
                        final_portion = "\n".join(portion_pieces[1:])
                        text_to_copy += final_portion + "\n\n\n"
                pyperclip.copy(text_to_copy)
                console.clear()
                with console.pager(styles=True):
                    syntax = Markdown(markdown, code_theme="monokai")
                    console.print(syntax)
        except KeyboardInterrupt:
            break
    print("\nGoodbye!")


