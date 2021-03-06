#ACCESS TO THE RESULTS
#Importing Section
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:57:07 2018

@author: a.iacono
"""
import sqlitedict 
import numpy as np
import matplotlib.pyplot as plt
#Preprocessing Section
#Setting the name of the file that contain the database
name='opti_g_50'
#Creating a dictonary from the database
#The print line just show us the number of the iterations and the respective keys for each iteration.
db = sqlitedict.SqliteDict( name, 'iterations' )
print( list( db.keys() ) )

#Defining the number of the iteration and the x-axis for the graph
n=len(db)
x=np.arange(0,n)
#Creating the empy vector to save all the value for each iteration of the variables of interest
cd=np.array([])
g=np.array([])
m=np.array([])
vm=np.array([])
cl=np.array([])
a=np.array([])
vms=np.array([])
t1=np.array([])
t2=np.array([])
t3=np.array([])
t4=np.array([])
t5=np.array([])
t6=np.array([])
t7=np.array([])
t8=np.array([])
t9=np.array([])
t10=np.array([])
t11=np.array([])
t12=np.array([])
#Extrapoling the dictonary of the first iteration to have access to some value like the yield stress
data = db['rank0:COBYLA|0|root|1']
c = data['Unknowns']
#Determinating the value of the lift and stress constraint
con_l=(c['W']/(0.5*c['rho_a']*c['V']**2*c['Sw']))*np.ones(n)
con_s=c['sigma_y']*np.ones(n)
#Accessing to the value for each iteration
#As first we obtain a database for each iteration, the print command it's just to have a feedback on the runtime.

#From the Data dictonary we can collect all the data in refernce at the variables of interest, and append it to the vector created in the settings section.
for j in range(0,n):
         data = db['rank0:COBYLA|'+str(j)+'|root|'+str(j+1)]
         print('rank0:COBYLA|'+str(j)+'|root|'+str(j+1))
#         u = data['Parameters']
         c = data['Unknowns']
         g = np.append(g,c['G'])
         cd =np.append(cd, c['CDi'])
         a = np.append(a,c['alpha'])
         m = np.append(m,c['mass'])
         vms = max(c['VMStress'])
         vm = np.append(vm,vms)
         cl = np.append(cl, c['CL'])
         t = c['t']
         t1 = np.append(t1,t[0])
         t2 = np.append(t2,t[1])
         t3 = np.append(t3,t[2])
         t4 = np.append(t4,t[3])
         t5 = np.append(t5,t[4])
         t6 = np.append(t6,t[5])
         t7 = np.append(t7,t[6])
         t8 = np.append(t8,t[7])
         t9 = np.append(t9,t[8])
         t10 = np.append(t10,t[9])
         t11 = np.append(t11,t[10])
         t12 = np.append(t12,t[11])
#Print Results
#Here we are printing all the graph of the variation of the variables for each iteration.
#The script is also set to save the plot as jpg files in the code folder.
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[1].grid (True)
axes[1].set_xlabel('iteration', fontsize=14)
axes[1].plot(x,vm)
axes[1].plot(x,con_s)
axes[1].set_title("VonMises")
axes[2].set_xlabel('iteration', fontsize=14)
axes[2].grid (True)
axes[2].plot(x,g)
axes[2].plot(x,con_s)
axes[2].set_title("G")
axes[0].plot(x,a)
axes[0].set_title("alpha")
axes[0].grid (True)
axes[0].set_xlabel('iteration', fontsize=14)
#axes[2].plot(x,32vms)
#axes[2].set_title("VonMises Stresses")
plt.savefig(name+'_1',dpi=1000, bbox_inches='tight')
plt.show()
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[1].grid (True)
axes[1].set_xlabel('iteration', fontsize=14)
axes[1].plot(x,cd)
axes[1].set_title("CDi")
axes[2].set_xlabel('iteration', fontsize=14)
axes[2].grid (True)
axes[2].plot(x,cl)
axes[2].plot(x,con_l)
axes[2].set_title("CL")
axes[0].plot(x,m)
axes[0].set_title("Mass")
axes[0].grid (True)
axes[0].set_xlabel('iteration', fontsize=14)
#axes[2].plot(x,32vms)
#axes[2].set_title("VonMises Stresses")
plt.savefig(name+'_2',dpi=1000, bbox_inches='tight')
plt.show()
plt.plot(x,t1,label='t[1]')
plt.plot(x,t2,label='t[2]')
plt.plot(x,t3,label='t[3]')
plt.plot(x,t4,label='t[4]')
plt.plot(x,t5,label='t[5]')
plt.plot(x,t6,label='t[6]')
plt.plot(x,t7,label='t[7]')
plt.plot(x,t8,label='t[8]')
plt.plot(x,t9,label='t[9]')
plt.plot(x,t10,label='t[10]')
plt.plot(x,t11,label='t[11]')
plt.plot(x,t12,label='t[12]')
plt.grid(True)
plt.xlabel('iteration', fontsize=14)
plt.ylabel('thickness', fontsize=14)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.savefig(name+'_3',dpi=1000, bbox_inches='tight')
