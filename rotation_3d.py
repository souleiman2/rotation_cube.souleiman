import math
from PIL import Image, ImageDraw
import imageio


pi = 3.14159265359

def matrix_mult(matrix1, matrix2, matrix_fin): # [range][colonne]

    for i in range(len(matrix2[0])):# les colonnes de la matrice 2
        for j in range(len(matrix1)): # les rangés de la matrice 1
            
#   à partir de ce moment l'exosquelette de la matrice ce dessine
#   maintenant il faut calculer les valeurs de la matrice
            result = 0
            for k in range(len(matrix2)): # on assume que la matrice2 a le meme nombre de rangé que de colonne dans la matrice1
                result += matrix1[j][k] * matrix2[k][i]
            
            matrix_fin[j][i] = result






taille = [400,400]

c = 50
cube = [[-c,c,c], [c,c,c], [c,-c,c], [-c,-c,c], [-c,c,-c], [c,c,-c], [c,-c,-c], [-c,-c,-c] ]

#                    [-c,c,-c] [c,c,-c]

# [-c,c,c]  [c,c,c]  [-c,-c,-c] [c,-c,-c]
 
# [-c,-c,c] [c,-c,c]
center = [taille[0]//2, taille[1]//2]

angle_deg = 0
angle = 0

sommet = []


maxAngle = 360



compteur = 0


for i in range(8):
    sommet.append([0,0])


#win = GraphWin("Rotation 3d", taille[0], taille[1])
#win.setBackground("white")
    

im = []
aLine = []
filenames = []

MR = [[],[],[]]
MRF = [[],[],[]]
for i in range(3):
     for j in range(3):
        MR[j].append(0)
        MRF[j].append(0)

while angle_deg <= maxAngle:
    im.append(Image.new( "RGB", (taille[0], taille[1]) ) )
    filenames.append("Cube_rotation" + str(compteur) + ".png")
    
    for i in range(12):
        aLine.append(ImageDraw.Draw(im[compteur]) )
        
    #matrice de rotation
    R_x = [[1,0,0],
           [0,math.cos(angle), -math.sin(angle)],
           [0, math.sin(angle), math.cos(angle)]]
    
    R_y = [[math.cos(angle), 0, math.sin(angle)],
           [0,1,0],
           [-math.sin(angle), 0, math.cos(angle)]]
    
    R_z = [[math.cos(angle), -math.sin(angle), 0],
           [math.sin(angle), math.cos(angle), 0],
           [0,0,1]]

    matrix_mult(R_x, R_z, MR)
    matrix_mult(MR,R_y , MRF)
    
    
    for i in range(8):
        sommet[i] = [center[0] + MRF[0][0]*cube[i][0] + MRF[0][1]*cube[i][1] + MRF[0][2]*cube[i][2],
                     center[1] + MRF[1][0]*cube[i][0] + MRF[1][1]*cube[i][1] + MRF[1][2]*cube[i][2]]

    
    

    aLine[0].line((sommet[0][0], sommet[0][1], sommet[1][0], sommet[1][1]), fill = 128)
    aLine[1].line((sommet[1][0], sommet[1][1], sommet[2][0], sommet[2][1]), fill = 128)
    aLine[2].line((sommet[2][0], sommet[2][1], sommet[3][0], sommet[3][1]), fill = 128)
    aLine[3].line((sommet[3][0], sommet[3][1], sommet[0][0], sommet[0][1]), fill = 128)
    aLine[4].line((sommet[0][0], sommet[0][1], sommet[4][0], sommet[4][1]), fill = 128)
    aLine[5].line((sommet[1][0], sommet[1][1], sommet[5][0], sommet[5][1]), fill = 128)
    aLine[6].line((sommet[2][0], sommet[2][1], sommet[6][0], sommet[6][1]), fill = 128)
    aLine[7].line((sommet[3][0], sommet[3][1], sommet[7][0], sommet[7][1]), fill = 128)
    aLine[8].line((sommet[4][0], sommet[4][1], sommet[5][0], sommet[5][1]), fill = 128)
    aLine[9].line((sommet[5][0], sommet[5][1], sommet[6][0], sommet[6][1]), fill = 128)
    aLine[10].line((sommet[6][0], sommet[6][1], sommet[7][0], sommet[7][1]), fill = 128)
    aLine[11].line((sommet[7][0], sommet[7][1], sommet[4][0], sommet[4][1]), fill = 128)

    
    for i in range(12):
        del aLine[0]
    
##    for i in range(12):
##        aLine[i].draw(win)
##
##    time.sleep(0.1)
##
##    for i in range(12):
##        aLine[i].undraw()

    im[compteur].save("Cube_rotation" + str(compteur) + ".png", "PNG")
    print("image " + str(compteur) + " done!")
        
        
    angle_deg += 6
    angle = angle_deg * pi / 180

    compteur +=1
    

    
    
with imageio.get_writer('movie2.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)  
#win.close()
