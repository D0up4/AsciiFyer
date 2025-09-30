from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

try:
    from pystyle import Center, Colors, Colorate
except ImportError:
    import os
    os.system('pip install pystyle')
    from pystyle import Center, Colors, Colorate

ASCII_ART = r"""
   _____                .__._____________                   
  /  _  \   ______ ____ |__|__\_   _____/__.__. ___________ 
 /  /_\  \ /  ___// ___\|  |  ||    __)<   |  |/ __ \_  __ \
/    |    \\___ \\  \___|  |  ||     \  \___  \  ___/|  | \/
/____|__  /____  >\___  >__|__|\___  /  / ____|\___  >__|   
        \/     \/     \/           \/   \/         \/       
"""

console = Console()

def print_gradient_ascii_art(ascii_art):
    centered_art = Center.XCenter(ascii_art)
    colored_art = Colorate.Horizontal(Colors.blue_to_purple, centered_art)
    print(colored_art)

def ascii_encode(text):
    return ' '.join(str(ord(c)) for c in text)

def ascii_decode(ascii_codes_str):
    try:
        return ''.join(chr(int(code)) for code in ascii_codes_str.strip().split())
    except ValueError:
        return None

def print_ascii_conversion(text):
    console.print("\n[bold green]Characters:[/bold green]")
    console.print(" ".join(f"[cyan]{c}[/cyan]" for c in text))
    console.print("[bold green]ASCII Codes:[/bold green]")
    console.print(" ".join(f"[magenta]{ord(c)}[/magenta]" for c in text))
    console.print()

def main():
    console.clear()
    print_gradient_ascii_art(ASCII_ART)

    while True:
        console.print("\n[bold blue][1][/bold blue] Asciify text")
        console.print("[bold blue][2][/bold blue] De-Asciify text")
        console.print("[bold blue][3][/bold blue] Exit\n")
        
        choice = Prompt.ask("Select an option (1-3)")
        
        if choice == "1":
            text = Prompt.ask("[bold green]Enter text to Asciify[/bold green]")
            encoded = ascii_encode(text)
            console.print(f"[green]Encoded ASCII:[/green] {encoded}")
            print_ascii_conversion(text)
            input("\nPress [Enter] to return to menu...")

        elif choice == "2":
            ascii_codes = Prompt.ask("[bold cyan]Enter ASCII codes to De-Asciify (space-separated)[/bold cyan]")
            decoded = ascii_decode(ascii_codes)
            if decoded is None:
                console.print("[bold red]Invalid ASCII code input! Please enter numbers separated by spaces.[/bold red]")
            else:
                console.print(f"[cyan]Decoded text:[/cyan] {decoded}")
            input("\nPress [Enter] to return to menu...")

        elif choice == "3":
            console.print("[bold red]Goodbye![/bold red]")
            break

        else:
            console.print("[bold red]Invalid selection. Please choose 1, 2, or 3.[/bold red]")

if __name__ == "__main__":
    main()
