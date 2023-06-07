def main():
    print("Hello Nigga, ")
    print("")
    
    email_input = input("Kindly Instanciate with your Email: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("username: ", username)
    print("Domain: ", domain)
    print("username: ", extension)

while True:
    main()
    