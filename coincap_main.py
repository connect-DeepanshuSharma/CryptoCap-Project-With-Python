import json
import requests
import os

os.system('cls')
def main():


    def menu():
        print("Select a choice to perform the concerned operation ")
        print("1. Have a look at the portfolio of your cryptocurrency")
        print("2. See the Latest Alerts in the Market of Cryptocurrency")
        print("3. Explorer the Hourly,Daily and Weekly Updates of cryptocurrency ")
        print("4. Look into the future of the market values of cryptocurrency")
        print("5. Generate an Excel Sheet for various cryptocurrency")

    def replayMenu():
        startover = ""
        startover = input("Would you like to see further features, yes or no? ")
        while startover.lower()!= "yes":
            print("Thanks for visitng us! Bye! ")
            break
        else:
            main()

    menu()
    ch = input('Enter the choices (1-5) or print 6 to exit')

    if ch =='1':
        os.system ('python coincap_portfolio.py')

    elif ch == '2':
        os.system('python coincap_alert.py')
    elif ch == '3':
        os.system('python coincap_explorerMenu.py')
    elif ch == '4':
        os.system('python coincap_ValuePrediction.py')
    elif ch == '5':
        os.system('python coincap_excel.py')
    while ch == '6':
            break #exits out of the program
    else:
            replayMenu()

main()
