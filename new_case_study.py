#!/usr/bin/env python
# coding: utf-8

# In[239]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium


# In[240]:


df = pd.read_table(r'Gorgonichthys_1_suite3_supercombo_log_sb.las',delim_whitespace = True)
df.columns


# In[241]:


df1 = df.replace(-999.0000,np.nan)


# In[242]:




fig, axes = plt.subplots(figsize =(16,25))

# first we are setting the axes

ax1 = plt.subplot2grid((1,6),(0,0), rowspan =1, colspan = 1)
ax2 = plt.subplot2grid((1,6),(0,1), rowspan =1, colspan = 1)
ax3 = plt.subplot2grid((1,6),(0,2), rowspan =1, colspan = 1)
ax4 = plt.subplot2grid((1,6),(0,3), rowspan =1, colspan = 1)
ax10= plt.subplot2grid((1,6),(0,4), rowspan =1, colspan = 1)

ax5= ax1.twiny()
ax6=ax2.twiny()
ax7=ax2.twiny()

ax8= ax3.twiny()
ax9= ax3.twiny()


# Set up indivisual log tracks / subplots :
# ax1
ax10.plot("CALI","DEPTH",data = df1, color= 'red')
ax10.set_xlim(6,16) # unit is in inch
ax10.xaxis.set_label_position('top')
ax10.spines['top'].set_position(('outward',0))
ax10.tick_params(axis='x', colors='red')
ax10.set_xlabel("CALI (inch)", color='red')
ax10.grid()
ax10.set_ylim(4775,3909)



# ax5
ax5.plot("GR","DEPTH",data= df1, color= 'g')
ax5.set_xlim(0,200)  # unit is in API

left_value = 0
right_value = 200
span = abs(right_value - left_value)
cmap= plt.get_cmap()
color_index = np.arange(left_value,right_value, span/10)
for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    ax5.fill_betweenx(df1["DEPTH"], left_value, df1["GR"], where= df1["GR"]>=index, color = color)
    

ax5.spines['top'].set_position(('outward',40))
ax5.tick_params(axis='x', colors='g')
ax5.set_xlabel("GR (API)", color='g')
ax5.xaxis.tick_top()
ax5.xaxis.set_label_position('top')
ax5.grid()
ax5.set_ylim(4775,3909)



# ax2
ax2.plot("AT10", "DEPTH", data= df1, color= 'blue')
ax2.spines['top'].set_position(('outward',0))
ax2.tick_params(axis='x', colors='blue')
ax2.set_xlabel("RShallow (ohm.m)", color='blue')
ax2.xaxis.tick_top()
ax2.semilogx()
ax2.xaxis.set_label_position('top')
ax2.grid()
ax2.set_ylim(4775,3909)

# ax6
ax6.plot("AT30", "DEPTH", data= df1, color= 'r')
ax6.spines['top'].set_position(('outward',40))
ax6.tick_params(axis='x', colors='r')
ax6.set_xlabel("RMed (ohm.m)", color='r')
ax6.xaxis.tick_top()
ax6.semilogx()
ax6.xaxis.set_label_position('top')
ax6.grid()
ax6.set_ylim(4775,3909)


# ax7
ax7.plot("AT90", "DEPTH", data= df1, color= 'black')
ax7.spines['top'].set_position(('outward',80))
ax7.tick_params(axis='x', colors='black')
ax7.set_xlabel("RDep (ohm.m)", color='black')
ax7.xaxis.tick_top()
ax7.semilogx()
ax7.xaxis.set_label_position('top')
ax7.grid()
ax7.set_ylim(4775,3909)


# ax3
ax3.plot("RHOB", "DEPTH", data= df1, color= 'b')
ax3.set_xlim(3,1.65)
ax3.set_ylim(4775,3909)
ax3.spines['top'].set_position(('outward',0))
ax3.tick_params(axis='x', colors='b')
ax3.set_xlabel("RHOB (gm/cc)", color='b')
ax3.xaxis.tick_top()




# ax8
ax8.plot("TNPH", "DEPTH", data= df1, color= 'red')
ax8.set_xlim(0,0.60)
ax8.spines['top'].set_position(('outward',40))
ax8.tick_params(axis='x', colors='red')
ax8.set_xlabel("NPHI", color='red')
ax8.xaxis.tick_top()
ax8.set_ylim(4775,3909)


# ax5
ax4.plot("DTCO", "DEPTH", data= df1, color= 'm')
ax4.set_xlim(140,40)
ax4.spines['top'].set_position(('outward',0))
ax4.tick_params(axis='x', colors='m')
ax4.set_xlabel("DTC (microfeet/sec)", color='m')
ax4.xaxis.tick_top()
ax4.xaxis.set_label_position('top')
ax4.grid()
ax4.set_ylim(4775,3909)





# Hide the tick labels on y axis 
for ax in [ax2,ax3,ax4, ax5, ax10]:
    plt.setp(ax.get_yticklabels(), visible= False)
    
# Reduce the space between each subplot :
fig.subplots_adjust(wspace=0.1)

fig.suptitle(" GORGONICHTHYS-1 ", fontsize=20)


plt.show()


# In[ ]:





# In[243]:


# We are making histogram Plots :

# Well 1 :
 
df1['GR'].plot(kind = 'hist',bins = 80, density = True, edgecolor = 'black')
df1['GR'].plot(kind='kde', color = 'black')
plt.xlabel("GR ( API)", fontsize=15)
plt.ylabel("Depth (m)", fontsize=15)
plt.xlim(0,200)
plt.title(" Well Gorgonichthys_1_PLAY_003 ")
mean= df1['GR'].mean()
p05 = df1['GR'].quantile(0.05)
p95 = df1['GR'].quantile(0.95)
print("Mean :", mean)
print("p05 :", p05)
print("p95: ", p95)
plt.axvline(mean, color='green', label ='mean')
plt.axvline(p05, color='red', label ='p05')
plt.axvline(p95, color='yellow', label ='p95')
plt.legend()


# volume of shale
# 

# In[269]:


# It is observed from the histogram plot of the GR log
GRmin = 15.3999
GRmax = 170.7985
Vshale_1 = (df1['GR']- GRmin ) / ( GRmax - GRmin )
Vshale_1


# # different lithology different density 

# In[270]:


#for sandstone we take the matrix density

for i in Vshale_1 :
        if i >= 0.6 :
                rho_ma = 2.65              # Condition to calculate rho_ma 
        else :
                rho_ma = 2.55
        

        rho_f = 1.05                          # unit gm/cc
        
        # Now we are trying to calculate the density porosity through the density log :
        
        phi_d = ( rho_ma - df1['RHOB'] ) / ( rho_ma - rho_f )
        
        
        # Calculation of total porosity :
        
        phi_t = (phi_d + df1['TNPH'])/2 #condition for diffrent phi to calculate total porosity
        
        
        # Calculation of Water Saturation : archies formula
        
        Rw = 0.0015
        Sw = (1 * Rw / ((phi_t**2) * df1['RT'] ))**(0.5)  # I am taking m as 2, n=2 and a=1
        
        #Calculation of water saturation using : simundoux formula
        
        
        
        Rsh=0.7
        Sw_simundoux = ((1 * Rw) / (2 * phi_t*2)) * ( ( ( Vshale_1/Rsh)**2 + (4 * phi_t*2)/(1 * Rw * df1['RT']) ) **0.5   - ( Vshale_1/Rsh)  )
        
        
        


# In[271]:


Sw


# # plotting with effective

# In[272]:


fig, axes = plt.subplots(figsize =(20,25))

# first we are setting the axes

ax1 = plt.subplot2grid((1,8),(0,0), rowspan =1, colspan = 1)
ax2 = plt.subplot2grid((1,8),(0,1), rowspan =1, colspan = 1)
ax3 = plt.subplot2grid((1,8),(0,2), rowspan =1, colspan = 1)
ax4 = plt.subplot2grid((1,8),(0,3), rowspan =1, colspan = 1)
ax10= plt.subplot2grid((1,8),(0,4), rowspan =1, colspan = 1)
ax11= plt.subplot2grid((1,8),(0,5), rowspan =1, colspan = 1)
ax12= plt.subplot2grid((1,8),(0,6), rowspan =1, colspan = 1)

ax5= ax1.twiny()
ax6=ax2.twiny()
ax7=ax2.twiny()

ax8= ax3.twiny()
ax9= ax3.twiny()


# Set up indivisual log tracks / subplots :
# ax1
ax10.plot("CALI","DEPTH",data = df1, color= 'red')
ax10.set_xlim(6,16) # unit is in inch
ax10.xaxis.set_label_position('top')
ax10.spines['top'].set_position(('outward',0))
ax10.tick_params(axis='x', colors='red')
ax10.set_xlabel("CALI (inch)", color='red')
ax10.grid()
ax10.set_ylim(4775,3909)



# ax5
ax5.plot("GR","DEPTH",data= df1, color= 'g')
ax5.set_xlim(0,200)  # unit is in API

left_value = 0
right_value = 200
span = abs(right_value - left_value)
cmap= plt.get_cmap()
color_index = np.arange(left_value,right_value, span/10)
for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    ax5.fill_betweenx(df1["DEPTH"], left_value, df1["GR"], where= df1["GR"]>=index, color = color)
    

ax5.spines['top'].set_position(('outward',40))
ax5.tick_params(axis='x', colors='g')
ax5.set_xlabel("GR (API)", color='g')
ax5.xaxis.tick_top()
ax5.xaxis.set_label_position('top')
ax5.grid()
ax5.set_ylim(4775,3909)



# ax2
ax2.plot("AT10", "DEPTH", data= df1, color= 'blue')
ax2.spines['top'].set_position(('outward',0))
ax2.tick_params(axis='x', colors='blue')
ax2.set_xlabel("RShallow (ohm.m)", color='blue')
ax2.xaxis.tick_top()
ax2.semilogx()
ax2.xaxis.set_label_position('top')
ax2.grid()
ax2.set_ylim(4775,3909)
ax2.set_xlim(0.1,1000)

# ax6
ax6.plot("AT30", "DEPTH", data= df1, color= 'r')
ax6.spines['top'].set_position(('outward',40))
ax6.tick_params(axis='x', colors='r')
ax6.set_xlabel("RMed (ohm.m)", color='r')
ax6.xaxis.tick_top()
ax6.semilogx()
ax6.xaxis.set_label_position('top')
ax6.grid()
ax6.set_ylim(4775,3909)
ax6.set_xlim(0.1,1000)


# ax7
ax7.plot("AT90", "DEPTH", data= df1, color= 'black')
ax7.spines['top'].set_position(('outward',80))
ax7.tick_params(axis='x', colors='black')
ax7.set_xlabel("RDep (ohm.m)", color='black')
ax7.xaxis.tick_top()
ax7.semilogx()
ax7.xaxis.set_label_position('top')
ax7.grid()
ax7.set_ylim(4775,3909)
ax7.set_xlim(0.1,1000)


# ax3
ax3.plot("RHOB", "DEPTH", data= df1, color= 'b')
ax3.set_xlim(3,1.65)
ax3.set_ylim(4775,3909)
ax3.spines['top'].set_position(('outward',0))
ax3.tick_params(axis='x', colors='b')
ax3.set_xlabel("RHOB (gm/cc)", color='b')
ax3.xaxis.tick_top()




# ax8
ax8.plot("TNPH", "DEPTH", data= df1, color= 'red')
ax8.set_xlim(0,0.60)
ax8.spines['top'].set_position(('outward',40))
ax8.tick_params(axis='x', colors='red')
ax8.set_xlabel("NPHI", color='red')
ax8.xaxis.tick_top()
ax8.set_ylim(4775,3909)


# ax4
ax4.plot("DTCO", "DEPTH", data= df1, color= 'm')
ax4.set_xlim(140,40)
ax4.spines['top'].set_position(('outward',0))
ax4.tick_params(axis='x', colors='m')
ax4.set_xlabel("DTC (microfeet/sec)", color='m')
ax4.xaxis.tick_top()
ax4.xaxis.set_label_position('top')
ax4.grid()
ax4.set_ylim(4775,3909)



# ax11

ax11.plot(phi_t, "DEPTH", data=df1, color= 'm')
ax11.set_xlim(-0.2,0.60)
ax11.spines['top'].set_position(('outward',0))
ax11.tick_params(axis='x', colors='m')
ax11.set_xlabel("Porosity(Total)", color='m')
ax11.xaxis.tick_top()
ax11.xaxis.set_label_position('top')
ax11.grid()
ax11.set_ylim(4775,3909)


# ax12

ax12.plot(Vshale_1, "DEPTH", data=df1, color= 'k')
#ax12.set_xlim(0,1)
ax12.spines['top'].set_position(('outward',0))
ax12.tick_params(axis='x', colors='k')
ax12.set_xlabel("V_Shale", color='k')
ax12.xaxis.tick_top()
ax12.xaxis.set_label_position('top')
ax12.grid()
ax12.set_ylim(4775,3909)




# Hide the tick labels on y axis 
for ax in [ax2,ax3,ax4, ax5, ax10, ax11, ax12]:
    plt.setp(ax.get_yticklabels(), visible= False)
    
# Reduce the space between each subplot :
fig.subplots_adjust(wspace=0.2)

fig.suptitle(" GORGONICHTHYS-1 ", fontsize=20)


plt.show()


# In[ ]:





# # plot for water saturation

# In[273]:




fig, axes = plt.subplots(figsize =(20,25))

# first we are setting the axes

ax1 = plt.subplot2grid((1,9),(0,0), rowspan =1, colspan = 1)
ax2 = plt.subplot2grid((1,9),(0,1), rowspan =1, colspan = 1)
ax3 = plt.subplot2grid((1,9),(0,2), rowspan =1, colspan = 1)
ax4 = plt.subplot2grid((1,9),(0,3), rowspan =1, colspan = 1)
ax10= plt.subplot2grid((1,9),(0,4), rowspan =1, colspan = 1)
ax11= plt.subplot2grid((1,9),(0,5), rowspan =1, colspan = 1)
ax12= plt.subplot2grid((1,9),(0,6), rowspan =1, colspan = 1)
ax13= plt.subplot2grid((1,9),(0,7),rowspan =1, colspan = 1)




ax5= ax1.twiny()
ax6=ax2.twiny()
ax7=ax2.twiny()

ax8= ax3.twiny()
ax9= ax3.twiny()


ax14 = ax13.twiny()



# Set up indivisual log tracks / subplots :
# ax1
ax10.plot("CALI","DEPTH",data = df1, color= 'red')
ax10.set_xlim(6,16) # unit is in inch
ax10.xaxis.set_label_position('top')
ax10.spines['top'].set_position(('outward',0))
ax10.tick_params(axis='x', colors='red')
ax10.set_xlabel("CALI (inch)", color='red')
ax10.grid()
ax10.set_ylim(4775,3909)



# ax5
ax5.plot("GR","DEPTH",data= df1, color= 'g')
ax5.set_xlim(0,200)  # unit is in API

left_value = 0
right_value = 200
span = abs(right_value - left_value)
cmap= plt.get_cmap()
color_index = np.arange(left_value,right_value, span/10)
for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    ax5.fill_betweenx(df1["DEPTH"], left_value, df1["GR"], where= df1["GR"]>=index, color = color)
    

ax5.spines['top'].set_position(('outward',40))
ax5.tick_params(axis='x', colors='g')
ax5.set_xlabel("GR (API)", color='g')
ax5.xaxis.tick_top()
ax5.xaxis.set_label_position('top')
ax5.grid()
ax5.set_ylim(4775,3909)



# ax2
ax2.plot("AT10", "DEPTH", data= df1, color= 'blue')
ax2.spines['top'].set_position(('outward',0))
ax2.tick_params(axis='x', colors='blue')
ax2.set_xlabel("RShallow (ohm.m)", color='blue')
ax2.xaxis.tick_top()
ax2.semilogx()
ax2.xaxis.set_label_position('top')
ax2.grid()
ax2.set_ylim(4775,3909)
ax2.set_xlim(0.1,1000)

# ax6
ax6.plot("AT30", "DEPTH", data= df1, color= 'r')
ax6.spines['top'].set_position(('outward',40))
ax6.tick_params(axis='x', colors='r')
ax6.set_xlabel("RMed (ohm.m)", color='r')
ax6.xaxis.tick_top()
ax6.semilogx()
ax6.xaxis.set_label_position('top')
ax6.grid()
ax6.set_ylim(4775,3909)
ax6.set_xlim(0.1,1000)


# ax7
ax7.plot("AT90", "DEPTH", data= df1, color= 'black')
ax7.spines['top'].set_position(('outward',80))
ax7.tick_params(axis='x', colors='black')
ax7.set_xlabel("RDep (ohm.m)", color='black')
ax7.xaxis.tick_top()
ax7.semilogx()
ax7.xaxis.set_label_position('top')
ax7.grid()
ax7.set_ylim(4775,3909)
ax7.set_xlim(0.1,1000)


# ax3
ax3.plot("RHOB", "DEPTH", data= df1, color= 'b')
ax3.set_xlim(3,1.65)
ax3.set_ylim(4775,3909)
ax3.spines['top'].set_position(('outward',0))
ax3.tick_params(axis='x', colors='b')
ax3.set_xlabel("RHOB (gm/cc)", color='b')
ax3.xaxis.tick_top()




# ax8
ax8.plot("TNPH", "DEPTH", data= df1, color= 'red')
ax8.set_xlim(0,0.60)
ax8.spines['top'].set_position(('outward',40))
ax8.tick_params(axis='x', colors='red')
ax8.set_xlabel("NPHI", color='red')
ax8.xaxis.tick_top()
ax8.set_ylim(4775,3909)


# ax4
ax4.plot("DTCO", "DEPTH", data= df1, color= 'm')
ax4.set_xlim(140,40)
ax4.spines['top'].set_position(('outward',0))
ax4.tick_params(axis='x', colors='m')
ax4.set_xlabel("DTC (microfeet/sec)", color='m')
ax4.xaxis.tick_top()
ax4.xaxis.set_label_position('top')
ax4.grid()
ax4.set_ylim(4775,3909)



# ax11

ax11.plot(phi_t, "DEPTH", data=df1, color= 'm')
ax11.set_xlim(-0.2,0.60)
ax11.spines['top'].set_position(('outward',0))
ax11.tick_params(axis='x', colors='m')
ax11.set_xlabel("Porosity(Total)", color='m')
ax11.xaxis.tick_top()
ax11.xaxis.set_label_position('top')
ax11.grid()
ax11.set_ylim(4775,3909)


# ax12

ax12.plot(Vshale_1, "DEPTH", data=df1, color= 'k')
#ax12.set_xlim(0,1)
ax12.spines['top'].set_position(('outward',0))
ax12.tick_params(axis='x', colors='k')
ax12.set_xlabel("V_Shale", color='k')
ax12.xaxis.tick_top()
ax12.xaxis.set_label_position('top')
ax12.grid()
ax12.set_ylim(4775,3909)


#ax13
ax13.plot(Sw, "DEPTH", data=df1, color= 'cyan')
ax13.set_xlim(-0.1,1)
ax13.spines['top'].set_position(('outward',0))
ax13.tick_params(axis='x', colors='cyan')
ax13.set_xlabel("Archie eqn", color='cyan')
ax13.xaxis.tick_top()
ax13.xaxis.set_label_position('top')
ax13.grid()
ax13.set_ylim(4775,3909)



#ax14
ax14.plot(Sw_simundoux, "DEPTH", data=df1, color= 'red')
ax14.set_xlim(-0.1,1)
ax14.spines['bottom'].set_position(('outward',0))
ax14.tick_params(axis='x', colors='red')
ax14.set_xlabel("Simundoux eqn", color='red')
ax14.xaxis.tick_top()
ax14.xaxis.set_label_position('bottom')
ax14.grid()
ax14.set_ylim(4775,3909)


# Hide the tick labels on y axis 
for ax in [ax2,ax3,ax4, ax5, ax10, ax11, ax12,ax13]:
    plt.setp(ax.get_yticklabels(), visible= False)
    
# Reduce the space between each subplot :
fig.subplots_adjust(wspace=0.2)

fig.suptitle(" GORGONICHTHYS-1 ", fontsize=20)


plt.show()


# In[ ]:





# In[274]:


core_data = pd.read_excel(r"C:\Users\sourav bera\Downloads\Grid Export.xlsx")


# In[275]:


core_data.columns


# In[276]:


depth_core = core_data['Top depth (m)']
poro_core = (core_data['Porosity (%)']*.01)

core_per = core_data['Permeability (mD)']


# In[277]:




fig, axes = plt.subplots(figsize =(20,25))

# first we are setting the axes

ax1 = plt.subplot2grid((1,9),(0,0), rowspan =1, colspan = 1)
ax2 = plt.subplot2grid((1,9),(0,1), rowspan =1, colspan = 1)
ax3 = plt.subplot2grid((1,9),(0,2), rowspan =1, colspan = 1)
ax4 = plt.subplot2grid((1,9),(0,3), rowspan =1, colspan = 1)
ax10= plt.subplot2grid((1,9),(0,4), rowspan =1, colspan = 1)
ax11= plt.subplot2grid((1,9),(0,5), rowspan =1, colspan = 1)
ax12= plt.subplot2grid((1,9),(0,6), rowspan =1, colspan = 1)
ax13= plt.subplot2grid((1,9),(0,7),rowspan =1, colspan = 1)




ax5= ax1.twiny()
ax6=ax2.twiny()
ax7=ax2.twiny()

ax8= ax3.twiny()
ax9= ax3.twiny()


ax14 = ax13.twiny()

ax15 = ax11.twiny()

# Set up indivisual log tracks / subplots :
# ax1
ax10.plot("CALI","DEPTH",data = df1, color= 'red')
ax10.set_xlim(6,16) # unit is in inch
ax10.xaxis.set_label_position('top')
ax10.spines['top'].set_position(('outward',0))
ax10.tick_params(axis='x', colors='red')
ax10.set_xlabel("CALI (inch)", color='red')
ax10.grid()
ax10.set_ylim(4775,3909)



# ax5
ax5.plot("GR","DEPTH",data= df1, color= 'g')
ax5.set_xlim(0,200)  # unit is in API

left_value = 0
right_value = 200
span = abs(right_value - left_value)
cmap= plt.get_cmap()
color_index = np.arange(left_value,right_value, span/10)
for index in sorted(color_index):
    index_value = (index-left_value)/span
    color = cmap(index_value)
    ax5.fill_betweenx(df1["DEPTH"], left_value, df1["GR"], where= df1["GR"]>=index, color = color)
    

ax5.spines['top'].set_position(('outward',40))
ax5.tick_params(axis='x', colors='g')
ax5.set_xlabel("GR (API)", color='g')
ax5.xaxis.tick_top()
ax5.xaxis.set_label_position('top')
ax5.grid()
ax5.set_ylim(4775,3909)



# ax2
ax2.plot("AT10", "DEPTH", data= df1, color= 'blue')
ax2.spines['top'].set_position(('outward',0))
ax2.tick_params(axis='x', colors='blue')
ax2.set_xlabel("RShallow (ohm.m)", color='blue')
ax2.xaxis.tick_top()
ax2.semilogx()
ax2.xaxis.set_label_position('top')
ax2.grid()
ax2.set_ylim(4775,3909)
ax2.set_xlim(0.1,1000)

# ax6
ax6.plot("AT30", "DEPTH", data= df1, color= 'r')
ax6.spines['top'].set_position(('outward',40))
ax6.tick_params(axis='x', colors='r')
ax6.set_xlabel("RMed (ohm.m)", color='r')
ax6.xaxis.tick_top()
ax6.semilogx()
ax6.xaxis.set_label_position('top')
ax6.grid()
ax6.set_ylim(4775,3909)
ax6.set_xlim(0.1,1000)


# ax7
ax7.plot("AT90", "DEPTH", data= df1, color= 'black')
ax7.spines['top'].set_position(('outward',80))
ax7.tick_params(axis='x', colors='black')
ax7.set_xlabel("RDep (ohm.m)", color='black')
ax7.xaxis.tick_top()
ax7.semilogx()
ax7.xaxis.set_label_position('top')
ax7.grid()
ax7.set_ylim(4775,3909)
ax7.set_xlim(0.1,1000)


# ax3
ax3.plot("RHOB", "DEPTH", data= df1, color= 'b')
ax3.set_xlim(3,1.65)
ax3.set_ylim(4775,3909)
ax3.spines['top'].set_position(('outward',0))
ax3.tick_params(axis='x', colors='b')
ax3.set_xlabel("RHOB (gm/cc)", color='b')
ax3.xaxis.tick_top()




# ax8
ax8.plot("TNPH", "DEPTH", data= df1, color= 'red')
ax8.set_xlim(0,0.60)
ax8.spines['top'].set_position(('outward',40))
ax8.tick_params(axis='x', colors='red')
ax8.set_xlabel("NPHI", color='red')
ax8.xaxis.tick_top()
ax8.set_ylim(4775,3909)


# ax4
ax4.plot("DTCO", "DEPTH", data= df1, color= 'm')
ax4.set_xlim(140,40)
ax4.spines['top'].set_position(('outward',0))
ax4.tick_params(axis='x', colors='m')
ax4.set_xlabel("DTC (microfeet/sec)", color='m')
ax4.xaxis.tick_top()
ax4.xaxis.set_label_position('top')
ax4.grid()
ax4.set_ylim(4775,3909)



# ax11

ax11.plot(phi_t, "DEPTH", data=df1, color= 'm')
ax11.set_xlim(-0.2,0.60)
ax11.spines['top'].set_position(('outward',0))
ax11.tick_params(axis='x', colors='m')
ax11.set_xlabel("Porosity(Total)", color='m')
ax11.xaxis.tick_top()
ax11.xaxis.set_label_position('top')
ax11.grid()
ax11.set_ylim(4775,3909)


# ax12

ax12.plot(Vshale_1, "DEPTH", data=df1, color= 'k')
#ax12.set_xlim(0,1)
ax12.spines['top'].set_position(('outward',0))
ax12.tick_params(axis='x', colors='k')
ax12.set_xlabel("V_Shale", color='k')
ax12.xaxis.tick_top()
ax12.xaxis.set_label_position('top')
ax12.grid()
ax12.set_ylim(4775,3909)


#ax13
ax13.plot(Sw, "DEPTH", data=df1, color= 'cyan')
ax13.set_xlim(-0.1,1)
ax13.spines['top'].set_position(('outward',0))
ax13.tick_params(axis='x', colors='cyan')
ax13.set_xlabel("Archie eqn", color='cyan')
ax13.xaxis.tick_top()
ax13.xaxis.set_label_position('top')
ax13.grid()
ax13.set_ylim(4775,3909)



#ax14
ax14.plot(Sw_simundoux, "DEPTH", data=df1, color= 'red')
ax14.set_xlim(-0.1,1)
ax14.spines['bottom'].set_position(('outward',0))
ax14.tick_params(axis='x', colors='red')
ax14.set_xlabel("Simundoux eqn", color='red')
ax14.xaxis.tick_top()
ax14.xaxis.set_label_position('bottom')
ax14.grid()
ax14.set_ylim(4775,3909)


#ax15
ax15.scatter(poro_core,depth_core, color= 'red')
ax15.set_xlim(-0.2,0.60)
ax15.spines['top'].set_position(('outward',0))
ax15.tick_params(axis='x', colors='red')
ax15.set_xlabel("Porosity(Core)", color='red')
ax15.xaxis.tick_top()
ax15.xaxis.set_label_position('top')
ax15.grid()
ax15.set_ylim(4775,3909)


# Hide the tick labels on y axis 
for ax in [ax2,ax3,ax4, ax5, ax10, ax11, ax12,ax13]:
    plt.setp(ax.get_yticklabels(), visible= False)
    
# Reduce the space between each subplot :
fig.subplots_adjust(wspace=0.2)

fig.suptitle(" GORGONICHTHYS-1 ", fontsize=20)


plt.show()


# In[ ]:





# In[278]:


x=poro_core
y=core_per
m,c=np.polyfit(x,y,1)


# In[279]:


m


# In[280]:


c


# # pore with permeability
# 

# In[281]:


perm_data = phi_t*m + c


# In[282]:


perm_data1=perm_data


# In[283]:




fig, axes = plt.subplots(figsize =(20,30))

# first we are setting the axes

ax2 = plt.subplot2grid((1,5),(0,0), rowspan =1, colspan = 1)
ax15=ax2.twiny()

ax2.plot(perm_data1, "DEPTH", data= df1, color= 'c')
ax2.spines['top'].set_position(('outward',0))
ax2.tick_params(axis='x', colors='c')
ax2.set_xlabel("Permeability Log Data", color='c')
ax2.xaxis.tick_top()
ax2.semilogx()
ax2.xaxis.set_label_position('top')
ax2.grid()
ax2.set_ylim(4775,3909)



ax15.scatter(core_per,depth_core, color= 'red')
ax15.set_xlim(-0.2,0.60)
ax15.spines['top'].set_position(('outward',40))
ax15.tick_params(axis='x', colors='red')
ax15.set_xlabel("Permeability (Core)", color='red')
ax15.xaxis.tick_top()
ax15.semilogx()
ax15.xaxis.set_label_position('top')
ax15.grid()
ax15.set_ylim(4775,3909)


# In[ ]:





# # Relationship from excel

# In[284]:


perm_data_excel =  phi_t * 0.000435313 + 0.082258153





# In[286]:





# In[ ]:





# # Effective porosity calculation

# In[288]:


#phi_shale = 0.15
phi_e = phi_t - (Vshale_1 * 0.15)
                 


# In[299]:


fig, axes = plt.subplots(figsize =(3,25))

# first we are setting the axes

ax11 = plt.subplot2grid((1,1),(0,0), rowspan =1, colspan = 1)
ax15 = ax11.twiny()

# ax11

ax11.plot(phi_t, "DEPTH", data=df1, color= 'b')
ax11.set_xlim(0.0,0.60)
ax11.spines['top'].set_position(('outward',0))
ax11.tick_params(axis='x', colors='b')
ax11.set_xlabel("Porosity(Total)", color='b')
ax11.xaxis.tick_top()
ax11.xaxis.set_label_position('top')
ax11.grid()
ax11.set_ylim(4775,3909)

# ax15

ax15.plot(phi_e,"DEPTH", data=df1, color= 'k', ls='--')
ax15.set_xlim(0.0,0.60)
ax15.spines['top'].set_position(('outward',40))
ax15.tick_params(axis='x', colors='k')
ax15.set_xlabel("Porosity(Effective)", color='k')
ax15.xaxis.tick_top()
ax15.xaxis.set_label_position('top')
ax15.grid()
ax15.set_ylim(4775,3909)


fig.suptitle(" Comparison of Core Porosity and log porosity(total)", color='red',fontsize=20)


# In[ ]:




