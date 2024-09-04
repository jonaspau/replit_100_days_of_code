# Get input
days = int(input("How many days do you want to calcualte? "))

# Print calculations
print("--------------------------")
hours = days*24
print(f"{days} days is {hours} hours")

mins = hours*60
print(f"{hours} hours is {mins} minutes")

secs = mins*60
print(f"{mins} minutes is {secs} seconds")

print(f"So to sum up, {days} days is {secs} seconds")
print("===========================================")