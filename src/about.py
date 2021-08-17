__title__ = "Template for code project"
__summary__ = "Basic setup for a project"

__version__ = "0.0.1"

__author__ = "Jonathan van Leeuwen"
__email__ = "jonathan.vanleeuwen@viqtordavis.com"

__release_notes__ = f"\n{'-'*120}\n".join(
    [
        "0.0.1 - Release notes\nInitial setup",
    ]
)


def version() -> None:
    """
    Print version information
    """
    sepperator = "*" * 120
    joiner = f"\n{'-'*120}\n"
    release_notes = joiner.join(__release_notes__.split(joiner)[::-1])
    print(sepperator)
    print(f"Release notes:\n{release_notes}")
    print(sepperator)
    print(f"Title:\n\t{__title__}")
    print(sepperator)
    print(f"Summary:\n\t{__summary__}")
    print(sepperator)
    print(f"Version:\n\t{__version__}")
    print(sepperator)
    print(f"Author:\n\t{__author__}")
    print(sepperator)
    print(f"Email:\n\t{__email__}")
    print(sepperator)


"""
https://packaging.python.org/guides/single-sourcing-package-version/
# In setup.py (if its a package) read and exec the value into a variable
version = {}
with open("...sample/version.py") as fp:
    exec(fp.read(), version)
# later on we use: version['__version__']
"""
