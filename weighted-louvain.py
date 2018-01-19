#Community detection using Louvain
# This program calculates the modules and their node membership in an undirected network  
# using Louvain at best modularity value out of different levels
# Reads the edgelist from a tab separated text file and produces following two output files: 
# best_com_size : Community label and their size
# best_node_membership : Node id and their membership

import timeit
import networkx as nx
import community

class WeightedLouvain():
    """docstring for WeightedLouvain:
    What it do? :
    Version:
    Author:
    Update:
    """
    def __init__(self, inFile):
        try:
            self.inFile = open(inFile,'rb')
        except:
            print "Error in Initialization:", inFile," File not found!!!"

    def __buildNetwork(self):
        try:
            with self.inFile as inf:
                next(inf, '')
                G = nx.read_weighted_edgelist(inf, delimiter='\t', nodetype=str)

            self.partition = community.best_partition(G)
            self.best_mod = community.modularity(self.partition,G)
            return 1
        except:
            print "Community detection error!! "
            return 0


    def comunityDetail(self, file1='', file2=''):
        if file1 and file2:
            pass
        else:
            file1 = "best_com_size"
            file2 = "best_node_membership"

        Wfile1 = open(file1,'w')
        Wfile2 = open(file2,'w')

        if self.__buildNetwork():

            size = float(len(set(self.partition.values())))
            print("Number of communities",size)
            Wfile1.write("Community\tSize\n")

            for com in set(self.partition.values()):
                list_nodes = [nodes for nodes in self.partition.keys()
                              if self.partition[nodes] == com]
                com_size = float(len(list_nodes))
                x1=str(com)+"\t"+str(com_size)+"\n"
                Wfile1.write(x1)     #write output in the file

            Wfile2.write("NodeId\tCommunityLabel\n") #write header in the file

            #print memberships
            for nodes in set(self.partition.keys()):
                com= self.partition[nodes]
                #print (nodes,com)
                x2=str(nodes)+"\t"+str(com)+"\n"
                Wfile2.write(x2)     #write output in the file
                
            Wfile1.close()
            Wfile2.close()
            return 1
        else:
            print "Error in writing Output"
            return 0


def main():
    import argparse 
    parser = argparse.ArgumentParser()

    parser.add_argument('-i',action='store',dest='inputFile',help='Input File <format detatil>')
    rparse = parser.parse_args()
    infile = rparse.inputFile.strip()

    wL = WeightedLouvain(infile)
    start= timeit.default_timer()
    try:
        wL.comunityDetail()
        stop= timeit.default_timer()

        print("modularity:", wL.best_mod)
        print("runtime: "+str(stop-start))
    except:
        print "Import Error"


if __name__ == '__main__':
    main()
