from flask import Flask,redirect,url_for,render_template,jsonify,request
from flaskext.mysql import MySQL
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOUSE']='location'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='45298'
app.config['MYSQL_DATABASE_DB']='library'
mysql=MySQL(app)
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    cursor=mysql.get_db().cursor()
    cursor.execute('select *from books')
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route('/addlibrary',methods=['GET','POST'])
def add():
    if request.method=='POST':
        bid1=request.form['bid']
        bname=request.form['bname']
        bauthor=request.form['bauthor']
        cursor=mysql.get_db().cursor()
        cursor.execute('insert into books(bid,bname,bauthor) values(%s,%s,%s)',[bid1,bname,bauthor]) 
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('add.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        bid1=request.form['bid']
        bname=request.form['bname']
        bauthor=request.form['bauthor']
        cursor=mysql.get_db().cursor()
        cursor.execute('update books set bname=%s,bauthor=%s,where bid=%s',[bname,bauthor,bid1])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        bid1=request.form['bid']
        bname=request.form['bname']
        bauthor=request.form['bauthor']
        cursor=mysql.get_db().cursor()
        cursor.execute('delete from books where bid=%s',[bid1])
        mysql.get_db().commit()
        return redirect(url_for('home'))
    return render_template('delete.html')
app.run(use_reloader=True)
          
    
        
    
           
