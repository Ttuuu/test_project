"""数据库相关操作"""
import pymysql

def addaAnswerRecord(item):
    """插入一条回答记录"""
    db = pymysql.connect("localhost","root","123456","codereview" )
    cursor = db.cursor()    
    sql="insert into answers_set(" \
                                "question_id, answer_id, score, owner_id, owner_reputation, is_accepted) " \
                                "values(%d, %d, %d, %d, %d, %d)"%\
                                (int(item['question_id']),int(item['answer_id'][0]),int(item['score'][0]),int(item['owner_id']),int(item['owner_reputation']),int(item['is_accepted'][0]=="acceptedAnswer"))
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("database error",e)
        db.rollback()
    finally:
        db.close()

def setQuestionVisited(question_id):
    """设置某问题为已访问状态"""
    db = pymysql.connect("localhost","root","123456","codereview" )
    cursor = db.cursor()    
    sql="update questions_set set vis =1  where question_id=%d;"%(question_id)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("database error",e)
        db.rollback()
    finally:
        db.close()

def getQuestionIdById(id):
    """通过id获取question_id"""
    db = pymysql.connect("localhost","root","123456","codereview" )
    cursor = db.cursor()    
    sql="select question_id from questions_set where id=%d and answer_count > 0 and vis =0;"%(id)
    try:
        if cursor.execute(sql) == 0:
        return 0
    else:
        return cursor.fetchone()[0]
    except Exception as e:
        print("database error",e)
        db.rollback()
    finally:
        db.close()

