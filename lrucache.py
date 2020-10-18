class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data ={}
        self.luk =""
        self.key_lru={}
        

    def get(self, key: int) -> int:
        # print(self.data)
        self.luk =key
        if key not in self.data.keys():
            return -1
        else:
            if len(self.key_lru) == 0:
                self.key_lru[key] = 1
            else:
                self.key_lru[key] =max(self.key_lru.values()) + 1
                return self.data[key]
            
        
        

    def put(self, key: int, value: int) -> None:
        
        if key in list(self.data.keys()):
            self.data[key] = value
            
    
        elif len(self.data) < self.capacity:
            self.data[key] = value
            
        else:
            
            # print(self.keyfreq
            # if len(self.data) >1:
            least_used = min(self.key_lru.values())
            # print(least_used)
            to_delete =[key  for (key, value) in self.key_lru.items() if value == least_used]
            # print(to_delete)
            # print(self.data)
            # print(self.key_lru)
                # to_delete = [key  for key in self.data.keys() if key != self.luk]
            self.data.pop(to_delete[0])
            self.key_lru.pop(to_delete[0])
            # else:
                # self.data.pop(self.luk)
            # self.keyfreq.pop(to_delete[0])
            self.data[key] = value
            
        if len(self.key_lru) == 0:
            self.key_lru[key] = 1
        else:
            self.key_lru[key] =max(self.key_lru.values()) + 1          
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)