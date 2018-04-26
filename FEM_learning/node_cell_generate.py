
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
from fealpy.mesh.TriangleMesh import TriangleMesh
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import numpy as np


# In[3]:


box = [0,1,0,1]#正方形区域
nx = 5#x轴均匀5等分
ny = 5#y轴均匀5等分
NN = (nx+1)*(ny+1)#node的数目
NC = nx*ny#小正方形的数目


# In[4]:


node = np.zeros((NN,2))#node的类型
X=np.linspace(box[0],box[1],nx+1)+np.zeros(nx+1).reshape(-1,1)#沿着y轴正向，x轴正向一排一排生成的node矩阵
Y=X.T#行列互换
node[:,0] = X.flatten()#按行取出矩阵X中的元素
node[:,1] = Y.flatten()
cell = np.zeros((2*NC,3),dtype = np.int)#cell的类型
sign = np.arange(NN).reshape(nx+1,ny+1)#网格每个点的标号，有nx+1列
cell[:NC,0] = sign[0:-1,1:].flatten()#每个小正方形下面的小三角形
cell[:NC,1] = sign[1:,1:].flatten()
cell[:NC,2] = sign[0:-1,0:-1].flatten()
cell[NC:,0] = sign[1:,0:-1].flatten()#每个小正方形上面的小三角形
cell[NC:,1] = sign[0:-1,0:-1].flatten()
cell[NC:,2] = sign[1:,1:].flatten()
print(node)
print(cell)


# In[5]:


from fealpy.mesh.TriangleMesh import TriangleMesh
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
tmesh = TriangleMesh(node, cell)
fig, axes = plt.subplots(1, 3,figsize=(15,15))
tmesh.add_plot(axes[0])
tmesh.find_node(axes[0], showindex=True, markersize=20, fontsize=20)
tmesh.find_cell(axes[0], showindex=True, markersize=15, fontsize=15)
axes[0].set_title('mesh')
for ax in axes.reshape(-1)[1:]:
    ax.axis('tight')
    ax.axis('off')
axes[1].table(cellText=node, rowLabels=np.arange(NN), loc='center')
axes[1].set_title('node', y=0.2)
axes[2].table(cellText=cell, rowLabels=np.arange(2*NC), loc='center')
axes[2].set_title('cell', y=0.9)
plt.tight_layout(pad=0.4, w_pad=1, h_pad=1.0)
plt.show()

