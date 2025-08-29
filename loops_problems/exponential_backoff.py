import time 

wait_time = 1 
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print("Attempts", attempts +1 , "-wait time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1