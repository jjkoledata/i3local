# Tool to easily change locale settings with i3
import subprocess as sp

def tz_now():
    """catches the current timezone"""
    status = sp.run(["timedatectl", "status"], capture_output=True,
                    encoding="utf-8")
    return status.stdout


def list_zones():
    """retrieves the list of timezones"""
    zones = sp.run(["timedatectl", "list-timezones"], capture_output=True,
                   encoding="utf-8")
    return zones


def change_tz():
    """changes the timezone"""
    new_tz = input("Enter the new timezone:\n> ")
    sp.run(["timedatectl", "set-timezone", new_zone], capture_output=True,
           encoding="utf-8")


# Script for parsing the data from commands
def dict_parser():
    """returns an organized dictionary from a list, organized by location"""
    tz_dict = {}
    tz_list = list_zones().stdout.split("\n")
    for i in tlist:
        parted = i.partition("/")
        if parted[0] in tz_dict:
            tz_dict[parted[0]].append(parted[-1])
        else:
            tz_dict[parted[0]] = [parted[-1]]
    return tz_dict

