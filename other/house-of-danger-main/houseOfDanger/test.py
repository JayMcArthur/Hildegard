import pandas as pd

dangerMeter = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 2, 2, 2]
dangDict = {'Water Bottle': (3, 'Discard at any time to lower Danger Meter by 3'), 'sandwhich': (4, 'Disalskdhf')}
psychDict = {}
climbDict = {}
fightDict = {'Pocketknife': (1, 'Increase Fighting roll by 1')}
dextDict = {}
percDict = {}
strengthDict = {}
items = {}
images = {}
inv = {'danger': dangDict, 'psychic': psychDict, 'climbing': climbDict, 'fighting': fightDict, 'dexterity': dextDict,
       'perception': percDict, 'strength': strengthDict, 'items': items, 'images': images}


a = []
b = []
c = []
for x in inv.items():
       if len(x[1]) > 0:
              for y in x[1]:
                     a.append(x[0])
                     b.append(y)
                     c.append(x[1][y][0])
df = pd.DataFrame(a, columns=['Category'])
df['Name'] = b
df['Amount/Desc'] = c
print(df)
