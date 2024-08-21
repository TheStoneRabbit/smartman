import os
from openai import OpenAI
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from pyfiglet import Figlet
from termcolor import colored
import readline



f = Figlet(font='rectangles')
f1 = Figlet(font='small')
f2 = Figlet(font='straight')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def query_chatgpt(prompt):
    chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt,
                }
                ],
            model="gpt-4o",
            )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    console = Console(color_system="256", emoji=True)
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
            response = query_chatgpt(prompt)
            markdown = response
            console.clear()
            with console.pager(styles=True):
                syntax = Markdown(markdown, code_theme="monokai")
                console.print(syntax)
        except KeyboardInterrupt:
            break
    print("\n\nGoodbye!")
