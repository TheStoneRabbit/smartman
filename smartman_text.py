import os
from openai import OpenAI
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from pyfiglet import Figlet
from termcolor import colored
import pyperclip

import readline
import threading
import time

conversation_log = [{"role": "system", "content": "You are ChatGPT, a helpful assistant."}]

f = Figlet(font='rectangles')
f1 = Figlet(font='small')
f2 = Figlet(font='straight')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console(color_system="256", emoji=True)

def spinner():
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(spinner_gen):
    while not spinner_done:
        print(f"\rThinking... {next(spinner_gen)}", end="", flush=True)
        time.sleep(0.1)
    print("\r" + " " * 15, end="\r")



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

    while True:
        try:
            os.system("clear")
            first_title = f.renderText("SmartMan")
            second_title = f1.renderText("ChatGPT CLI")
            author = f2.renderText("By: TheStoneRabbit")
            colored_text1 = colored(first_title, color="white", on_color="on_dark_grey", attrs=['bold'])
            colored_text2 = colored(second_title, color="white", on_color="on_dark_grey", attrs=['bold'])
            colored_text3 = colored(author, color="white", on_color="on_dark_grey", attrs=['bold'])
            print(colored_text1)
            print(colored_text2)
            print(colored_text3)
            prompt = input("> ")
            if prompt == "/newcontext":
                conversation_log = [{"role": "system", "content": "You are ChatGPT, a helpful assistant."}]
                os.system("clear")
                print("New context created.")
                sleep(2)
                continue
            elif prompt == "/quit":
                break
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
    print("\n\nGoodbye!")


