m=[[1,0,1],[1,1,0],[0,1,1]]
ocup=sum(x for l in m for x in l)
print("Ocupadas:",ocup,"Disponíveis:",9-ocup)
