import time

timestamp0 = time.time()
print("timestamp0:", timestamp0)
time.sleep(2)
timestamp1 = time.time()
print("timestamp1:", timestamp1)
timestamp_delta = timestamp1 - timestamp0
print("timestamp_delta:", timestamp_delta)
