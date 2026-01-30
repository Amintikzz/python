n = ['Jacob','Max','Nate', 'George','Alikhan']

if len(n) == 0:
    print('No one likes this')
elif len(n) == 1:
    print(n[0], 'likes this')
elif len(n) == 2:
    print(n[0], 'and', n[1], 'likes this')
elif len(n) == 3:
    print(f'{n[0]}, {n[1]} and {n[2]} likes this')
elif len(n) > 3:
    print(f'{n[0]}, {n[1]} and {len(n)-2} others likes this')
    
