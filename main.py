class Heap :
  def __init__(self):
    self.size = 0
    self.capacity = 20
    self.heap_arr = [None]*self.capacity 
    

  def left_child_index(self,parent_index):
    return 2*parent_index +1

  def right_child_index(self,parent_index):
    return 2*parent_index +2

  def parent_index(self,child_index):
    return int((child_index -1)/2)

  def has_left_child(self,parent_index):
    return self.left_child_index(parent_index)< self.size 
    
  def has_right_child (self,parent_index):
    return self.right_child_index(parent_index)< self.size 

  def has_parent (self,child_index):
    return self.parent_index(child_index) >= 0 

  def swap (self,first_index,second_index):
    temp = self.heap_arr[first_index]
    self.heap_arr[first_index] = self.heap_arr[second_index]
    self.heap_arr[second_index] = temp 

  def heapfy_up(self):
    value_index = self.size
    while (
      self.has_parent(value_index) and   
      self.heap_arr[self.parent_index(value_index)] > self.heap_arr[value_index]
    ):
      self.swap(self.parent_index(value_index),value_index)
      value_index = self.parent_index(value_index)

  
      
  def insert(self,value):
    if self.size == 0 : 
      self.heap_arr[0] = value
      self.size +=1 
    else :
      self.heap_arr[self.size] = value
      self.heapfy_up()
      self.size +=1

  def heapfy_down(self):
    value_index = 0
    while self.has_left_child(value_index):
      
      left_child_value = self.heap_arr[self.left_child_index(value_index)]
      right_child_value = self.heap_arr[self.right_child_index(value_index)] 
      value =self.heap_arr[value_index]
      min_child_index = None
      if  left_child_value< value:        
        min_child_index = self.left_child_index(value_index)
        if (self.has_right_child(value_index) and     
              right_child_value < left_child_value):
              min_child_index = self.heap_arr[self.right_child_index(value_index)]

      if min_child_index != None :
          self.swap(value_index,min_child_index)
          value_index = min_child_index
      else:
        break
        
      # print("min_child:",self.heap_arr[min_child_index])
      # print("value:",self.heap_arr[value_index])
      
      
  def delete_root(self):
    self.heap_arr[0] = self.heap_arr[self.size-1]
    self.heap_arr[self.size-1] = None
    self.size -=1
    self.heapfy_down()
if __name__ == "__main__":
  heap = Heap()
  heap.insert(10)
  heap.insert(3)
  heap.insert(4)
  heap.insert(2)
  heap.insert(0)
  heap.delete_root()
  heap.delete_root()
  heap.delete_root()

  
  
  
  
  
  
  
  print(heap.heap_arr)
  
    
    
    
    
    
    
    
