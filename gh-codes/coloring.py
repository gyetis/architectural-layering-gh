__author__="GizemYetis, OzanYetkin, KongpyungMoon & Ozkan Kilic"
__mail__="yetis.gizem@metu.edu.tr, ozan.yetkin@metu.edu.tr, kpmoon@gmail.com & okilic@ybu.edu.tr"
__institution__="Middle East Technical University, Yildirim Beyazit University"

from Grasshopper import DataTree
c = [list(i) for i in category.Branches]
color = []
for j in c[0]:
    if j == "column":
        a.append("red")
    elif j == "beam":
        a.append("blue")
    elif j == "wall":
        a.append("green")
    elif j == "slab":
        a.append("yellow")
print(color)
