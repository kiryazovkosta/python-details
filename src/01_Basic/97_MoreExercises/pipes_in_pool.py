volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours = float(input())

pipe_one_volume = pipe_one_debit * hours
pipe_two_volume = pipe_two_debit * hours
filled_volume = pipe_one_volume + pipe_two_volume

if volume >= filled_volume:
    filled = filled_volume/volume * 100
    pipe_one_usage = pipe_one_volume/filled_volume * 100
    pipe_two_usage = pipe_two_volume/filled_volume * 100
    print(f"The pool is {filled}% full. Pipe 1: {pipe_one_usage}%. Pipe 2: {pipe_two_usage}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {filled_volume-volume:.2f} liters.")