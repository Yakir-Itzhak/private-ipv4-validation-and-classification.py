# private_ipv4_validation_and_classification.py

import ipaddress

def get_private_ipv4(max_attempts = 3):
    attempt = 1

    while attempt <= max_attempts:
        ip_str = input("Enter a private IPv4 address (or 'q' to quit):\n").strip()

        # allow user to exit
        if ip_str.lower() in ["q", "quit", "exit"]:
            return None

        try:
            ip = ipaddress.IPv4Address(ip_str)
        except ipaddress.AddressValueError:
            print("That is not a valid IPv4 address.\n")
            attempt += 1
            continue

        # make sure it's private
        if not ip.is_private:
            print("This address is valid, but it is not a private IPv4.\n")
            attempt += 1
            continue

        # if we get here, ip is both valid and private
        return ip

    print("Too many invalid attempts.")
    return None


def get_class(ip):
    # get the first octet to decide the class
    first_octet = int(str(ip).split(".")[0])

    if 1 <= first_octet <= 126:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    else:
        return "Unknown"


def main():
    ip = get_private_ipv4()
    if ip is None:
        return

    ip_class = get_class(ip)

    if ip_class == "Unknown":
        print(f"{ip} is a private IPv4 address but not in the usual A/B/C ranges.")
    else:
        print(f"{ip} is a valid class {ip_class} private IPv4 address!")


if __name__ == "__main__":
    main()
