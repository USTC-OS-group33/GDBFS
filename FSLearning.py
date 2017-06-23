import neo4jdb

LEARNING_RATE = 0.009
MAX_LENGTH=200

Ndb=neo4jdb.neo4jdb()      

class Markov:

    def __init__(self):
        self.last_node=[]

        


    def learn(self, source, to):
        ls_of_adj=Ndb.get_adj_node
        if to in ls_of_adj:
            for tar in ls_of_adj:
                l=Ndb.getlength
                if(tar == ls_of_adj):
                    l=1.0/(1.0/l-LEARNING_RATE*(1.0/l-1))
                else:
                    l=1.0/(1.0/l-LEARNING_RATE/l)
                Ndb.changerelation()
        
        else:
            delta=0
            for tar in ls_of_adj:
                l=Ndb.getlength
                delta=delta+LEARNING_RATE/l
                l=1.0/(1.0/l-LEARNING_RATE/l)
                Ndb.changerelation()
            l=1/delta
            if(len(ls_of_adj)==0):
                l=1
            Ndb.create_relation()


        def trim(self, source):
            ls_of_adj=Ndb.get_adj_node
            for node in ls_of_adj:
                l=Ndb.getlength
                if(l>MAX_LENGTH):
                    Ndb.deleterelation
                    

