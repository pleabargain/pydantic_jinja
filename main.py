from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

class Car(BaseModel):
    color: str

class Manufacturer(BaseModel):
    name: str

class Year(BaseModel):
    year: int

class Price(BaseModel):
    price: int

class EngineSize(BaseModel):
    size: str

class InternalOptions(BaseModel):
    leather_seats: bool = False
    electric_windows: bool = False
    heated_seats: bool = False
    air_conditioning: bool = False

class CarSelection(BaseModel):
    color: str
    manufacturer: str
    year: int
    price: int
    engine_size: str
    internal_options: InternalOptions

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# Data for demonstration
cars = sorted([Car(color="green"), Car(color="blue"), Car(color="yellow"), Car(color="black"), Car(color="white"), Car(color="red")], key=lambda x: x.color)
manufacturers = sorted([Manufacturer(name="chevy"), 
                        Manufacturer(name="ford"), 
                        Manufacturer(name="toyota"), 
                        Manufacturer(name="nissan"), 
                        Manufacturer(name="mazda"), 
                        Manufacturer(name="BMW"),
                        Manufacturer(name="Audi"),
                        Manufacturer(name="Mercedes"),
                        Manufacturer(name="subaru"), 
                        Manufacturer(name="honda")], key=lambda x: x.name)
years = sorted([Year(year=1980), 
                Year(year=1989),
                Year(year=1908),
                Year(year=1981), Year(year=1982)], key=lambda x: x.year)


engine_sizes = ["4 cylinder", "6 cylinder", "8 cylinder"]

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {
        "request": request, 
        "cars": cars, 
        "manufacturers": manufacturers, 
        "years": years,
        "engine_sizes": engine_sizes
    })

@app.post("/", response_class=JSONResponse)
async def form_post(
    color: str = Form(...), 
    manufacturer: str = Form(...), 
    year: int = Form(...), 
    price: int = Form(...),
    engine_size: str = Form(...),
    leather_seats: bool = Form(False),
    electric_windows: bool = Form(False),
    heated_seats: bool = Form(False),
    air_conditioning: bool = Form(False)):
    
    internal_options = InternalOptions(
        leather_seats=leather_seats,
        electric_windows=electric_windows,
        heated_seats=heated_seats,
        air_conditioning=air_conditioning
    )
    car_selection = CarSelection(
        color=color, 
        manufacturer=manufacturer, 
        year=year, 
        price=price,
        engine_size=engine_size,
        internal_options=internal_options
    )
    return car_selection.dict()

# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# from typing import List

# class Car(BaseModel):
#     color: str

# class Manufacturer(BaseModel):
#     name: str

# class Year(BaseModel):
#     year: int

# class Price(BaseModel):
#     price: int

# class CarSelection(BaseModel):
#     color: str
#     manufacturer: str
#     year: int
#     price: int

# app = FastAPI()
# templates = Jinja2Templates(directory='templates')

# #TODO add jinja calendar interface for year 

# # Data for demonstration, sorted alphabetically
# cars = sorted([Car(color="green"), Car(color="blue"), Car(color="yellow"), Car(color="black"), Car(color="white"), Car(color="red")], key=lambda x: x.color)
# manufacturers = sorted([Manufacturer(name="chevy"), 
#                         Manufacturer(name="ford"), 
#                         Manufacturer(name="toyota"), 
#                         Manufacturer(name="nissan"), 
#                         Manufacturer(name="mazda"), 
#                         Manufacturer(name="BMW"),
#                         Manufacturer(name="Mercedes"),
#                         Manufacturer(name="subaru"), 
#                         Manufacturer(name="honda")], key=lambda x: x.name)
# years = sorted([Year(year=1980), 
#                 Year(year=1989),
#                 Year(year=1908),
#                 Year(year=1981), Year(year=1982)], key=lambda x: x.year)

# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse('index.html', {"request": request, "cars": cars, "manufacturers": manufacturers, "years": years})

# @app.post("/", response_class=JSONResponse)
# async def form_post(color: str = Form(...), manufacturer: str = Form(...), year: int = Form(...), price: int = Form(...)):
#     car_selection = CarSelection(color=color, manufacturer=manufacturer, year=year, price=price)
#     return car_selection.dict()



# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# from typing import List

# class Car(BaseModel):
#     color: str

# class Manufacturer(BaseModel):
#     name: str

# class CarSelection(BaseModel):
#     color: str
#     manufacturer: str

# app = FastAPI()
# templates = Jinja2Templates(directory='templates')

# # Data for demonstration, sorted alphabetically
# cars = sorted([Car(color="green"),
#                Car(color="blue"  ) ,
#                Car(color="yellow"),
#                Car(color="black" ),
#                Car(color="white" ),
#                Car(color="red")], key=lambda x: x.color)
# manufacturers = sorted([Manufacturer(name="chevy"), 
#                         Manufacturer(name="ford"),
#                         Manufacturer(name="toyota"),
#                         Manufacturer(name="nissan"),
#                         Manufacturer(name="mazda"),
#                         Manufacturer(name="subaru"),
#                         Manufacturer(name="honda")], key=lambda x: x.name)

# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse('index.html', {"request": request, "cars": cars, "manufacturers": manufacturers})

# @app.post("/", response_class=JSONResponse)
# async def form_post(color: str = Form(...), manufacturer: str = Form(...)):
#     car_selection = CarSelection(color=color, manufacturer=manufacturer)
#     return car_selection.dict()
