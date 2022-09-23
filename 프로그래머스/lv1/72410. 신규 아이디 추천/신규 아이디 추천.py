def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    for i in new_id:
        if not (i=="-" or i=="_" or i=="." or i.isdigit() or i.islower()):
            new_id = new_id.replace(i,'')
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    new_id = new_id.strip('.')
    
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    elif len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id+new_id[-1]
    
    return new_id