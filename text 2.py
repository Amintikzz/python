f=open('rashyvruy slovo','w')
text={'a': '!',  'b': '@',  'c': '#',  'd': '$',  'e': '%',  'f': '^',
'g': '&',  'h': '*',  'i': '(',  'j': ')',  'k': '-',  'l': '_',
'm': '+',  'n': '=',  'o': '{',  'p': '}',  'q': '[',  'r': ']',
's': ':',  't': ';',  'u': '"',  'v': "'",  'w': '<',  'x': '>',
'y': '?',  'z': '/'}


f.write(text['n']+text['a']+text['r']+text['u']+text['t']+text['o'])
f=open("rashyvruy slovo","a")
f.write('''
a: !     b: @     c: #
d: $     e: %     f: ^
g: &     h: *     i: (     j: )     k: -     l: _
m: +     n: =     o: {     p: }     q: [     r: ]
s: :     t: ;     u: "     v: '     w: <     x: >
y: ?     z: /''')
f.close()
