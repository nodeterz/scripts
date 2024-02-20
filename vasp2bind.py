def get_pos_cell(poscarFile):
    positions=[]
    cell=[]
    for iline ,line in enumerate(poscarFile):
        if iline < 2 :
            continue
        elif iline == 2:
            cxx=float(line.split()[0])
            cxy=float(line.split()[1])
            cxz=float(line.split()[2])
            cell.append([cxx,cxy,cxz])
            if(abs(cxy) > 1.E-4 or abs(cxz) > 1.E-4):
                print('Error_X: Non-orthogonal Cell')
        elif iline == 3:
            cyx=float(line.split()[0])
            cyy=float(line.split()[1])
            cyz=float(line.split()[2])
            cell.append([cyx,cyy,cyz])
            if(abs(cyx) > 1.E-4 or abs(cyz) > 1.E-4):
                print('Error_Y: Non-orthogonal Cell')
        elif iline == 4:
            czx=float(line.split()[0])
            czy=float(line.split()[1])
            czz=float(line.split()[2])
            cell.append([czx,czy,czz])
            if(abs(czx) > 1.E-4 or abs(czy) > 1.E-4):
                print('Error_Z: Non-orthogonal Cell')
        elif iline == 5:
            elem=line.split()[0]
        elif iline == 6:
            nat=int(line.split()[0])
        elif iline == 7:
            if line.split()[0] != 'direct':
                print('Error_D: Make sure POSCAR is in direct and reduced format')
                quit()
        elif iline > 7 and iline < 8+nat:
            x=float(line.split()[0])
            y=float(line.split()[1])
            z=float(line.split()[2])
            r = (x**2+y**2+z**2)**0.5
            positions.append([x,y,z,r])
    
    sorted_list = sorted(positions, key=lambda x: x[3])
    sorted_positions = [sublist[:3] for sublist in sorted_list]
    #print(sorted_positions)
    return cell, sorted_positions, elem, nat

def get_kpts(kpointFile):
    nextLine=0
    kpoints=[]
    for iline, line in enumerate(kpointFile):
        if iline == 0 or iline == 2 or iline == 3:
            continue
        elif iline == 1:
            bandNum=int(line.split()[0])
        elif iline == 4+nextLine:
            if line.split()[4][0] != '\\':
                kpoints.append([line.split()[4],float(line.split()[0]),float(line.split()[1]),float(line.split()[2])])
            else:
                kpoints.append([line.split()[4][1:],float(line.split()[0]),float(line.split()[1]),float(line.split()[2])])
            nextLine +=3    
    kpoints.append(kpoints[0])
    #print(kpoints)
    unique_elements_dict = {}
    for sublist in kpoints:
        key = sublist[0]
        if key not in unique_elements_dict:
            unique_elements_dict[key] = sublist
    
    # Get the unique elements as a list of lists
    unique_kpoints = list(unique_elements_dict.values())
    return kpoints,unique_kpoints,bandNum

def write_bind_file(poscarFile,kpointFile,bindFile,zs,ips,zp,ipp,tcs):
    c,p,elem,nat=get_pos_cell(poscarFile)
    k,k_unique,b=get_kpts(kpointFile)
    
    bindFile.write('; System Name\n')
    bindFile.write('carbon\n')
    
    bindFile.write('\n; define the geometry, in crystallographic coordinates\nGeometry crystallographic\n')
    bindFile.write('\n; this is the number of atoms\n%d\n'%(nat+3))
    bindFile.write('\n; the * here indicates that custom parameters are being used.\n')
    for iat in range(nat+3):
        if iat == 0 :
            bindFile.write('%d * %.16f %.16f %.16f\n'%(iat+1,p[iat][0],p[iat][1],p[iat][2]))
        elif iat < nat :
            bindFile.write('%d %s %.16f %.16f %.16f\n'%(iat+1,elem,p[iat][0],p[iat][1],p[iat][2]))
        elif iat == nat :
            bindFile.write('\n%d %s %.16f %.16f %.16f\n'%(iat+1,elem,p[0][0]+1.E0,p[0][1],p[0][2]))
        elif iat == nat+1 :
            bindFile.write('%d %s %.16f %.16f %.16f\n'%(iat+1,elem,p[0][0],p[0][1]+1.E0,p[0][2]))
        elif iat == nat+2 :
            bindFile.write('%d %s %.16f %.16f %.16f\n'%(iat+1,elem,p[0][0],p[0][1],p[0][2]+1.E0))
    
    bindFile.write('\n; define custom parameters for C\nparameters\n\n;Sym Atom_num Val_elec ns zs ips np zp ipp nd zd ipd c1 z2d c2\n')
    bindFile.write('%s 6 4 2 %.16f %.16f 2 %.16f %.16f\n'%(elem, zs, ips, zp, ipp))
    bindFile.write('\n; definition of the lattice\nlattice\n\n; dimensionality\n3\n\n; number of overlaps in each direction\n')
    bindFile.write('%d %d %d\n'%(nat,nat,nat))
    bindFile.write('; definition of a\n%d %d\n'%(1,nat+1))
    bindFile.write('; definition of b\n%d %d\n'%(1,nat+2))
    bindFile.write('; definition of c\n%d %d\n'%(1,nat+3))
    bindFile.write('\nThe Constant\n%.16f\n'%tcs)
    bindFile.write('\nCrystal Spec\n\n; the lengths of the lattice vectors a, b, and c\n')
    bindFile.write('%.16f %.16f %.16f\n'%(c[0][0],c[1][1],c[2][2]))
    bindFile.write('\n; the crystallographic angles alpha, beta, and gamma.\n 90 90 90\n')
    bindFile.write('\nBand\n%d\n%d\n'%(b,len(k)))
    bindFile.write('\n; The k points are specified in terms of the reciprocal lattice\n')
    for kpt in k:
        bindFile.write('%s %.16f %.16f %.16f\n'%(kpt[0],kpt[1],kpt[2],kpt[3]))
    #bindFile.write('\nprint\ndistance matrix\noverlap matrix\nhamiltonian\nwave func transp\ncharge mat transp\nenergy levels\nend_print\n')
    bindFile.write('\naverage properties\n')
    bindFile.write('\nelectrons\n%d\n'%(nat*4))
    bindFile.write('\n; These k points are not reliable for a real average properties\n')
    bindFile.write('k points\n%d\n'%len(k_unique))
    for kpt in k_unique:
        bindFile.write('%s %.16f %.16f %.16f\n'%(kpt[0],kpt[1],kpt[2],kpt[3]))

poscarFile=open('POSCAR','r')
kpointFile=open('KPOINTS','r')
bindFile=open('mpband.bind','w')
write_bind_file(poscarFile,kpointFile,bindFile,-1.0,-2.0,-3.0,-4.0,1.75)
poscarFile.close()
kpointFile.close()
bindFile.close()
