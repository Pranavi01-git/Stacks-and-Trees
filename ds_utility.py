# ds_utility.py
# A simple CLI tool to practice Stacks and Trees.

class UndoRedoManager:
    # Uses a dual-stack to handle undo and redo history
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def add_action(self, text):
        self.undo_stack.append(text)
        self.redo_stack.clear() # clear redo history when new action happens
        print(f"Added: '{text}'")

    def undo(self):
        if len(self.undo_stack) == 0:
            print("Nothing to undo.")
            return
        
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print(f"Undo: removed '{action}'")

    def redo(self):
        if len(self.redo_stack) == 0:
            print("Nothing to redo.")
            return
        
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print(f"Redo: restored '{action}'")

    def show_history(self):
        print(f"Undo stack: {self.undo_stack}")
        print(f"Redo stack: {self.redo_stack}")


class FileNode:
    # A simple tree structure to represent folders and files
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, node):
        if self.is_file:
            print(f"Error: Cannot put an item inside a file ({self.name}).")
            return
        self.children.append(node)

    def print_tree(self, level=0):
        indent = "  " * level
        symbol = "-" if self.is_file else ">"
        print(f"{indent}{symbol} {self.name}")
        
        for child in self.children:
            child.print_tree(level + 1)

    def search_dfs(self, target_name, current_path=""):
        # Uses Depth-First Search to find a file
        path = f"{current_path}/{self.name}"
        
        if self.name.lower() == target_name.lower():
            print(f"Found it at: {path}")
            return True

        found = False
        for child in self.children:
            if child.search_dfs(target_name, path):
                found = True
        return found


def main():
    editor = UndoRedoManager()
    
    # Set up a dummy folder structure based on my portfolio
    root = FileNode("my_portfolio", is_file=False)
    
    src = FileNode("src", is_file=False)
    src.add_child(FileNode("index.html", is_file=True))
    src.add_child(FileNode("style.css", is_file=True))
    src.add_child(FileNode("script.js", is_file=True))
    
    assets = FileNode("assets", is_file=False)
    assets.add_child(FileNode("resume.pdf", is_file=True))
    
    root.add_child(src)
    root.add_child(assets)

    while True:
        print("\n--- DS Utility Menu ---")
        print("1. Type new text (Stack)")
        print("2. Undo (Stack)")
        print("3. Redo (Stack)")
        print("4. Show stack history")
        print("5. View folder tree (Tree)")
        print("6. Search for a file (DFS)")
        print("7. Quit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter some text: ")
            editor.add_action(text)
        elif choice == "2":
            editor.undo()
        elif choice == "3":
            editor.redo()
        elif choice == "4":
            editor.show_history()
        elif choice == "5":
            print("\nFolder Structure:")
            root.print_tree()
        elif choice == "6":
            target = input("Enter file name to search: ")
            print("Searching...")
            if not root.search_dfs(target):
                print("File not found.")
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
