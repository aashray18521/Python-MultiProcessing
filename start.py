import multiprocessing
import time


start = time.perf_counter()


def do_something():
    print("Sleeping")
    time.sleep(1)
    print("Done")

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

end = time.perf_counter()

print(f"Time Taken: {round(end-start, 3)} second(s)")
