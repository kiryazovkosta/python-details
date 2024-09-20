HOURS_FOR_PROJECT_COMPLETE = 3

name = input()
projects_count = int(input())

total_hours = projects_count * HOURS_FOR_PROJECT_COMPLETE
print(f'The architect {name} will need {total_hours} hours to complete {projects_count} project/s.')