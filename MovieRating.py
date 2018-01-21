
# coding: utf-8

# In[30]:



import pandas as pd
import os
os.getcwd()


# In[31]:


#Importing the MovieRatings data
movies = pd.read_csv("C:/Users/Deekshith/Documents/DS/data science/R-DS/Movie-Ratings.csv")


# In[32]:


#Total length of the dataset
len(movies)


# In[33]:


movies.head()


# In[34]:


#Renaming the columns
movies.columns = ['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']


# In[35]:


movies.head()


# In[36]:


#Basic structure of data
movies.info()


# In[37]:


#Basic statistics of the data
movies.describe()


# In[38]:


#Converting into category variables
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')


# In[39]:


movies.info()


# In[40]:


#To find out the different categories of movies
movies.Genre.cat.categories


# In[41]:


movies.Genre.cat


# In[42]:


movies.describe()


# In[43]:


#Importing the visualization packages
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
import warnings
warnings.filterwarnings('ignore')


# In[44]:


#JoinPlot
j = sns.jointplot(x='CriticRating',y='AudienceRating',data=movies)


# In[45]:


j = sns.jointplot(data=movies,x='CriticRating',y='AudienceRating',kind='hex')
#Region with black region has more concentration


# In[46]:


#Histograms
m1 = sns.distplot(movies.AudienceRating)


# In[47]:


m1 = sns.distplot(movies.AudienceRating,bins=15)


# In[48]:


m2 = sns.distplot(movies.CriticRating,bins=20)


# In[49]:


n1 = plt.hist(movies.AudienceRating,bins=15)


# In[50]:


n2 = plt.hist(movies.CriticRating,bins=15)


# In[51]:


#ntc dat for Audience Rating it is normal distribution for Critic Rating it is not perfect normal distribution


# In[52]:


#Stcked Histoganms
plt.hist(movies.BudgetMillions)
plt.show()


# In[53]:


#To get a data from a particular category of a variable
FilterDrama = movies.Genre == 'Drama'


# In[54]:


FilterDrama


# In[55]:


movies[FilterDrama]


# In[56]:


movies[FilterDrama].BudgetMillions


# In[57]:


plt.hist(movies[movies.Genre=='Drama'].BudgetMillions)
plt.show()


# In[58]:


plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
plt.show()


# In[59]:


plt.hist(movies[movies.Genre=='Drama'].BudgetMillions)
plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
plt.show()


# In[60]:


plt.hist(movies[movies.Genre=='Drama'].BudgetMillions)
plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions)
plt.show()


# In[61]:


plt.hist(movies[movies.Genre=='Action'].BudgetMillions)
plt.hist(movies[movies.Genre=='Drama'].BudgetMillions)
plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions)
plt.show()
#ntc that all hv diff bins


# In[62]:


#These are overlayed not stacked
plt.hist(movies[movies.Genre=='Action'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre=='Drama'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre=='Thriller'].BudgetMillions,bins=15)
plt.show()


# In[63]:


plt.hist([movies[movies.Genre=='Action'].BudgetMillions,movies[movies.Genre=='Drama'].BudgetMillions],bins=15,stacked=True)
plt.show()


# In[64]:


plt.hist([movies[movies.Genre=='Action'].BudgetMillions,          movies[movies.Genre=='Drama'].BudgetMillions,          movies[movies.Genre=='Thriller'].BudgetMillions],          bins=15,stacked=True)
plt.show()


# In[65]:


plt.hist([movies[movies.Genre=='Action'].BudgetMillions,          movies[movies.Genre=='Drama'].BudgetMillions,          movies[movies.Genre=='Thriller'].BudgetMillions,          movies[movies.Genre=='Comedy'].BudgetMillions],          bins=15,stacked=True)
plt.show()


# In[66]:


for gen in movies.Genre.cat.categories:
    print(gen)


# In[67]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
print(list1)


# In[68]:


h=plt.hist(list1)


# In[69]:


h=plt.hist(list1,bins=30)


# In[70]:


h=plt.hist(list1,bins=30,stacked=True)


# In[71]:


h=plt.hist(list1,bins=30,stacked=True,rwidth=1) #remove the gap b/w bars


# In[72]:


mylabels = list()
for gen in movies.Genre.cat.categories:
    mylabels.append(gen)


# In[73]:


h=plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.legend()
plt.show()


# In[74]:


mylabels


# In[75]:


#KDE plot
#Visualize AR vs CR
#This is the first method
vis1 = sns.lmplot(x='CriticRating',y='AudienceRating',data=movies,fit_reg=False,hue='Genre',size=7,aspect=1)


# In[76]:


#btr way is KDE plot
k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating)
#This shows us where the more density is
#And how the density is distributed from the chart
#and as v move away from the kernel or centre the density is getting lower


# In[77]:


k1 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True)


# In[78]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False)
#shows the grid


# In[79]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Reds')
#shows the colour


# In[80]:


#SubPlots
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating)
#Does the BudMill effect the AR?
#slice it at 20M and ntc the AR is approx 50
#as v move to d higher budget AR narrows down low


# In[81]:


sns.set_style("dark")


# In[82]:


k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating)


# In[83]:


sns.set_style("dark")
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating)
#this shows us that CR is most concwntrated bw 20 & 40


# In[84]:


#subplots
f, ax = plt.subplots(1,2) #gvs 1row,2cols


# In[85]:


f,ax = plt.subplots(1,3) #1row,3cols


# In[86]:


f,ax = plt.subplots(1,2)


# In[87]:


f,ax = plt.subplots(1,2,figsize=(12,6))


# In[88]:


f,ax = plt.subplots(1,2,figsize=(12,6))
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating)
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating)
#they r both printed on 1


# In[89]:


f,axes = plt.subplots(1,2,figsize=(12,6))
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[1])


# In[90]:


#ViolinPlots
v = sns.violinplot(x='Genre',y='CriticRating',data=movies)


# In[91]:


b = sns.boxplot(x='Genre',y='CriticRating',data=movies)
#From the below graph we can say that horror movies have low critic & audience rating i.e., low variance so mostly they incur
#loses on the other hand thriller movies have high audience & critic rating i.e., high variance so they have high profits. 


# In[92]:


#Facet Grids r created on rules based unlike subplots
#where we manually create them
vis1 = sns.lmplot(x='CriticRating',y='AudienceRating',data=movies,fit_reg=False,hue='Genre',size=7,aspect=1)


# In[93]:


#First create a FacetGrid
g = sns.FacetGrid(movies,row='Genre',hue='Genre')


# In[94]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')


# In[95]:


plt.scatter(movies.CriticRating,movies.AudienceRating)


# In[96]:


#now we want to map the scatter on tho the Facet Grid
#From the below graph we can say that Action & Comedy films are made on a large scale,Romance & Thriller movies are very low
g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
g.map(plt.scatter,'CriticRating','AudienceRating')


# In[97]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
g.map(plt.hist,'BudgetMillions')


# In[98]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
#here we analyse from left to right
#how did the relationship b/w AR evolve over yrs
#we can observe some trends


# In[99]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
g.set(xlim=(0,100),ylim=(0,100))


# In[100]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((20,60),(20,60))


# In[101]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((20,60),(20,60),c='grey',ls='--')


# In[102]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((20,60),(20,60),c='grey',ls='--')


# In[103]:


g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor="Black")
g.map(plt.scatter,'CriticRating','AudienceRating',**kws)
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((20,60),(20,60),c='grey',ls='--')
g.add_legend()


# In[104]:


#Finishing touches
list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)


# In[105]:


sns.set_style("whitegrid")
h = plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.legend()
plt.show()


# In[106]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
fig,ax = plt.subplots()
fig.set_size_inches(11.7,8.24) #size of A4 paper
plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.legend()
plt.show()


# In[107]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
fig,ax = plt.subplots()
fig.set_size_inches(11.7,8.24) #size of A4 paper
plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.title("MovieBudgetDistribution",fontsize=35,color="DarkBlue",fontname="Console")
plt.legend()
plt.show()


# In[108]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
f,ax = plt.subplots()
f.set_size_inches(11.7,8.24)
plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.title("MovieBudgetDistribution",fontsize=35,color="DarkBlue",fontname="Console")
plt.xlabel("Budget",fontsize=25,color="Red")
plt.ylabel("Number of Movies",fontsize=25,color="Green")
plt.legend()
plt.show()


# In[109]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
f,ax = plt.subplots()
f.set_size_inches(11.7,8.24)
plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.title("MovieBudgetDistribution",fontsize=35,color="DarkBlue",fontname="Console")
plt.xlabel("Budget",fontsize=25,color="Red")
plt.ylabel("Number of Movies",fontsize=25,color="Green")
plt.legend(frameon=True,prop={'size':20})
plt.show()


# In[110]:


list1 = []
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].BudgetMillions)
    mylabels.append(gen)
sns.set_style("whitegrid")
f,ax = plt.subplots()
f.set_size_inches(11.7,8.24)
plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.title("MovieBudgetDistribution",fontsize=35,color="DarkBlue",fontname="Console")
plt.xlabel("Budget",fontsize=25,color="Red")
plt.ylabel("Number of Movies",fontsize=25,color="Green")
plt.legend(frameon=True,framealpha=0.5,prop={'size':20})
plt.show()


# In[120]:


#Dash Board
#First Acedamia
sns.set_style("darkgrid")
f,axes = plt.subplots(2,2,figsize=(15,15))
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,1])
z = sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0])
k3 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Reds',ax=axes[1,1])
k3b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='Reds',ax=axes[1,1])
k1.set(xlim=(-20,-160))
k2.set(xlim=(-20,-160))
plt.show()


# In[121]:


#Conference
sns.set_style("dark",{"axes.facecolor":"black"})
fig,axes = plt.subplots(2,2,figsize=(15,15))
k1 = sns.kdeplot(movies.BudgetMillions,movies.AudienceRating,shade=True,shade_lowest=False,cmap='inferno',ax=axes[0,0])
k1b = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,cmap='cool',x=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,shade=True,shade_lowest=False,cmap='inferno',ax=axes[0,1])
k2b = sns.kdeplot(movies.BudgetMillions,movies.CriticRating,cmap='cool',ax=axes[0,1])
z = sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0],palette='YIOrRD')
k3 = sns.kdeplot(movies.CriticRating,movies.AudienceRating,shade=True,shade_lowest=False,cmap='Blues_r',ax=axes[1,1])
k3b = sns.kdeplot(movies.CriticRating,movies.AudienceRating,cmap='gist_gray_r',ax=axes[1,1])
k1.set(xlim=(-20,-160))
k2.set(xlim=(-20,-160))
plt.show()

