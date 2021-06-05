while(True):
    print("███████╗ ██████╗██████╗  █████╗ ██████╗       ██╗████████╗██╗")
    print("██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗      ██║╚══██╔══╝██║")
    print("███████╗██║     ██████╔╝███████║██████╔╝█████╗██║   ██║   ██║")
    print("╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ╚════╝██║   ██║   ╚═╝")
    print("███████║╚██████╗██║  ██║██║  ██║██║           ██║   ██║   ██╗")
    print("╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝           ╚═╝   ╚═╝   ╚═╝") 

    print("\n")
    print("Select from the following options...")
    print("1) Compare the price of a product from multiple sites.")
    print("2) Get details about the Covid-19 situation in India.")
    print("3) Get a list of the top 100 best movies on imdb.")
    print("4) To find the highest or lowest temperature on Earth today with the name of the place.")
    print("5) Analyze different type of data from a wikipedia page.")
    print("\n")
    a=int(input("Select from the above options : "))
    if(a==1):
        import compare
    elif(a==2):
        import covid19
    elif(a==3):
        import imdb
    elif(a==4):
        import temp
    elif(a==5):
        import scrap_wiki
    else:
        print("Entered option is invalid! Please Try Again...")
    print("-------------------------------------------------------------------------------------------------------------")