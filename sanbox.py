class Country:
    def __init__(self, continent, country):
        self.continent = continent
        self.country = country
    def __str__(self):
        return f"Country{{country='{self.country}', continent='{self.continent}}}"

def main():
    fruits = ['apple', 'banana', 'grape', 'orange']
    print(fruits[0], fruits[1], fruits[2], fruits[3])
    print(*fruits)

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    dict = {"continent":"asia", "country":"china"}
    print(*dict) # will print out the keys only
    print(Country(**dict)) # will pass the key/value pairs as named parameters



if __name__ == "__main__":
    main()

