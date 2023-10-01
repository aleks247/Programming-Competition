participants = int(input("Enter participants count: "))
max_points = 0
winner = ""

for i in range(participants):
    name = input("Enter participant name: ")
    points = 0
    command = input("Enter points(To finish type `Stop`):")
    
    while command.lower() != "stop":
        current_points = int(command)
        points += current_points
        command = input("Enter points(To finish type `Stop`):")
    
    print(f"{name} has {points} points.")
    
    if points > max_points:
        max_points = points
        winner = name
        print(f"{name} is the new number 1!")

print(f"{winner} won competition with {max_points} points!")
