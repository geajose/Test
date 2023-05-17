

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.types import Date

from .database import Base

from sqlalchemy.orm import relationship


class Employee(Base):
    
    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    joining_date = Column(Date)
    role = Column(String)
    status = Column(String)
    dept_id = Column(Integer, ForeignKey("department.dept_id"),nullable=False)
    start_date = Column(Date)
    experience = Column(Integer,default=None)
    address_line1 = Column(String)
    address_line2 = Column(String)
    state = Column(String)
    pincode =  Column(Integer)


    people = relationship("Department", back_populates="team")


# class Employee_address(Base):
#      __tablename__ = "employee_address"

#      emp_id = Column(Integer, ForeignKey("employee.employee_id"),primary_key=True)



class Department(Base):
    __tablename__ = "department"

    dept_id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String)
    team= relationship("Employee", back_populates="people")






