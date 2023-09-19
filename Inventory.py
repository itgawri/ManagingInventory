class Product:
    def __init__(self, name, price, units):
        self.name = name
        self.price = price
        self.units = units
        self.is_on_sale = False

    def describe(self):
        print(f"Product name: {self.name}")
        print(f"Product price: ${self.price:.2f}")
        print(f"Available units: {self.units}")
        print(f"On sale? {self.is_on_sale}")
        print(f"In stock? {self.is_in_stock()}")
        print(f"Total inventory value: ${self.calculate_inventory_value():.2f}")
        print("-------------------------")

    def add_units(self, units):
        if isinstance(units, int) and units > 0:
            self.units += units
        else:
            print("Error: Invalid units value.")

    def reduce_units(self, units):
        if isinstance(units, int) and units > 0:
            if self.units - units >= 0:
                self.units -= units
            else:
                print("Error: Not enough units in inventory.")
        else:
            print("Error: Invalid units value.")

    def reduce_price(self, discount):
        if 0 <= discount <= 1:
            self.price = self.price * (1 - discount)
            self.is_on_sale = True
        else:
            print("Error: Invalid discount value.")

    def is_in_stock(self):
        return self.units > 0

    def calculate_inventory_value(self):
        return self.price * self.units


laptop = Product("Dell Laptop", 850, 12)
laptop.describe()
laptop.add_units(15)
laptop.reduce_units(10)
laptop.reduce_units(20)
laptop.reduce_price(0.1)
laptop.describe()

# PL-------------------------------------------------------------------------

class Produkt:
  def __init__(self, nazwa, cena, jednostki):
    self.nazwa = nazwa
    self.cena = cena
    self.jednostki = jednostki
    self.jest_przeceniony = False

  def opis(self):
    print(f"Nazwa produktu: {self.nazwa}")
    print(f"Cena produktu: {self.cena:.2f} zł")
    print(f"Dostępne jednostki: {self.jednostki}")
    print(f"Czy jest przeceniony? {self.czy_jest_w_przecenie()}")
    print(f"Całkowita wartość zapasów: {self.oblicz_wartosc_zapasow():.2f} zł")
    print("-------------------------")

  def dodaj_jednostki(self, jednostki):
    if isinstance(jednostki, int) and jednostki > 0:
      self.jednostki += jednostki
    else:
      print("Błąd: Nieprawidłowa wartość jednostek.")

  def zmniejsz_jednostki(self, jednostki):
    if isinstance(jednostki, int) and jednostki > 0:
      if self.jednostki - jednostki >= 0:
        self.jednostki -= jednostki
      else:
        print("Błąd: Brak wystarczającej liczby jednostek na stanie.")
    else:
      print("Błąd: Nieprawidłowa wartość jednostek.")

  def zmniejsz_cene(self, rabat):
    if 0 <= rabat <= 1:
      self.cena = self.cena * (1 - rabat)
      self.jest_przeceniony = True
    else:
      print("Błąd: Nieprawidłowa wartość rabatu.")

  def czy_jest_w_przecenie(self):
    return self.jest_przeceniony

  def oblicz_wartosc_zapasow(self):
    return self.cena * self.jednostki


laptop = Produkt("Laptop Dell", 850, 12)
laptop.opis()
laptop.dodaj_jednostki(15)
laptop.zmniejsz_jednostki(10)
laptop.zmniejsz_jednostki(20)
laptop.zmniejsz_cene(0.1)
laptop.opis()
