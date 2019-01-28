print('Once upon a time...')


class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    # add new branches to the story
    def add_child(self, node):
        self.choices = self.choices + [node]

    # initiates story from root. Takes input to traverse story lines
    def traverse(self):
        # sets init value to story node
        story_node = self
        # prints variable story piece from self. Which is the starting/root story in this case
        print(story_node.story_piece)
        # iterates through list of choices until empty
        while len(story_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue the story: ")
            # checks if input is valid. If input is not valid it starts again at the top of the while loop
            if choice not in ['1', '2']:
                print('Enter a valid choice. 1 or 2.')
            # in this case the input is valid
            else:
                # index numbers are 0 and 1. Choices are 1 and 2. This corrects for that
                chosen_index = int(choice) - 1
                # this inputs index into new variable chosen child
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                # shifts tree one level/branch down. Which shortens the choices list
                story_node = chosen_child


story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
# start story
story_root.traverse()
