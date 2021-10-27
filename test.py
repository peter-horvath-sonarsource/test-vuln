from mymodule import my_func

__all__ = ["unknown_func"]  # Noncompliant. "unknown_func" is undefined


import requests

requests.request('GET', 'https://example.domain', verify=False) # Noncompliant
requests.get('https://example.domain', verify=False) # Noncompliant

