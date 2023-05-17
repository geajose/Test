from fastapi import FastAPI, Depends, status, HTTPException
from . import models
from . import schemas
from sqlalchemy.orm import Session
from .database import engine,SessionLocal
from datetime import date

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

#post

@app.post('/employee')
def create(request:schemas.Blog, db:Session=Depends(get_db)):
    today = date.today()
    new_blog = models.Employee(employee_id = request.employee_id,name = request.name,joining_date = request.joining_date,role = request.role,
    status = request.status,dept_id=request.dept_id,start_date = request.start_date,experience=today.year - request.start_date.year - ((today.month, today.day) < (request.start_date.month, request.start_date.day)),
    address_line1=request.address_line1,address_line2 =request.address_line2,state = request.state,pincode = request.pincode)
    

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.post('/department')
def create_department(request:schemas.Department,db:Session=Depends(get_db)):
    new_dept=models.Department(dept_id=request.dept_id,dept_name=request.dept_name)
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept


#delete


@app.delete('/employee/{emp_id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(emp_id,db:Session=Depends(get_db)):
    blog=db.query(models.Employee).filter(models.Employee.employee_id==emp_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"Blog with id {emp_id} not fount")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@app.delete('/department/{dep_id}',status_code=status.HTTP_204_NO_CONTENT)
def del_dept(dep_id,db:Session=Depends(get_db)):
    dep=db.query(models.Department).filter(models.Department.dept_id==dep_id)
    if not dep.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"Blog with id {dep_id} not fount")

    dep.delete(synchronize_session=False)
    db.commit()
    return 'done'




#update



@app.put('/employee/{emp_id}',status_code=status.HTTP_202_ACCEPTED)
def update(emp_id,request:schemas.Blog, db:Session=Depends(get_db)):
    db.query(models.Employee).filter(models.Employee.employee_id==emp_id).update(request)
    db.commit()
    return 'updated'


@app.put('/department/{dep_id}',status_code=status.HTTP_202_ACCEPTED)
def update_dept(dep_id,request:schemas.Department, db:Session=Depends(get_db)):
     db.query(models.Department).filter(models.Department.dept_id==dep_id).update(request)
     db.commit()
     return 'updated'









@app.get('/employee/{emp_id}')
def show(emp_id,db:Session=Depends(get_db)):
    results= db.query(models.Employee).filter(models.Employee.employee_id==emp_id).first()
    return results


    
