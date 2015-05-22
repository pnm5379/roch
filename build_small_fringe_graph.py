import networkx as nx
import json
import pickle
#import matplotlib.pyplot as plt


global di
di = nx.DiGraph()

#unlabeled_data = file ("51-2014_master_user_list.json")
unlabeled_data = file ("master_user_list.json")
#graph_data = file ("34-2014_social_graph.json")
#graph_data = file ("07-2015_social_graph.json")
graph_data = file ("social_graph.json")

j = json.load(unlabeled_data)
unlabeled_data.close () 

people = 0
agents = set()
for key, value in j.iteritems():
    di.add_node(int(key))
    people = people + 1
    agents.add(int(key))

print "People"
print people

#file = open("Rochester_Fringe_Count.txt","w")
found = 0
#other = 0
total = 0
found_agents = set()
while True:
    line = graph_data.readline()
    if line == "":
        break
    try:
        j = json.loads(line)
        #total = total + 1
        #c = set(j["user_id"])
        #if c in agents:
        #if int(j["user_id"]) in di:
        if int(j["user_id"]) in agents:
            #a = set(j["follower_ids"])
            #b = set(j["friend_ids"])
            #temp = j["follower_ids"].intersection(j["friend_ids"])
            temp = set(j["follower_ids"]).intersection(set(j["friend_ids"]))
            #temp = a.intersection(b)
            found = found + 1
            found_agents.add(int(j["user_id"]))
            #file.write(str(found))
            #file.write("\n")
            for new_users in temp:
                if new_users not in di:
                    di.add_node(int(new_users))
        #else:
            #other = other + 1            
    except ValueError:
        pass
#file.close()        

graph_data.close()

#file = open("34-2014_social_graph.json",'r')
graph_data = file ("34-2014_social_graph.json")

print "Found"
print found
# print "Other"
# print other
# print "Total"
# print total

missing_agents = agents.difference(found_agents)


#graph_data = file ("34-2014_social_graph.json")

connections = 0
fringe_graph = 0
#file = open("Rochester_Twitter_Oneway_Connections.txt","w")
while True:
    line = graph_data.readline()
    if line == "":
        break
    #print line
    try:
        j = json.loads(line)
        if int(j["user_id"]) in agents:
            ego = int(j["user_id"])
            for out_neighbor in j["follower_ids"]:
                if out_neighbor == ego:
                    print "self %d" % ego
                elif out_neighbor in di:
                    di.add_edge(ego, out_neighbor)
                    connections = connections + 1
                    #file.write(str(ego))
                    #file.write(" ")
                    #file.write(str(out_neighbor))
                    #file.write("\n")
            for in_neighbor in j["friend_ids"]:
                if in_neighbor == ego:
                    print "self %d" % ego
                elif in_neighbor in di:
                    di.add_edge(in_neighbor, ego)
                    connections = connections + 1
                    #file.write(str(in_neighbor))
                    #file.write(" ")
                    #file.write(str(ego))
                    #file.write("\n")
        if int(j["user_id"]) in di:
            if int(j["user_id"]) not in agents:
                fringe_graph = fringe_graph + 1
    except ValueError:
        pass
#file.close()        
graph_data.close()

print "Connections"
print connections


u = di.to_undirected(reciprocal=True)
ccs = nx.connected_component_subgraphs(u)
l = sorted(ccs, key = lambda x: len(x), reverse=True)
u = l[0]

#print "Tester"


#file = open("Rochester_Twitter_Mutual_Connections.txt","w")
#for ego,alter in u.edges():
    #u[ego][alter]["embeddedness"] = 1 + len(set(u.neighbors(ego)) & set(u.neighbors(alter)))
    #u[ego][alter]["embeddedness"] = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
    

    #embed_temp = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))

    # if mutuals < 100:
    #     #file.write(str(u[ego]))
    #     #file.write(" ")
    #     #file.write(str(u[ego][alter]))
    #     #file.write(" ")
    #     file.write(str(ego))
    #     file.write(" ")
    #     file.write(str(alter))
    #     file.write(" ")
    #     file.write(str(u[ego][alter]["embeddedness"]))
    #     file.write(" ")
    #     file.write(str(embed_temp))
    #     file.write("\n")

    

    # file.write(str(ego))
    # file.write(" ")
    # file.write(str(alter))
    # file.write("\n")   
#file.close()

mutuals = 0
file = open("Embeddedness_Full_Network.txt",'w')
for ego,alter in u.edges():
    a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
    b = len(set(u.neighbors(ego)))
    c = len(set(u.neighbors(alter)))
    file.write(str(a))
    file.write(" ")
    file.write(str(b))
    file.write(" ")
    file.write(str(c))
    file.write(" ")
    #file.write(str(u[ego][alter]["embeddedness"]))
    file.write("\n")
    mutuals = mutuals + 1
file.close()

print "Mutuals"
print mutuals

#test1 = 0
#test2 = 0
high_embeddedness = set()
file = open("Embeddedness_Non-Fringe_Fringe.txt",'w')
for ego,alter in u.edges():
    if ego in agents:
        if alter not in agents:
            a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
            b = len(set(u.neighbors(ego)))
            c = len(set(u.neighbors(alter)))
            file.write(str(a))
            file.write(" ")
            file.write(str(b))
            file.write(" ")
            file.write(str(c))
            file.write(" ")
            #file.write(str(u[ego][alter]["embeddedness"]))
            file.write("\n")
            #test1 = test1 + 1
            if int(a) >= 50:
                high_embeddedness.add(alter)
    if alter in agents:
        if ego not in agents:
            a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
            b = len(set(u.neighbors(ego)))
            c = len(set(u.neighbors(alter)))
            file.write(str(a))
            file.write(" ")
            file.write(str(b))
            file.write(" ")
            file.write(str(c))
            file.write(" ")
            #file.write(str(u[ego][alter]["embeddedness"]))
            file.write("\n")  
            #test2 = test2 + 1  
            if int(a) >= 50:
                high_embeddedness.add(ego)    
file.close()

#print "Test1"
#print test1
#print "Test2"
#print test2

file = open("Embeddedness_Non-Fringe_Non-Fringe.txt",'w')
for ego,alter in u.edges():
    if ego in agents:
        if alter in agents:
            a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
            b = len(set(u.neighbors(ego)))
            c = len(set(u.neighbors(alter)))
            file.write(str(a))
            file.write(" ")
            file.write(str(b))
            file.write(" ")
            file.write(str(c))
            file.write(" ")
            #file.write(str(u[ego][alter]["embeddedness"]))
            file.write("\n")
    if alter in agents:
        if ego in agents:
            a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
            b = len(set(u.neighbors(ego)))
            c = len(set(u.neighbors(alter)))
            file.write(str(a))
            file.write(" ")
            file.write(str(b))
            file.write(" ")
            file.write(str(c))
            file.write(" ")
            #file.write(str(u[ego][alter]["embeddedness"]))
            file.write("\n")            
file.close()

# for ego in u.edges():
#     u[ego]["degree"] = nx.degree(ego)

file = open("Degree_Full_Network.txt",'w')
for ego in u.nodes():
    deg = len(set(u.neighbors(ego)))
    file.write(str(deg))
    file.write("\n")
file.close()

high_degree = set()
fringe = 0
file = open("Degree_Fringe.txt",'w')
for ego in u.nodes():
    if ego not in agents:
        deg = len(set(u.neighbors(ego)))
        file.write(str(deg))
        file.write("\n")
        fringe = fringe + 1
        if int(deg) >= 50:
            high_degree.add(ego)
file.close()

print "Fringe"
print fringe

print "Fringe Graph"
print fringe_graph

file = open("Degree_Non-Fringe.txt",'w')
for ego in u.nodes():
    if ego in agents:
        deg = len(set(u.neighbors(ego)))
        file.write(str(deg))
        file.write("\n")
file.close()

file = open("Degree_Non-Fringe_to_Non-Fringe.txt",'w')
for ego in u.nodes():
    if ego in agents:
        deg = len(set(u.neighbors(ego)).intersection(agents))
        file.write(str(deg))
        file.write("\n")
file.close()

# file = open("Degree_Non-Fringe_Fringe.txt",'w')
# for ego in u.edges():
#     if ego in agents:
#         if alter not in agents:
#             file.write(str(u[ego]["degree"]))
#             file.write("\n")
# file.close()

# file = open("Degree_Non-Fringe_Non-Fringe.txt",'w')
# for ego in u.edges():
#     if ego in agents:
#         if alter in agents:
#             file.write(str(u[ego]["degree"]))
#             file.write("\n")
# file.close()

#deg_all = nx.degree(u)
#plt.loglog(deg_all)


# file = open("Norm_Embeddedness_Full_Network.txt",'w')
# for ego,alter in u.edges():
#     a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
#     b = a / len(set(u.neighbors(ego)))
#     c = a / len(set(u.neighbors(alter)))
#     file.write(str(b))
#     file.write("\n")
#     file.write(str(c))
#     file.write("\n")
# file.close()

# file = open("Norm_Embeddedness_Non-Fringe_Fringe.txt",'w')
# for ego,alter in u.edges():
#     if ego in agents:
#         if alter not in agents:
#             a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
#             b = a / len(set(u.neighbors(ego)))
#             c = a / len(set(u.neighbors(alter)))
#             file.write(str(b))
#             file.write("\n")
#             file.write(str(c))
#             file.write("\n")
# file.close()

# file = open("Norm_Embeddedness_Non-Fringe_Non-Fringe.txt",'w')
# for ego,alter in u.edges():
#     if ego in agents:
#         if alter in agents:
#             a = len(set(u.neighbors(ego)).intersection(set(u.neighbors(alter))))
#             b = a / len(set(u.neighbors(ego)))
#             c = a / len(set(u.neighbors(alter)))
#             file.write(str(b))
#             file.write("\n")
#             file.write(str(c))
#             file.write("\n")
# file.close()


file = open("Mising Agents.txt","w")
for agents in missing_agents:
    file.write(str(agents))
    file.write("\n")
file.close()

print "High Embeddedness"
print len(high_embeddedness)

print "High Degree"
print len(high_degree)

file = open("High Embeddednss Fringe Nodes.txt","w")
for agents in high_embeddedness:
    file.write(str(agents))
    file.write("\n")
file.close()

file = open("High Degree Fringe Nodes.txt","w")
for agents in high_degree:
    file.write(str(agents))
    file.write("\n")
file.close()

