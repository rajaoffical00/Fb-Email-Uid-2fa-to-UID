INPUT_FILE_PATH = "input.txt"
OUTPUT_FILE_PATH = "output.txt"

class Node:
    def __init__(self):
        self.emails = self.read_input()
        for mail in self.emails:
            if not mail:
                continue
            val = mail.split("|")
            if val and len(val) == 3:
                self.write_output(val[1])
            else:
                print(f"Invalid input format: {mail}")
        print("Done")
        input("Press Enter to exit...")
    def write_output(self, output):
        try:
            with open(OUTPUT_FILE_PATH, "a", encoding="utf-8") as file:
                file.write(output + "\n")
        except Exception as e:
            print(f"An error occurred while writing to the output file: {e}")
    
    def read_input(self):
        try:
            with open(INPUT_FILE_PATH, "r", encoding="utf-8") as file:
                data =  file.read().split("\n")
                return data
        except Exception as e:
            print(f"An error occurred while reading the input file: {e}")
            return []


if __name__ == "__main__":
    Node()