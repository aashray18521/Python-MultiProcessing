import concurrent.futures
import time
import torch


def do_something(seconds):
    print(f"Sleeping for : {seconds} second(s)")
    time.sleep(seconds)
    # if seconds == 4:
    #     raise ValueError("My Random Exception")
    return f"Done : {seconds}"


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()


def run():
    start = time.perf_counter()
    torch.multiprocessing.freeze_support()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 10)
        # f2 = executor.submit(do_something, 10)
        # print(f1.running())
        # print(f1.result())
        # print(f2.result())
        # print(f1.running())

        # results = [executor.submit(do_something, _) for _ in range(5)]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for r in results:
            try:
                print(r)
            except (Exception, ValueError):
                # print("Some exception was raised")
                continue

    end = time.perf_counter()

    print(f"Time Taken: {round(end-start, 3)} second(s)")


if __name__ == "__main__":
    run()
