from pydantic import BaseModel
from datetime import date

class Blog(BaseModel):
    employee_id:int
    name:str
    joining_date : date
    role : str
    status : str
    dept_id : int
    start_date : date
    address_line1:str
    address_line2 : str
    state : str
    pincode : int



    class Config:
        orm_mode = True


class Department(BaseModel):
    dept_id:int
    dept_name:str



    class Config:
        orm_mode=True
