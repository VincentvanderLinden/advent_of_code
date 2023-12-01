with open('q02.in') as f: 
    presents = f.read().splitlines()

def calc_surface_area(l, w, h): 
    s = sorted([l, w, h])
    return 2*l*w + 2*w*h + 2*h*l + s[0]*s[1] 

def calc_ribbon_length(l, w, h): 
    s = sorted([l, w, h])
    return l*w*h + s[0]*2 + s[1]*2 

paper_length = 0
ribbon_length = 0

for present in presents: 
    l, w, h = map(int, present.split('x'))
    paper_length += calc_surface_area(l, w, h)
    ribbon_length += calc_ribbon_length(l, w, h)

print(f"Answer 1 :{paper_length}")
print(f"Answer 2 :{ribbon_length}")

