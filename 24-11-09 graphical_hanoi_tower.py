# Step-by-step solution of the Hanoi Tower: a graphical visualisation

def create_towers(n, hanoi):
    global fixed_height
    for i in range(n):
        hanoi[0].append(i+1)
    fixed_height = n

def move_disks(n, start, end, aux):
    if n:
        move_disks(n - 1, start, aux, end)  # Move n-1 disks to auxiliary rod
        t = start.pop(0)  # Pop the top disk from the start rod
        end.insert(0, t)  # Place it on top of the end rod
        print_towers(hanoi)  # Print the rods after the move
        move_disks(n - 1, aux, end, start)  # Move n-1 disks from auxiliary to end rod

def print_towers(hanoi):
    # Define a fixed height for the towers
    global fixed_height
    print("\n   |      |      |")
    for level in range(fixed_height):
        for rod in hanoi:
            # Calculate the index from the bottom
            if level < fixed_height - len(rod):
                print("   |   ", end = "")  # Print empty level
            else:
                # Print disk or another | if no disk is at that level
                print(f"   {rod[level - (fixed_height - len(rod))]}   ", end = "")
        print("", end = "\n")
    print("   |      |      |")
    print("  ■■■    ■■■    ■■■")

### MAIN ###
n = 4  # Number of disks
hanoi = [[], [], []]
create_towers(n, hanoi) # Create the three towers
print_towers(hanoi)  # Print the initial configuration
move_disks(n, hanoi[0], hanoi[1], hanoi[2])  # Solve the Tower of Hanoi
