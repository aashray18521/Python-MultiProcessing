import multiprocessing
import time


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for : {seconds} second(s)")
    time.sleep(seconds)
    print("Done")

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

end = time.perf_counter()

print(f"Time Taken: {round(end-start, 3)} second(s)")
