class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.refs = 0

    def __repr__(self):
        return 'TrieNode(children: {}, endOfWord: {})'.format(self.children, self.endOfWord)


def drawTrie(root):
    def height(node):
        if not node:
            return -1
        if not node.children:
            return 0
        return 1 + max(height(child) for child in node.children.values())

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx, parent_x=None, parent_y=None, char=''):
        if node:
            # Draw line from parent to current node
            if parent_x is not None and parent_y is not None:
                jumpto(parent_x, parent_y)
                t.goto(x, y)

            # Move to node position
            jumpto(x, y)

            # Draw the character and end-of-word marker
            display_text = char if char else 'ROOT'
            if hasattr(node, 'endOfWord') and node.endOfWord:
                # Parentheses indicate end of word
                display_text = f"({display_text})"

            # Draw a circle around the node
            t.penup()
            t.goto(x, y-15)
            t.pendown()
            t.circle(15)

            # Write the character
            jumpto(x, y-5)
            t.write(display_text, align='center', font=('Arial', 10, 'bold'))

            # Draw children
            if hasattr(node, 'children') and node.children:
                # Get (char, node) pairs
                children_items = list(node.children.items())
                num_children = len(children_items)

                if num_children == 1:
                    # Single child goes straight down
                    child_x = x
                else:
                    # Multiple children spread out
                    start_x = x - (dx * (num_children - 1)) / 2

                for i, (child_char, child_node) in enumerate(children_items):
                    if num_children == 1:
                        child_x = x
                    else:
                        child_x = start_x + i * dx

                    draw(child_node, child_x, y - 80,
                         dx * 0.7, x, y - 15, child_char)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)

    # Set up the canvas
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)

    h = height(root)
    initial_y = 30 * h + 100
    initial_dx = 60 * (h + 1)  # Adjust spacing based on height

    jumpto(0, initial_y)
    draw(root, 0, initial_y, initial_dx)

    t.hideturtle()
    turtle.mainloop()
