# Hanoi game: 3 rods, 7 disks. The n-tower is on the start rod

# Move the n-tower from the starting rod to the end rod using an auxilary rod if needed 
def move_disk(n, start, end, aux):
    # Base case: 1-tower
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
    else:   # Recursion step
        # Move the (n-1)-disk from start to aux
        move_disk(n-1, start, aux, end) # Now the end rod is used as an aux rod
        print(f"Move disk {n} from {start} to {end}")
        # Move the (n-1)-disk from aux to end
        move_disk(n-1, aux, end, start)

### TESTING ###
n = 1
print(f"Instruction to move the {n}-disk tower")
move_disk(n, "Left", "Right", "Center")
print("-------------------")

n = 4
print(f"Instruction to move the {n}-disk tower")
move_disk(n, "Left", "Right", "Center")
print("-------------------")



