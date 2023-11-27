from matplotlib.markers import MarkerStyle
from matplotlib import pyplot as plt
def getVals(filename,ucenter,dcenter):
    inpFile=open(filename,'r')
    eigUp=[]
    eigDn=[]
    occUpArr=[]
    occDnArr=[]
    CUp=[]
    iUp=[]
    CDn=[]
    iDn=[]
    for line in inpFile:
        occUp=float(line.split()[1])*float(line.split()[2])
        occDn=-1.0*float(line.split()[4])*float(line.split()[5])
        eigUp.append(float(line.split()[0])) 
        occUpArr.append(occUp)
        eigDn.append(float(line.split()[3])) 
        occDnArr.append(occDn)
        CUp.append([occUp*1.0,0,0,(occUp)])
        iUp.append([ucenter])
        CDn.append([0,0,occDn*1.0,(occDn)])
        iDn.append([dcenter])
    return eigUp,occUpArr,CUp,iUp,eigDn,occDnArr,CDn,iDn

fermiN0CCFile=open('./cage-chain-N0/fermiEner','r')
for line in fermiN0CCFile:
    fermiN0CCLevel=float(line.split()[-1])
fermiN0CCFile.close()
fermiP1CCFile=open('./cage-chain-P1/fermiEner','r')
for line in fermiP1CCFile:
    fermiP1CCLevel=float(line.split()[-1])
fermiP1CCFile.close()
fermiN0CAFile=open('./cage/fermiEner','r')
for line in fermiN0CAFile:
    fermiN0CALevel=float(line.split()[-1])
fermiN0CAFile.close()
fermiN0CHFile=open('./chain/fermiEner','r')
for line in fermiN0CHFile:
    fermiN0CHLevel=float(line.split()[-1])
fermiN0CHFile.close()
eigUpN0CC,occUpN0CC,CUpN0CC,iUpN0CC,eigDnN0CC,occDnN0CC,CDnN0CC,iDnN0CC=getVals('./cage-chain-N0/eigs.dat',0.05,-0.05)
eigUpP1CC,occUpP1CC,CUpP1CC,iUpP1CC,eigDnP1CC,occDnP1CC,CDnP1CC,iDnP1CC=getVals('./cage-chain-P1/eigs.dat',0.5,0.4)
eigUpN0CA,occUpN0CA,CUpN0CA,iUpN0CA,eigDnN0CA,occDnN0CA,CDnN0CA,iDnN0CA=getVals('./cage/eigs.dat',-0.5,-0.6)
eigUpN0CH,occUpN0CH,CUpN0CH,iUpN0CH,eigDnN0CH,occDnN0CH,CDnN0CH,iDnN0CH=getVals('./chain/eigs.dat',-0.9,-1.0)


fig, ax = plt.subplots()
ax.scatter(iUpN0CC,eigUpN0CC,c=CUpN0CC,edgecolor="black", s=60.0, marker=MarkerStyle("^", fillstyle="top"))
ax.scatter(iDnN0CC,eigDnN0CC,c=CDnN0CC,edgecolor="black", s=60.0, marker=MarkerStyle("v", fillstyle="bottom"))
ax.scatter(iUpP1CC,eigUpP1CC,c=CUpP1CC,edgecolor="black", s=60.0, marker=MarkerStyle("^", fillstyle="top"))
ax.scatter(iDnP1CC,eigDnP1CC,c=CDnP1CC,edgecolor="black", s=60.0, marker=MarkerStyle("v", fillstyle="bottom"))
ax.scatter(iUpN0CA,eigUpN0CA,c=CUpN0CA,edgecolor="black", s=60.0, marker=MarkerStyle("^", fillstyle="top"))
ax.scatter(iDnN0CA,eigDnN0CA,c=CDnN0CA,edgecolor="black", s=60.0, marker=MarkerStyle("v", fillstyle="bottom"))
ax.scatter(iUpN0CH,eigUpN0CH,c=CUpN0CH,edgecolor="black", s=60.0, marker=MarkerStyle("^", fillstyle="top"))
ax.scatter(iDnN0CH,eigDnN0CH,c=CDnN0CH,edgecolor="black", s=60.0, marker=MarkerStyle("v", fillstyle="bottom"))
ax.axhline(y=fermiN0CCLevel,color='r',linestyle='-',label='N0CC')
ax.axhline(y=fermiP1CCLevel,color='g',linestyle=':',label='P1CC')
ax.axhline(y=fermiN0CALevel,color='b',linestyle='--',label='N0CA')
ax.axhline(y=fermiN0CHLevel,color='k',linestyle='--',label='N0CH')
ax.legend()
#plt.ylim(fermiLevel-0.5,fermiLevel+0.2)
plt.xlim(-2,2)

plt.show()
