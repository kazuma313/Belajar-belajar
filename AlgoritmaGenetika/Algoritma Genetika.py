import numpy as np
import random as rd
import copy



target = 'Kur'
lajuMutasi =0.05
besarPopulasi = 5


def genetik(panjangGen):
    randomChr = ""
    for x in range(0, panjangGen):
        randomChr += chr(rd.randint(32, 126))
    return randomChr


def perhitunganfitness(gen, target):
    fitness = 0
    for x in range(len(target)):
        if gen[x]==target[x]:
            fitness += 1
    fitness = (fitness/len(target))*100
    return fitness

# genBaru = genetik(len(target))
# fitness = perhitunganfitness(genBaru, target)


def buatPopulasi(target,besarPopulasi):
    populasi = []
    for x in range(besarPopulasi):
        gen = genetik(len(target))
        # populasi.append([fitness(target), "".join(randomChrList)])
        populasi.append([perhitunganfitness(gen,target), gen])
    return populasi




def seleksi(populasi):
    populasiSel = copy.deepcopy(populasi)
    nilaiFitnes = np.zeros(besarPopulasi).tolist()
    for x in range(besarPopulasi):
        nilaiFitnes[x] = populasiSel[x][0]
        

    index1 = nilaiFitnes.index(max(nilaiFitnes))
    parent1 = populasiSel[index1]

    del nilaiFitnes[index1]
    del populasiSel[index1]


    index2 = nilaiFitnes.index(max(nilaiFitnes))
    parent2 = populasiSel[index2]
    

    del nilaiFitnes[index2]     
    del populasiSel[index2]

    best1 = parent1
    best2 = parent2

    return best1, best2


def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    crossP =round(len(parent1[1])/2)

    child1[1] = child1[1].replace(child1[1][:crossP], parent2[1][:crossP])
    child2[1] = child2[1].replace(child2[1][:crossP], parent1[1][:crossP])

    return child1, child2

def mutasi(child, lajuMutasi):
    mutasi = copy.deepcopy(child)
    for x in range(len(mutasi[1])):
        if rd.random() <= lajuMutasi: 
            # print(mutasi[1][x])
            # mutasi[1][x] = chr(rd.randint(32, 126))
            mutasi[1] = mutasi[1].replace(mutasi[1][x], chr(rd.randint(32,126)))
    # mutasi[0] = fitness(mutasi[1], target)
    # print()
    return mutasi   






def regenerasi(children, populasi):
  
    nilaiFitnes = np.zeros(len(populasi)).tolist()
    for x in range(len(populasi)):
        nilaiFitnes[x] =populasi[x][0]
            
    for x in range(len(children)):
        index1 = nilaiFitnes.index(min(nilaiFitnes))
        del nilaiFitnes[index1]
        del populasi[index1]

    for x in range(len(children)):
        populasi.append(children[x])
    
    return populasi


def stop(populasi):
    bestSolution1, bestSolution2= seleksi(populasi)
    if bestSolution1[0] == 100:
        looping = False
    else:
        looping = True
    return looping, bestSolution1, bestSolution2

def panggil(popul, target, solusi1, solusi2 ,generasi):
    print('\x1bc')
    print("Target : ",target)
    print("Solusi1: ", solusi1)
    print("Solusi2 : ", solusi2)
    print("Generasi : ",generasi)

    for x in range(len(populasi)):
        print("gen {angka} : {generasi} || fitness : {fitness}".format(angka = x, generasi= popul[x][1], fitness = popul[x][0]))
    

    


populasi = buatPopulasi(target, besarPopulasi)
    

looping = True;
generasiKe = 0
while looping:
    
    parent1, parent2 = seleksi(populasi)
    child1, child2 = crossover(parent1, parent2)
    mutant1 = mutasi(child1, lajuMutasi)
    mutant2 = mutasi(child2, lajuMutasi)

    mutant1[0] = perhitunganfitness(mutant1[1], target)
    mutant2[0] = perhitunganfitness(mutant2[1], target)

    children = [mutant1, mutant2]
    newPopulasi = regenerasi(children, populasi)

    looping, hasil1, hasil2=stop(newPopulasi)
    generasiKe += 1
    
    panggil(newPopulasi, target, hasil1,hasil2, generasiKe)

    

