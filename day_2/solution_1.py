with open("day_2/input.txt") as file:
    reports = [[int(n) for n in line.split()] for line in file]

counter = 0
for report in reports:
    valid_report = True
    level_increasing = report[1] > report[0]
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if (diff == 0) or ((diff > 0) ^ level_increasing) or (abs(diff) < 1 or abs(diff) > 3):
            valid_report = False
            break
    counter += valid_report      
print(counter)