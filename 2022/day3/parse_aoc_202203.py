import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

#puzzle_input = pathlib.Path('input.txt').read_text().strip()
puzzle_example = pathlib.Path(PUZZLE_DIR / "example.txt").read_text().strip()
puzzle_input = puzzle_example.split()
curated_input = []
for line in puzzle_input:
    curated_input.append([x for x in line])
item_list= []
for rucksacks in curated_input:
        count = len(rucksacks)
        for x in rucksacks[:int(count/2)]:
            if x in rucksacks[int(count/2):]:
                item_list.append(x)
                break
#print(item_list)
priorities_dic = {
    'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
    'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,
    'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,
    'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,
    'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,
    'Z':52
}
priorities_list = []
for i in item_list:
    priorities_list.append(priorities_dic.get(i))
#print(sum(priorities_list))
data = curated_input
badge_list = []
i = 0
while i <= len(data) -2:
    for x in data[i + 0]:
        if x in data[i + 1]:
            if x in data[i + 2]:
                badge_list.append(x)
                break
    i += 3
print(badge_list)