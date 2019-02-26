class ingredient:
    def __init__(self, name="", amount="", storeSection=""):
        self.name = name
        self.amount = amount
        self.storeSection = storeSection

    def print(self):
        print(f"{self.name}\t\t\t{self.amount}\t\t\t{self.storeSection}")

class recipie:
    def __init__(self, name="NONE", ingredients=[], steps=[]):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def printHeader(self, headerLine):
        print("\n")
        print(headerLine)
        dashLine = ""

        for character in headerLine:
            if character == '\t':
                dashline = dashLine + "===="
            else:
                dashLine = dashLine + "="

        print(dashLine)
        print("\n")
        
    def print(self):
        tabs = "\t\t\t\t"
        self.printHeader(f"Recipie:\t{self.name}")
        self.printHeader(f"Ing.{tabs}Amount{tabs}Store Loc.")

        for ing in self.ingredients:
            ing.print()
            
        self.printHeader(f"Steps")
        counter = 1
        for step in self.steps:
            print(f"{counter})\t{step}")
            counter = counter + 1

ingredients = [ingredient("Pickles", "1 jar", "Isle 3"),ingredient("Cheese", "2 slices", "Dairy"), ingredient("Ham", "3 slices", "Deli"), ingredient("Bread", "2 slices", "Bakery")]
steps = ["Place down 1 slice of bread","Add the cheese","Add the pickles", "Add the Ham", "Add the 2nd slice of bread"]


sandwich = recipie("Ham Sandwich", ingredients, steps)

sandwich.print()
