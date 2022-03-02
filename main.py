

d = dict()


class eventNode:
  def __init__(self, note, time, prev = None, next = None):
    self.note = note
    self.time = time
    self.prev = prev
    self.next = next

  
class daySchedule:
  def __init__(self):
    self.head = None 
    self.tail = None
    self.count = 0
  

  def push_front(self, note, time): 
    newNode = eventNode(note, time) 
    newNode.next = self.head 
    self.count += 1

    if self.head != None:
        self.head.prev = newNode 
        self.head = newNode 
        newNode.prev = None
    
    else: 
      self.head = newNode
      self.tail = newNode
      newNode.prev = None 
  
  def insertAfter(self, tmpNode, note, time):
    if tmpNode == None:
      print("Given node is empty")
    
    if tmpNode != None:
      self.count += 1
      newNode = eventNode(note, time)
      newNode.next = tmpNode.next
      tmpNode.next = newNode
      newNode.prev = tmpNode
      if newNode.next != None:
        newNode.next.prev = newNode
      
      if tmpNode == self.tail:
        self.tail = newNode 
  
  def insertBefore(self, tmpNode, note, time): 
    if tmpNode == None:
      print("Given node is empty")
    
    if tmpNode != None:
      self.count += 1
      newNode = eventNode(note, time)
      newNode.prev = tmpNode.prev
      tmpNode.prev = newNode
      newNode.next = tmpNode
      if newNode.prev != None:
        newNode.prev.next = newNode
      
      if tmpNode == self.head:
        self.head = newNode 

  def timeInsert(self, note, time):
     newNode = eventNode(note, time)
     
     if self.count == 0:
       self.head = newNode
       self.tail = newNode
       self.count += 1
       return

     tmp = self.head
     for i in range(self.count):
       if newNode.time > tmp.time:
         if tmp.next == None:
           self.insertAfter(tmp, note, time)
           return
         else:
          tmp = tmp.next
       else:
         self.insertBefore(tmp, note, time)
         return

  def removeByNote(self, note):
     rm = self.head
     for i in range(self.count):
       if note != rm.note:
         rm = rm.next
       else:
         self.count -= 1
         rm.prev.next = rm.next
         rm.next.prev = rm.prev
         return

  def displaySchedule(self):
     tmp = self.head
     for i in range(self.count):
       print(i+1, tmp.note, tmp.time)
       tmp = tmp.next



dl = daySchedule()
# some bug with times size 10?
#dl.push_front("Shaw", 9)
dl.timeInsert("abs", 0)
dl.timeInsert("Sam", 2)
dl.timeInsert("filter", 1)
dl.timeInsert("hasattr", 10)
dl.timeInsert("KeyboardInterrupt", -5)
dl.removeByNote("Sam")
dl.push_front(7, "time1")
dl.displaySchedule()

#dict[key] = 7
