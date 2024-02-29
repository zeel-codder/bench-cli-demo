import logging
from rich.logging import RichHandler


def get_logger(force=False):
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=False, markup=False)],
    )

    custom_logger = logging.getLogger("erpnext_xero")
    return custom_logger
