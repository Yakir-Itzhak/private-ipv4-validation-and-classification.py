# Private IPv4 Validation & Class Classification Tool

This script asks the user for a private IPv4 address (like 10.x.x.x or 192.168.x.x) and checks if it's valid.  
If the address is valid and private, it will tell you whether it's Class A, B, or C.

### What it does
- Asks you for an IPv4 address (up to 3 attempts or until quit).
- Validates if it's a correct IPv4 address.
- Checks if it's a private range.
- Determines the class based on the first octet.

### Why I made it
I wanted to practice:
- input validation,
- using Python's `ipaddress` module,
- IPv4 private ranges,
- and basic address classification.

### How to run
