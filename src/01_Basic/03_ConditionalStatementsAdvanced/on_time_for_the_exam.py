exam_hour = int(input())
exam_minutes = int(input())
arrived_hour = int(input())
arrived_minutes = int(input())

exam_total_minutes = exam_hour * 60 + exam_minutes
arrived_total_minutes = arrived_hour * 60 + arrived_minutes
diff_in_minutes = exam_total_minutes - arrived_total_minutes

if 0 <= diff_in_minutes <= 30:
    print("On time")
    if diff_in_minutes != 0:
        print(f"{abs(diff_in_minutes)} minutes before the start")
elif diff_in_minutes < 0:
    print("Late")
    diff_in_minutes = abs(diff_in_minutes)
    if diff_in_minutes <= 59:
        print(f"{abs(diff_in_minutes)} minutes after the start")
    else:
        hours = diff_in_minutes // 60
        minutes = diff_in_minutes % 60
        print(f"{hours}:{minutes:02d} hours after the start")
else:
    print("Early")
    if diff_in_minutes <= 59:
        print(f"{abs(diff_in_minutes)} minutes before the start")
    else:
        hours = diff_in_minutes // 60
        minutes = diff_in_minutes % 60
        print(f"{hours}:{minutes:02d} hours before the start")