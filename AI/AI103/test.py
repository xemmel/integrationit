import re


def main():
    print("Hello")
    user_input = input("Input: ")
    tools_pattern = "(?<=\\().*?(?=\\)$)"
    match = re.search(tools_pattern,user_input)
    if match:
        print(f"yes! {match.group()}")

if __name__ == "__main__":
    main()
