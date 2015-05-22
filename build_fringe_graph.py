import networkx as nx
import json
import pickle


global di
di = nx.DiGraph()

unlabeled_data = file ("34-2014_master_user_list.json")
graph_data = file ("34-2014_social_graph.json")

j = json.load(unlabeled_data)
#print j["346990051"]["followers_count"]
unlabeled_data.close ()

# file = open("Newfile.txt","w")
# file.write("Testing!\n")
# file.write("Double-Test\n")
# file.close()

# file = open("Rochester_Twitter_Users.txt","w")
# for key, value in j.iteritems():
#     file.write(key)
#     file.write("\n")
# file.close()    

for key, value in j.iteritems():
    #print key
    di.add_node(int(key))

# file = open("Rochester_Fringe_Twitter_Users.txt","w")
# while True:
#     line = graph_data.readline()
#     if line == "":
#         break
#     #print line
#     try:
#         j = json.loads(line)
#         #ego = int(j["user_id"])
#         for out_neighbor in j["follower_ids"]:
#             for in_neighbor in j["friend_ids"]:
#                 if out_neighbor == in_neighbor:
#                     if out_neighbor not in di:
#                         di.add_node(int(out_neighbor))
#                         file.write(str(j["user_id"]))
#                         file.write(" ")
#                         file.write(str(out_neighbor))
#                         file.write("\n")
#     except ValueError:
#         pass
# file.close()        
# graph_data.close()

# file = open("Rochester_Fringe_Twitter_Users.txt","w")
# while True:
#     line = graph_data.readline()
#     if line == "":
#         break
#     #print line
#     try:
#         j = json.loads(line)
#         a = set(j["follower_ids"])
#         b = set(j["friend_ids"])
#         #temp = j["follower_ids"].intersection(j["friend_ids"])
#         temp = a.intersection(b)
#         for new_users in temp:
#             if new_users not in di:
#                 di.add_node(int(new_users))
#                 file.write(str(j["user_id"]))
#                 file.write(" ")
#                 file.write(str(new_users))
#                 file.write("\n")
#     except ValueError:
#         pass
# file.close()        
# graph_data.close()

file = open("Rochester_Fringe_Count.txt","w")
count = 0
while True:
    line = graph_data.readline()
    if line == "":
        break
    #print line
    try:
        j = json.loads(line)
        a = set(j["follower_ids"])
        b = set(j["friend_ids"])
        #temp = j["follower_ids"].intersection(j["friend_ids"])
        temp = a.intersection(b)
        for new_users in temp:
            if new_users not in di:
                count = count + 1
                file.write(str(count))
                file.write("\n")
                di.add_node(int(new_users))
    except ValueError:
        pass
file.close()        
graph_data.close()

#file = open("Rochester_Twitter_Oneway_Connections.txt","w")
while True:
    line = graph_data.readline()
    if line == "":
        break
    #print line
    try:
        j = json.loads(line)
        ego = int(j["user_id"])
        for out_neighbor in j["follower_ids"]:
            if out_neighbor == ego:
                print "self %d" % ego
            elif out_neighbor in di:
                di.add_edge(ego, out_neighbor)
                #file.write(str(ego))
                #file.write(" ")
                #file.write(str(out_neighbor))
                #file.write("\n")
        for in_neighbor in j["friend_ids"]:
            if in_neighbor == ego:
                print "self %d" % ego
            elif in_neighbor in di:
                di.add_edge(in_neighbor, ego)
                #file.write(str(in_neighbor))
                #file.write(" ")
                #file.write(str(ego))
                #file.write("\n")
    except ValueError:
        pass
#file.close()        
graph_data.close()

# while True:
#     line = graph_data.readline()
#     if line == "":
#         break
#     #print line
#     try:
#         j = json.loads(line)
#         ego = int(j["user_id"])
#         for out_neighbor in j["follower_ids"]:
#             if out_neighbor == ego:
#                 print "self %d" % ego
#             elif out_neighbor in di:
#                 di.add_edge(ego, out_neighbor)
#         for in_neighbor in j["friend_ids"]:
#             if in_neighbor == ego:
#                 print "self %d" % ego
#             elif in_neighbor in di:
#                 di.add_edge(in_neighbor, ego)
#     except ValueError:
#         pass
# graph_data.close()


u = di.to_undirected(reciprocal=True)
ccs = nx.connected_component_subgraphs(u)
l = sorted(ccs, key = lambda x: len(x), reverse=True)
u = l[0]

#l = list(u.nodes())
#v = u.subgraph(l[0:8000])
#ccs = nx.connected_component_subgraphs(v)
#l = sorted(ccs, key = lambda x: len(x), reverse=True)
#u = l[0]

#file = open("Rochester_Twitter_Mutual_Connections.txt","w")
for ego,alter in u.edges():
    u[ego][alter]["embeddedness"] = 1 + len(set(u.neighbors(ego)) & set(u.neighbors(alter)))
    # file.write(str(ego))
    # file.write(" ")
    # file.write(str(alter))
    # file.write("\n")   
#file.close()

# u = di.to_undirected(reciprocal=True)
# ccs = nx.connected_component_subgraphs(u)
# l = sorted(ccs, key = lambda x: len(x), reverse=True)
# u = l[0]

# #l = list(u.nodes())
# #v = u.subgraph(l[0:8000])
# #ccs = nx.connected_component_subgraphs(v)
# #l = sorted(ccs, key = lambda x: len(x), reverse=True)
# #u = l[0]
# for ego,alter in u.edges():
#     u[ego][alter]["embeddedness"] = 1 + len(set(u.neighbors(ego)) & set(u.neighbors(alter)))

# return u

# neighbors = set()
# def build_neighbor_graph (labeled_data_name, graph_pkl_name):
#     global u
#     global neighbors
    
#     labeled_data = file (labeled_data_name)
#     graph_file = file (graph_pkl_name)
#     u = pickle.load(graph_file)

#     print len(u)
    
#     global neighbors 
#     while True:
#         line = labeled_data.readline()
#         if line == "":
#             break
#         orientation, description, key, profile_image_url, profile_banner_url, profile_background_image_url = line.split("\t")
        
#         ego = int(key)
#         if ego in u:
#             egoset = set()
#             egoset.add(ego)
#             neighbors = neighbors | set(u.neighbors(ego)) | egoset
#             #print len(neighbors)

#     labeled_data.close()
#     u.remove_nodes_from(set(u.nodes()) - neighbors)
#     print len(u)
#     #u = di.to_undirected(reciprocal=True)
#     ccs = nx.connected_component_subgraphs(u)
#     l = sorted(ccs, key = lambda x: len(x), reverse=True)
#     u = l[0]
#     print len(u)
#     return u

