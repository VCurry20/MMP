
#You can achieve this by using range() to loop the amount of times input under value.

#The for loop defines, from 0 --> values and will loop over the code the specified amount of times.

values = int(input('Number of addresses: '))

#>>>Enter a value: 2

def addresss():
    addresses = []
    for i in range(0, 100):
        value = input('Enter a Value: ')
        volume = input('Enter the Volume: ')
        weight = input('Enter the Weight: ')
        userinput = [value, volume, weight]
        addresses.append(userinput)
    #print(addresses)



    def newAddresss():
        
        for i in range(0, 100):
            house_number = input('Enter a House Number: ')
            street = input('Enter the Street: ')
            town = input('Enter the town: ')
            county = input('Enter the county: ')
            eircode = input('Enter the eircode: ')
            country = input('Enter the country: ')
            userinput = [house_number, street , town, county, eircode, country]
            addresses.append(userinput)
        #print(addresses)



    #addresses = []

    def address_input():
         while True:
              userinput = (input("Enter your address"))
              if userinput == 0:
                   break
              else:
                   addresses.append(userinput)



##

    def newAddress():
         for i in range(0, 100):
            house_number = input('Enter a House Number: ')
            street = input('Enter the Street: ')
            town = input('Enter the town: ')
            county = input('Enter the county: ')
            eircode = input('Enter the eircode: ')
            country = input('Enter the country: ')
            userinput = [house_number, street , town, county, eircode, country]
            address.append(userinput)



    def addAddress(self, address):
         self.address.append(address)
         print(f"address is something I am lost")