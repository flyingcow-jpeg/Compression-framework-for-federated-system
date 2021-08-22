import tensorflow as tf

def prune(before,after,p):
    global c
    f=after-before
    for i in [0,2,4,6]:
        # ct=np.count_nonzero(f[i])
        # print(ct)
        updates=f[i]
        all_=abs(updates).flatten()
        all_=all_[all_!=0]
        l=int(len(all_)*p)
        k=max(np.partition(all_,l)[:l])
        updates[abs(updates)<=k]=int(0)
        f[i]=updates
    #     print(ct-np.count_nonzero(f[i]))
    #     print("---")
    # print("###")
    return f+before


def disp(t):
    for i in t:
        print(i.shape)
        print("-")


def kmeans(f):
    x=f.flatten()
    y=x.reshape(-1,1)
    clusters_n = 128
    iteration_n = 100
    points = tf.constant(y)
    centroids = tf.Variable(tf.slice(tf.random_shuffle(points), [0, 0], [clusters_n, -1]))
    points_expanded = tf.expand_dims(points, 0)
    centroids_expanded = tf.expand_dims(centroids, 1)
    distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
    assignments = tf.argmin(distances, 0)
    means = []
    for c in range(clusters_n):
        means.append(tf.reduce_mean(
          tf.gather(points, 
                    tf.reshape(
                      tf.where(
                        tf.equal(assignments, c)
                      ),[1,-1])
                   ),reduction_indices=[1]))
    new_centroids = tf.concat(means, 0)
    update_centroids = tf.assign(centroids, new_centroids)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
      sess.run(init)
      for step in range(iteration_n):
        [_, centroid_values, points_values, assignment_values] = sess.run([update_centroids, centroids, points, assignments])
    return centroid_values

def call_kmeans(before,after):
        f=after-before
        # Layer 6
        c=kmeans(f[6])
        # print(np.count_nonzero(f[6]))
        c = c[~np.isnan(c)]
        final_c=np.append(c,np.array([0,]))
        c1=final_c
        update_updates_with_centeroids(f[6],final_c)
        # print(np.count_nonzero(f[6]))
        return c1,f
        #return f
        
def update_updates_with_centeroids(x,c):
    for i in range(len(x)):
        if type(x[i])==np.ndarray or type(x[i])==list:
            update_updates_with_centeroids(x[i],c)
        else:
            x[i]=find_nearest_centroid(c,x[i])

def find_nearest_centroid(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def convert(t1 , t2):
    t1=np.array(t1)
    t2=np.array(t2)
    disp(t1)
    disp(t2)
    

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:47:59 2021

@author: ishan
"""

# import bisect

import numpy as np
#print(np.__version__)
import sys




#disp(before)

# '''
# import numpy as np
# print(np.__version__)
# '''
# before = np.load("before.npy")
# after = np.load("after.npy")
# print(before[6],after[6])



# c=0
# # print(type(before))
# def count(z):
#     global c
#     for i in z:
#         if type(i)== np.ndarray or type(i)== list:
#             count(i)
#         else:
#             c+=1
            
# print(64*32*5*5)

# def prune(before,after,p):
#     global c
#     f=after-before
#     # layer 0
#     # print(max(f[0].flatten()))
#     updates=f[0]
#     all_=abs(updates).flatten()
#     l=int(len(all_)*p)
#     k=max(np.partition(all_,l)[:l])  
#     updates[abs(updates)<=k]=0
#     f[0]=updates
#     # layer 2
#     # print(max(f[2].flatten()))
#     updates=f[2]
#     all_=abs(updates).flatten()
#     l=int(len(all_)*p)
#     k=max(np.partition(all_,l)[:l])  
#     updates[abs(updates)<=k]=0
#     # count(f[2])
#     f[2]=updates
#     # print(c)
#     # print(np.count_nonzero(f[2]))
#     # layer 5
#     updates=f[4]
#     all_=abs(updates).flatten()
#     l=int(len(all_)*p)
#     k=max(np.partition(all_,l)[:l])    
#     updates[abs(updates)<=k]=0
#     f[4]=updates
#     # layer 7
#     updates=f[6]
#     all_=abs(updates).flatten()
#     l=int(len(all_)*p)
#     k=max(np.partition(all_,l)[:l])
#     updates[abs(updates)<=k]=0
#     # count(f[6])
#     f[6]=updates
#     return before+f

if __name__=="__main__":
    first = np.load("first.npy")
    before = np.load("before.npy")
    after = np.load("after.npy")
    disp(first)
    # for i in range(128):
    #     for j in range(62):
    #         if before[6][i][j]!=after[6][i][j]:
    #             print(before[6][i][j],after[6][i][j])
    #         else:
    #             print("True")
    # print(np.count_nonzero(a1[6]),np.count_nonzero(a2[6]))
    # c1,t3=call_kmeans(first,after)
    # print(len(c1),len(np.unique(t3[6].flatten())))
    # print(sorted(c1)==sorted(np.unique(t3[6].flatten())))
    #np.save("sparsification",t3)

# print(sys.getsizeof(before)*3136)
# print(sys.getsizeof(after)*3136)
        