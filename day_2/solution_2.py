with open("day_2/input.txt") as file:
    reports = [[int(n) for n in line.split()] for line in file]

def level_diff_not_safe(diff, level_increasing):
    return (diff == 0) or (abs(diff) < 1 or abs(diff) > 3) or ((diff > 0) ^ level_increasing)

def validate_report(report):
    level_increasing = report[1] > report[0]
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if level_diff_not_safe(diff, level_increasing):
            return False
    return True

counter = 0
for report in reports:
    if validate_report(report):
        counter += 1
    else:
        for i in range(len(report)):
            short_report = report[:i] + report[i+1:]
            if validate_report(short_report):
                counter += 1
                break

print(counter)