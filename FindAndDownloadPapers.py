try:
    import sys
    from os import path
    import requests
    from colorama import Fore
    import re
    from datetime import date
except ImportError as IE:
    print(
        u"\u001b[31m"+f"{IE}, install it by typing `{sys.executable} -m pip install {IE.name}`"+u"\u001b[0m")
    exit()

download = False
verbose = False
last_year = 0
filesToDownload = []
urlSaveFile = "ValidUrls.txt"
ses = requests.Session()
subjectCodes = []
WARNING = Fore.YELLOW
VERBOSE = Fore.CYAN
TITLE = Fore.MAGENTA
POSITIVE = Fore.GREEN
POSITIVE_HL = Fore.LIGHTGREEN_EX
ERROR = f"{Fore.RED}[X]"
ERROR_HL = Fore.LIGHTRED_EX
RESET = Fore.RESET


def validate_year(year):
    if re.search("\D", year):
        return False
    elif int(year) > date.today().year or int(year) < 2010:
        return False
    return True


def checkParams():
    global download
    global verbose
    global last_year
    args = sys.argv
    help = f"""\r{VERBOSE}Download BE papers from https://www.gtu.ac.in/uploads/[term]/BE/[SubCode].pdf
                    \rOptions:
                    \r{POSITIVE_HL}-d{VERBOSE}\t\tDownload and save file(s) after fetching
                    \r{POSITIVE_HL}-v{VERBOSE}\t\tShow verbose output
                    \r{POSITIVE_HL}-l N{VERBOSE}\t\tLast year to check untill(Default is 4 years from current year)
                    (e.g: '-l 2019' would check from current year to 2019)
                    \r{POSITIVE_HL}-h|--help{VERBOSE}\tShow this help message
                    \rExample: '{POSITIVE}{args[0]} {POSITIVE_HL}-dvl 2019' would download all the papers from current year to 2019.{RESET}
                    """
    skip_iter = False
    if args.__len__() >= 2:
        for no, arg in enumerate(args):
            arg = arg.lower()
            if not no < 1:
                if not last_year == 0 and skip_iter:
                    skip_iter = False
                    continue
                if arg == '-l' or arg == '-dvl' or arg == '-vdl' or arg == '-vl' or arg == '-dl':
                    if arg.__contains__('v'):
                        verbose = True
                    if arg.__contains__('d'):
                        download = True
                    last_year = args[no + 1]
                    if not validate_year(last_year):
                        print(
                            f"{ERROR}Invalid year: {ERROR_HL}{last_year}{RESET}")
                        exit(128)
                    else:
                        skip_iter = True
                elif arg == '-d':
                    download = True
                elif arg == '-v':
                    verbose = True
                elif arg == '-dv' or arg == '-vd':
                    download = True
                    verbose = True
                elif arg == '-h' or arg == '--help':
                    print(help)
                    exit()
                else:
                    print(
                        f"{ERROR}Invalid argument: {ERROR_HL}{arg}{RESET}")
                    exit(128)


def getSubjects() -> list[str]:
    global verbose
    subjectString = input(
        "Enter subject codes separeted with commas: ").strip()
    if subjectString == "":
        print(f"{ERROR}No subject codes entered!{RESET}")
        exit()
    else:
        subcodes = []
        splittedCodes = subjectString.split(',')
        for code in splittedCodes:
            code = code.strip()
            if not len(code) == 7 or re.search("\D", code):
                print(f"{ERROR}Invalid code: {ERROR_HL}{code}{RESET}")
            else:
                subcodes.append(code)
    if len(subcodes) < 1:
        print(f"{ERROR}No valid Subject Codes where found!{RESET}")
        exit(1)
    if verbose:
        print(f"{VERBOSE}Following valid Subject Codes found:{RESET}")
        for no, code in enumerate(subcodes):
            if no == 0:
                print(f"{VERBOSE}{code}{RESET}", end="")
            else:
                print(f"{VERBOSE}, {code}{RESET}", end="")
        print()
    return subcodes


def main():
    global subjectCodes
    global download
    global verbose
    global last_year
    subjectCodes = getSubjects()
    exams = []
    if last_year == 0:
        last_year = date.today().year - 4
    else:
        last_year = int(last_year)
    for year in range(date.today().year, last_year-1, -1):
        exams.append(f"S{year}")
        exams.append(f"W{year}")

    with open(urlSaveFile, "w"):#creating file if it does not exist
        pass

    print(f"{TITLE}-------------Fetching URLs-----------{RESET}")
    for exam in exams:
        for subject in subjectCodes:
            url = f"https://www.gtu.ac.in/uploads/{exam}/BE/{subject}.pdf"
            r = ses.head(url=url)
            if r.status_code == 200:
                if not download:
                    with open(urlSaveFile, "a") as validUrls:
                        validUrls.write(f"{url}\n")
                    print(f"{POSITIVE}Got 200 for {url} {RESET}")
                else:
                    print(f"{POSITIVE}{url} will be downloaded!{RESET}")

                    tempDict = {"url": url, "exam": exam}
                    filesToDownload.append(tempDict)
            else:
                if verbose:
                    print(f"{VERBOSE}Got {r.status_code} for {url}{RESET}")
    if download:
        print(f"{TITLE}-------------Downloading-------------{RESET}")
        DownloadFiles()
    print(f"{WARNING}NOTE: File Urls are saved in {urlSaveFile}{RESET}")


def DownloadFiles():
    global filesToDownload
    for file in filesToDownload:
        url = file.get("url")
        exam = file.get("exam")
        filename = f"{exam}_{path.basename(url)}"
        print(
            f"{POSITIVE}[*]Downloding {url}, and will be saved as {filename}{RESET}")
        if not path.exists(filename):
            with open(f"{filename}", "wb") as fileToWrite:
                fileToWrite.write(ses.get(url).content)
            print(
                f"{POSITIVE_HL}[+]Downloaded {url} to {filename}{RESET}")
        else:
            print(
                f"{WARNING}[!]Skipping {url}, file {filename} already exists!{RESET}")


if __name__ == "__main__":
    checkParams()
    main()
