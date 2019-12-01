#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program takes in input and outputs a canada post address


def canada_address(first_name, last_name, address, city,
                   province, postal_code, apartment=None):
    # This function turns inputs into a proper address format

    # Process
    if apartment is not None:
        post_address = first_name + " " + last_name + "\n" + apartment + \
            " " + address + "\n" + city + " " + province + "  " + postal_code
    else:
        post_address = first_name + " " + last_name + "\n" + address + "\n" + \
            city + " " + province + " " + postal_code

    return post_address


def main():
    # This function gets input

    # Variables
    apartment = None

    # Input
    first_name = input("Enter the recipient's first name: ")
    last_name = input("Enter the recipient's last name: ")
    address = input("Enter the destination address : ")
    apt_checker = input("Does the recipient live in an apartment (y/n): ")
    if apt_checker.upper() == "Y" or apt_checker.upper() == "YES":
        apartment = input("Enter the recipient's apartment number: ")
    city = input("Enter the recipient's city: ")
    province = input("Enter the recipient's province or territory: ")
    postal_code = input("Enter the recipient's postal code: ")

    # Process
    if apartment is not None:
        post_address = canada_address(first_name, last_name, address,
                                      city, province,
                                      postal_code, apartment)
    else:
        post_address = canada_address(first_name, last_name, address,
                                      city, province,
                                      postal_code)

    # Output
    print("")
    print(post_address)


if __name__ == "__main__":
    main()
