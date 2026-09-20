import os
import re 




def main():
    print("Starting...")
    user_input = input("Input: ")
    pattern = "(?<=\\().*?(?=\\))"
    match = re.search(pattern,user_input)
    if match:
        print("match!!")
        tools_string = match.group()
        tools_array = tools_string.split(",")
        for item in tools_array:
            print(item.strip())

        user_input = user_input.replace(f"({match.group()})","")
    print(f"user input: {user_input}")
if __name__ == "__main__":
    main()