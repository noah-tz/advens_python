
import re
import time

# ANSI colors
colors = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[33m",  # Yellow
)

def count():
    print(f"{colors[1]}One")
    time.sleep(1)
    print(f"{colors[2]}Two")


def search_for_pattern():
    pattern = r'\d+'
    text = 'abc 123 def 456 ghi'
    match = re.search(pattern, text)
    print(f"{colors[3]}Match: {match[0]}")


def main():
    tasks = [count(), count(), count(), search_for_pattern()]
    for task in tasks:
        task


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{colors[4]}{__file__} executed in {elapsed:0.2f} seconds.")
