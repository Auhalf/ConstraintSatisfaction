__author__ = 'Coruzzi Nicolas'
__Filename__ = 'AC.py'
__Creationdate__ = '04/11/18'

#######################ALGORYTHME AC#####################
from genererJeuDeDonnees import*

def WithoutSupport_AC(i,j,b, jeuDD):
    #i et j sont des entiers, b est une valeur. Renvoie un booleen
    #Si b dans Dj possède un support dans Di, la fonction renvoie False
    #Sinon elle renvoie True
        
    relation_ij = jeuDD[i,j]
    domaine_i = (relation_ij.shape)[0]
    a=domaine_i[0]
    while a<domaine_i[-1] and jeuDD[i,j,a,b]==0:
        a=domaine_i[domaine_i.index(a)+1]
    return not(jeuDD[i,j,a,b])

def initialisation_AC(jeuDD):
    n= jeuDD.shape[0]
    List_AC=[]
    Status_AC=[False]*n
    
   
    for i in range(n): 
        for j in range(n): 
            relation_ij = jeuDD[i,j]
            if np.array_equal(jeuDD[i,j],np.zeros((relation_ij.shape)[0]),(relation_ij.shape)[1]))):
            
                Dj = (relation_ij.shape)[1]
                for b in Dj: 
                    if WithoutSupport_AC(i,j,b, jeuDD):
                        Dj=Dj.remove(b)
                        if not(Status_AC[j]):
                            List_AC+=[j]
                            Status_AC[j]=True
    return(list_AC, Status_AC)

def propager_AC(i,List_AC,Status_AC,jeuDD):
    n= jeuDD.shape[0]
 

    for j in range(n): 
            relation_ij = jeuDD[i,j]
            if np.array_equal(jeuDD[i,j],np.zeros((relation_ij.shape)[0]),(relation_ij.shape)[1]))):
            
                for b in Dj: 
                    if WithoutSupport_AC(i,j,b, jeuDD):
                        Dj = Dj.remove(b)
                        if not (Status_AC[j]):
                            List_AC += [j]
                            Status_AC[j] = True
    return(list_AC, Status_AC)

def algo_AC8(jeuDD):
    init = initialisation_AC(jeuDD)
    list_AC = init[0]
    status_AC = init[1]          
    while List_AC!=[]:
        for i in List_AC:
            List_AC=List_AC.remove(i)
            Status_AC[i]=False
            propager_AC(i,List_AC,Status_AC, jeuDD)


