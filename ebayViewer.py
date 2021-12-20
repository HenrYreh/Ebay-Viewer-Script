import requests
import time

delay = 1                        #delay for viewing.

def view(link,amount):                                                  #view function.
    success = 0
    failed = 0

    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    print(f"Attempting to view {amount} amount of times. Please wait.")
    for x in range(amount):                                             #send GET Requests to link until amount is met.
        response = requests.get(url=link,headers=headers)
        if response.ok == True:
            print(f"View Success.")
            success = success + 1
        else:
            print(f"View failed.")
            failed = failed + 1
        time.sleep(delay)

    print("Task Complete.\n")
    print(f"{success} view(s) viewed successfully.")
    print(f"{failed} view(s) failed to view.")


def start():
    linkStatus = False
    amountStatus = False

    while (linkStatus == False) or (amountStatus == False):             #loop continues until both inputs are valid.
        linkStatus = True
        amountStatus = True

        print("Ebay Viewer.\n")

        link = input("Please Enter URL:")                           #link format 'https://www.ebay.com/itm/XXXXXXXXXXXX'

        if "https://www.ebay"  not in link:
            linkStatus = False
            print("Invalid Link. Please try again.\n")

        else:
            try:
                amount = int(input("Please Enter Amount of Views:"))
            except:
                amountStatus = False

                print("Input Invalid.\n")



    print(f"Your link is {link} and you want to view {amount} time(s)")
    view(link,amount)                                                       #call view function.

#---------------------------------Start-------------------------------------------


if __name__ == '__main__':
    start()


