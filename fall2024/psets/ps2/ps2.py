class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    #THIS FUNCTION IS NOT CORRECT!!
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind-left_size-1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    #THIS FUNCTION IS CORRECT!!
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    #THIS FUNCTION IS TOO SLOW!!
    def insert(self, key):
        if self.key is None:
            self.key = key
            self.size = 1
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == "L":
            rotating_child = self.left  
        elif child_side == "R":
            rotating_child = self.right  
        else:
            return self  

    # Ensure the child being rotated exists
        if rotating_child is None:
            return self
       
        # Left Rotation
        if direction == "L":
            new_subtree_root = rotating_child.right 
            if new_subtree_root is None:
                return self  
        
            rotating_child.right = new_subtree_root.left  
            new_subtree_root.left = rotating_child  

        # Update parent's child to point to new_subtree_root
            if child_side == "L":
                self.left = new_subtree_root 
            else:
                self.right = new_subtree_root  
    
        #Right Rotation
        elif direction == "R":
            new_subtree_root = rotating_child.left  
            if new_subtree_root is None:
                return self  
        
            rotating_child.left = new_subtree_root.right 
            new_subtree_root.right = rotating_child  

        # Update parent's child to point to new_subtree_root
            if child_side == "L":
                self.left = new_subtree_root  
            else:
                self.right = new_subtree_root 

        if rotating_child is not None:
            rotating_child.size = 1 + (rotating_child.left.size if rotating_child.left else 0) + (rotating_child.right.size if rotating_child.right else 0)
        if new_subtree_root is not None:
            new_subtree_root.size = 1 + (new_subtree_root.left.size if new_subtree_root.left else 0) + (new_subtree_root.right.size if new_subtree_root.right else 0)
        return self  # Return the modified tree
    
    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self