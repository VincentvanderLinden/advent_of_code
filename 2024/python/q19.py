import re 
with open('q19.in') as f: 
    p, t  = f.read().split('\n\n')

# pattern = '^(' + '|'.join(p.split(', ')) + (')*$')
# towels = t.splitlines()

# wheee gode golf
print("Answer 1:", sum((1 for m in (re.match('^(' + '|'.join(p.split(', ')) + (')*$'), t) for t in t.split('\n')) if m)))
