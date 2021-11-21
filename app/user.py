from db import db

def add_user(name,password,email,gender,birthday,weight,height):
  sql="INSERT INTO users VALUES (:name,:password,:email,:gender,:birthday,:weight,:height)"
  result = db.session.execute(sql, {"name":name,"password":password,"email":email,"gender":gender,
                                    "birthday":birthday,"weight":weight,"height":height})
  db.session.commit()

def get_user(name,password):
  sql = "SELECT user_id FROM users WHERE name=:name AND password=:password"
  result = db.session.execute(sql,{"name":name,"password":password})
  user = result.fetchone()
  return user

def login(name,password):
  user = get_user(name,password)
  if not user:
    return False
  else:
    if check_password_hash(user.password,password):
      session["user_id"] = user.id
      return True
    else:
      return False

def get_exes():
  result = db.session.execute("SELECT calories from user_exes as e INNER JOIN users as u ON e.user_id=u.user_id")
  return result.fetchall()

def get_diets():
  result = db.session.execute("SELECT calories from user_diets as d INNER JOIN users as u ON d.user_id=u.user_id")
  return result.fetchall()

#for users adding new exercise record
def new_exes(exe_name,length,cal,date):
  id_sql = "SELECT exe_id from exes WHERE exe_name=:exe_name"
  id = db.session.execute(id_sql,{"exe_name":exe_name}).fetchone()
  cal_sql = "SELECT calories from exes WHERE exe_name=:exe_name"
  cal = db.session.execute(cal_sql,{"exe_name"}:exe_name).fetchone()
  id = id_fetch.fetchone()[0]
  cal = cal_fetch.fetchone()[0]
  result = db.session.execute("INSET INTO user_exes VALUES (:id,:exe_name,:length,:cal*:length,:date)",
                              "id":id,"exe_name":exe_name,"length":length,"cal":cal,"date":date)
  db.session.commit()

#for users adding new diet record
def new_diets():
    #to be continued
    #the calories of diets are ideally calculated based on
    #what ingredients and how much


