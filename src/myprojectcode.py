import logging
import multiprocessing as mp
import time
import sys

import psutil
from tqdm import tqdm

from src.utils import init_worker


def handle_mp_results(processes: list) -> None:
    """
    This handles the results from the multiproccessing call
    This is usefull because it also removes the finished processes and cleans up the
    process poll when process is done.
    By calling this function in a try except block, it allows for keyboard interupts to
    properly stop all the processing.

    :param processes: A list of all te started processes
    ]"""
    finished = False
    while not finished:
        for proc_idx, process in enumerate(processes):
            if process:
                if process.ready():
                    results = process.get()
                    processes[proc_idx] = None
                    logging.info(f"Result: {results}")
                    logging.info(f"Process: {proc_idx:04}")
        if not [proc for proc in processes if proc]:
            finished = True
        else:
            time.sleep(0.5)


def is_even(n: int) -> bool:
    """
    Checks if the number 'n' is even or odd

    :param n: The number to check
    :return: Whether (True) or not (False) the number is even
    """
    time.sleep(0.1)
    if n % 2 == 0:
        logging.info(f"{n} - is even")
        return True
    else:
        logging.info(f"{n} - is odd")
        return False


def run_code(x: int, y: int) -> None:
    """
    Main executing code for the project.
    The code runs through all the numbers between 0 and (x*y) and
    checks if the number is even or odd

    :param x: The first number to multiply with
    :param y: The second number to multiply with
    """
    # Single core processing
    pbar = tqdm(desc="Running code", total=x * y)
    for value in range(x * y):
        even = is_even(value)
        pbar.update()

    # Multicore processing
    pbar = tqdm(desc="Running code in parallel", total=x * y)
    n_cores = psutil.cpu_count() - 1
    logging.info(f"Parallel processing using {n_cores} cores...")
    pool = mp.Pool(n_cores, init_worker)
    processes = [pool.apply_async(is_even, kwds={"n": i}, callback=lambda _: pbar.update(1)) for i in range(x * y)]
    try:
        handle_mp_results(processes)
    except KeyboardInterrupt:
        logging.info("Caught KeyboardInterrupt, terminating workers...")
        for idx, _ in enumerate(processes):
            processes[idx] = None
        processes = None
        pool.terminate()
        pool.join()
        pool = None
        logging.info("Caught KeyboardInterrupt, Exiting...")
        sys.exit()
    else:
        pool.close()
        pool.join()
        pool = None
