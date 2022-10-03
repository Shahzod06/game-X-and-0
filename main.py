g = [1,2,3,4,5,6,7,8,9]
def chiz():
     print(f"""
                 {g[0]} |   {g[1]} |   {g[2]}
                 _ _ _ _ _ _ _
                 {g[3]} |   {g[4]} |   {g[5]}
                 _ _ _ _ _ _ _ 
                 {g[6]} |   {g[7]} |   {g[8]}
""")
chiz()
def mantiq(band):
     x0= int(input(band +'='))
     while isinstance(g[x0-1],str):
          x0 = int(input(band + '='))
     g[x0 - 1] = band
     chiz()
     if g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]== g[4] and g[4]==g[7] or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or g[2]== g[4] and g[4]==g[6]:
          print(band + ' yutdi! O\'yin tugadi. Agar xohlasangiz qayta urunib ko\'rishingiz mumkin!')
          return True
     return False

while True:
     if mantiq('x') or mantiq('0'):
          break
