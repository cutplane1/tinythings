import dataclasses
import enum
import os

VER = "0.0.0.3-pre-pre-pre-alpha"

@dataclasses.dataclass
class Product:
    code: int
    price: int
    desc: str

@dataclasses.dataclass
class InRecord:
    product: Product
    _how_much: int = 0
    total_cost: int = 0

    @property
    def how_much(self):
        return self._how_much

    @how_much.setter
    def how_much(self, value):
        self._how_much = value
        self.total_cost = self.product.price * self._how_much
  

list_of_products = [Product(code=1, price=1, desc='ripe tomato'), Product(code=2, price=5, desc='white cauliflower'), Product(code=3, price=4, desc='dark-green broccoli'), Product(code=4, price=3, desc='red apple'), Product(code=5, price=2, desc='green pear'), Product(code=6, price=3, desc='juicy orange'), Product(code=7, price=2, desc='orange carrot'), Product(code=8, price=6, desc='yellow banana'), Product(code=9, price=3, desc='dark-green broccoli'), Product(code=10, price=2, desc='white cauliflower')]

class AddInfo(enum.Enum):
    NEW = 0
    PLUSONE = 1

class NotFoundException(Exception):
    pass

class DB:
    def __init__(self, list_of_products):
        self.base: list[Product] = list_of_products
        self.db: list[InRecord] = []


    def add(self, i: int) -> AddInfo:
        rec: Product = None
        # it could be sql query
        for r in self.base:
            if r.code == i:
                rec = r
        if rec == None:
            raise NotFoundException('not found in db')
            return
        
        for r in self.db:
            if r.product == rec:
                r.how_much += 1
                return AddInfo.PLUSONE
        
        self.db.append(InRecord(rec, 1, rec.price))
        return AddInfo.NEW

    def total(self) -> int:
        return sum([a.total_cost for a in self.db])


n = DB(list_of_products=list_of_products)

# le frontend
class FrontendBase:
    def __init__(self,nano: DB):
        self.nano = nano
        self.err_msg: str = ""
        self.info_msg: str = ""
        self.cur = -1

    def up(self):
        if self.cur <= 0:
            self.cur = len(self.nano.db)-1
        else:
            self.cur -= 1
    
    def down(self):
        if self.cur >= len(self.nano.db)-1:
            self.cur = 0
        else:
            self.cur += 1
    
    def add(self, i: int):
        try:
            a = self.nano.add(i)
            if a == AddInfo.NEW:
                self.cur += 1
        except NotFoundException as e:
            self.err_msg = str(e)
    
    def multiply(self, x: int):
                self.nano.db[self.cur].how_much = x

    def delete(self):
        self.nano.db.pop(self.cur)
        self.cur = len(self.nano.db)-1
    
    def checkout(self):
        cur = -1
        self.nano.db = []
    

def print_inverted(x:str):
    BLACK_TEXT = '\033[30m'
    WHITE_BACKGROUND = '\033[47m'
    RESET = '\033[0m'
    print(f"{WHITE_BACKGROUND}{BLACK_TEXT}{x}{RESET}")

def portable_clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')
    else:
        raise Exception('your os is not supported atm')


class CliFrontend(FrontendBase):
    def __init__(self, nano):
        super().__init__(nano)
    
    def format_output(self):
        if self.info_msg != "": print(self.info_msg); self.info_msg = ""
        for i, r in enumerate(self.nano.db):
            s = f"Price {r.product.price}; Desc: {r.product.desc}; Amount: {r.how_much}; Total: {r.total_cost}"
            if i == self.cur:
                print_inverted(s)
            else:
                print(s)
        print("-"*16)
        
        print("TOTAL:", self.nano.total(), "of money")
        if self.err_msg != "": print(self.err_msg); self.err_msg = ""
    
    def run(self):
        while True:
            portable_clear()
            self.format_output()

            i = input(f"nanoPOS {VER}> ")

            if i.isnumeric():
                self.add(int(i))
            elif i.startswith("x"):
                self.multiply(int(i[1:]))
            elif i == "k":
                self.down()
            elif i == "j" or i == "\t":
                self.up()
            elif i == "del":
                self.delete()
            elif i.startswith("c"):
                hv = int(i.split()[1])
                self.info_msg = "CHARGE: " + str(hv-self.nano.total())
                self.checkout()

CliFrontend(n).run()
