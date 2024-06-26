from ase.io import read
from nequip.ase import NequIPCalculator
import numpy as np
import matplotlib.pyplot as plt

Strs=read('SelectedStrs.extxyz',index=':')
lenStrs=len(Strs)
compassLog=open('compassLog.log','w')
formater=1+int(np.log10(lenStrs))
calculator =  NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device = "cuda",
        species_to_type_name = {
            "Au": "Au",
        }
    )
enersList=[]
colorsList=[]
index=[]
counter=-1
for i in range(lenStrs-1):
    try:
        ALStr=Strs[i]
        formatB='out_%'+'0'+str(formater)+'d_BB.extxyz'
        BBStr=read(formatB%i,format='extxyz')
        CRStr=Strs[i+1]
        ALStr.calc=calculator
        BBStr.calc=calculator
        CRStr.calc=calculator
        bt=BBStr.info['barriertype']
        EAL=ALStr.get_potential_energy()
        EBB=BBStr.get_potential_energy()
        ECR=CRStr.get_potential_energy()
        print(EAL,EBB,ECR)
        enersList.append(EAL)
        colorsList.append('k')
        counter += 1
        index.append(counter)
        enersList.append(EBB)
        counter += 1
        index.append(counter)
        if bt=='s':
            colorsList.append('g')
        elif bt=='u':
            colorsList.append('b')
        elif bt=='f':
            colorsList.append('r')
        else:
            raise ValueError("Barrier type not defined")
    except:
        print('Not Converged Run')
        quit()

enersList.append(ECR)
counter += 1
index.append(counter)
colorsList.append('k')

for i in range(len(enersList)-1):
    plt.plot([index[i],index[i+1]],[enersList[i],enersList[i+1]],'-k')

print(enersList)
print(colorsList)
for i in range(len(enersList)):
    plt.scatter(index[i],enersList[i],color=colorsList[i])
plt.xlabel('Index')
plt.ylabel('Energy')
plt.title('Energy Plot with Colors')
plt.savefig('energy_plot_with_colors.png',dpi=1000) 
