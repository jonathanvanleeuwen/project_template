import logging
import time
from datetime import timedelta
from pathlib import Path

import argh
from tqdm import tqdm

from src.about import version
from src.myprojectcode import run_code


class TqdmLoggingHandler(logging.Handler):
    """
    Setup logging handler class for the progressbar to work with logging module
    """

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def config_logger() -> None:
    """
    Define the settings for the logger
    """
    log_file = Path("template_log.log")
    log_file.unlink(missing_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(log_file), TqdmLoggingHandler()],
    )


@argh.arg("--y", help="Second optional value.")
@argh.arg("x", help="The first value. (Required)")
def entry(x: int, y: int = 10) -> None:
    """
    Information about the entry point
    """
    config_logger()
    start = time.time()
    sepperator = "_" * 120
    logging.info(sepperator)
    logging.info("Starting template run:")
    logging.info(sepperator)
    logging.info(f"  x value:    {x}")
    logging.info(f"  y value:    {y}")
    logging.info(sepperator)
    logging.info("Starting...")
    run_code(int(x), int(y))
    logging.info("Finished!")
    logging.debug(f"Duration: {str(timedelta(seconds=int(time.time()-start)))}")


if __name__ == "__main__":
    argh.dispatch_commands([entry, version])
