from math import floor
serial = input()
seasons = int(input())
episodes = int(input())
episode_duration = float(input())
extra_time = seasons * 10
episode_duration += episode_duration * 0.2
total_time = seasons*episodes*episode_duration + extra_time
print(f"Total time needed to watch the {serial} series is {floor(total_time)} minutes.")