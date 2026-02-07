class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("❌ No team lead exists yet.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side.lower() == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                    return True
                else:
                    print("❌ Left side already occupied.")
                    return False

            elif side.lower() == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                    return True
                else:
                    print("❌ Right side already occupied.")
                    return False
            else:
                print("❌ Side must be 'left' or 'right'.")
                return False

        found = False

        if current_node.left:
            found = self.insert(manager_name, employee_name, side, current_node.left)

        if not found and current_node.right:
            found = self.insert(manager_name, employee_name, side, current_node.right)

        if current_node == self.root and not found:
            print("❌ Manager not found.")

        return found

    def print_tree(self, node=None, level=0):
        if self.root is None:
            print("❌ No team to display.")
            return

        if node is None:
            node = self.root

        print("  " * level + "- " + node.name)

        if node.left:
            self.print_tree(node.left, level + 1)

        if node.right:
            self.print_tree(node.right, level + 1)


def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root is not None:
                print("❌ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    company_directory()


"""
DESIGN MEMO

In this assignment, I created a company directory using a custom binary tree
instead of built-in data structures. Recursive insertion worked by starting
at the root of the tree and checking whether the current node matched the
manager’s name. If it did not match, the function called itself on the left
and right children, allowing the program to search through the entire tree
until the correct manager was found.

One challenge I faced was determining when to stop the recursive search.
Without proper base cases, the function could continue searching even after
the employee was inserted or attempt to access a node that did not exist.
Carefully checking for None values and returning early helped prevent errors
and unnecessary recursion. Another challenge was handling cases where a
manager name did not exist or when a requested side was already occupied.

Trees are preferable to other data structures when representing hierarchical
relationships such as company reporting structures or file systems. Unlike
lists or dictionaries, trees naturally model parent-child relationships and
allow data to be stored and accessed in an organized way. This makes trees
useful in real-world systems where structure, scalability, and clarity are
important.
"""
