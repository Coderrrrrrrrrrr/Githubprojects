import sqlite3
from bottle import route, run, request, template


# conn = sqlite3.connect('todo.db')
# conn.execute("create table todo (id integer primary key, task char(100) not null, status bool Not Null)")
# conn.execute("insert into todo(task,status) values ('加十个小姐姐微信',0)")
# conn.execute("insert into todo(task,status) values ('赚它1个亿',1)")
# conn.execute("insert into todo(task,status) values ('大笑10下',1)")
# conn.commit()

@route('/edit/<no:int>',method='get')
def edit_item(no):
    if request.GET.save:
        edit=request.GET.task.strip()
        status=request.GET.status.strip()

        if status=='open':
            status=1
        else:
            status=0

        conn=sqlite3.connect('todo.db')
        c=conn.cursor()
        c.execute("update todo set task=?,status=? where id like ?",(edit,status,no))
        conn.commit()

        return '<p>成功提交计划 ID：%s</p>'% no
    else:
        conn=sqlite3.connect('todo.db')
        c=conn.cursor()
        c.execute("select task from todo where id like ?",(str(no),))
        cur_data=c.fetchone()

        return template('edit_task.tpl',old=cur_data,no=no)

@route('/todo')
def todo_list():
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute("select id,task from todo where status like '1'")
    result=c.fetchall()
    c.close()
    output=template('make_table.tpl',rows=result)
    return output

@route('/new',method='get')
def new_task():
    if request.GET.save:
        new=request.GET.task.strip()
        conn=sqlite3.connect('todo.db')
        c=conn.cursor()
        c.execute("insert into todo (task,status) values (?,?)",(new,1))
        new_id=c.lastrowid
        conn.commit()
        c.close()
        return '<p>成功添加数据，ID为：%s</p>'% new_id
    else:
        return template('new_task.tpl')

run(reloader=True,host='localhost',port=7777)

@error(404)
def mistake404(code):
    return 'Sorry,你要的网页找不到'