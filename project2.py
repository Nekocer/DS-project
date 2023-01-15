class Node:
    def __init__ (self, key=None, next=None):
        self.key = key
        self.next = next

            
class BuildBinaryTree:
    def __init__(self):
        self.root = None
        self.right = None
        self.left = None
        self._size = 0
    
    #A method to get the node at index n.
    def index_n(self, n): 
        if self.root is None:
            return False
        else:
            value = self.root
            for i in range(n):
                value = value.next
            return value    
    
    #To get the parent of the node at index n
    def findParent(self, n):
        #conditions: root does not have parent; other nodes have parent node
        if n == 0:
            return print("No parent")
        else:
            return print(f'the value is {self.index_n((n-1)//2)}')
    
    #To get the right child of the node at index n
    def findRightChild(self, n):
        #two conditions: no right child or right child exists
        if self.right is None:
            return False
        else:
            return print(f'the right child is{self.index_n(2*n+2)}')
    
    #To get the left child if the nide at index n
    def findLeftChild(self, n):
        #two conditions: no left child or left child exists
        if self.left is None:
            return False
        else:
            return print(f'the left child is{self.index_n(2*n+1)}')


class PriorityQueue:
    
    def __init__(self):#init operation
        self.queue = BuildBinaryTree()

    def insert(self, key):#insert a node into the queue according to the key
        self.queue.append(Node(key))#use append method to add the node to the end

    #delete the minimum 
    def delMin(self):
        #different conditions
        if self.queue.size ==0:
            return False  
        #delete the root node(also the minimum key)    
        elif self.queue.size() >= 1:
            return self.root




#Visualize the results by an example 
pq = PriorityQueue()
time = []
for i in range(100):#the most common to know visualize the time complexity of insert method
    start = time.perf_counter #end minus start
    pq.insert(i)
    end = time.perf_counter
    time.append(end-start)
print(time)

#find the relationship between index i and time(spent by insert method)
#and we could use the same way to visualize the time complexity of delMin method.