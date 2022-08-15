import dbinfo

def db_query(query, *arg):
    args = [0]*10
    for i in range(len(arg)):
        args[i] = arg[i]
    
    query_list ={
        'getall' : f"select * from {args[0]} ",
        'insertuser' : f"insert into {args[0]} ({args[1]}, {args[2]}) values({args[3]}, '{args[4]}')" 
    }
    return query_list[query]
