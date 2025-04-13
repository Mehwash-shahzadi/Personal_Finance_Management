class Category:

    @staticmethod
    def load_standard_categories():
        ''' Main categories'''
        food = Category("Food", 1)
        transport = Category("Transport", 2)
        bills = Category("Bills", 3)

        '''Subcategories for Food'''
        groceries = Category("Groceries", 4)
        dining_out = Category("Dining Out", 5)
        food.add_subcategory(groceries)
        food.add_subcategory(dining_out)
 
        '''Subcategories for Transport'''
        fuel = Category("Fuel", 6)
        public_transport = Category("Public Transport", 7)
        transport.add_subcategory(fuel)
        transport.add_subcategory(public_transport)

        '''Subcategories for Bills'''
        electricity = Category("Electricity", 8)
        internet = Category("Internet", 9)
        bills.add_subcategory(electricity)
        bills.add_subcategory(internet)

        return [food, transport, bills]
    
    def __init__(self,name,id,parent_category=None):
        self.name=name
        self.id=id
        self.parent_category = parent_category
        self.subcategories_list = []

    def add_subcategory(self,subcategory):
        self.subcategories_list.append(subcategory)
        subcategory.parent_category = self
        print(f"Subcategory '{subcategory.name}' added to category '{self.name}'.")
        return self.subcategories_list
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return (f'Category(name:{self.name},id:{self.id})')
    
    def search_by_id(self,id):
        '''search by id'''
        if self.id==id:
            return self
        for subcat in self.subcategories_list:
            result=subcat.search_by_id(id)
            if result:
               return result
        return None
    
    def search_by_name(self,name):
        '''search by name '''
        if self.name==name:
            return self
        for subcat in self.subcategories_list:
            result=subcat.search_by_name(name)
            if result:
               return result
        return None
    

    def filter_category_by_id(self,id):
        '''filter by id'''
        result=[]
        if self.id==id:
            result.append(self)
        for subcat in self.subcategories_list:
            result.extend(subcat.filter_category_by_id(id))
        return result
    
    def filter_category_by_name(self,name):
        '''filter by name'''
        result=[]
        if self.name==name:
            result.append(self)
        for subcat in self.subcategories_list:
            result.extend(subcat.filter_category_by_name(name))
        return result
    

         
    # def search_by_name_or_id(self,name,id):
    #     if self.name==name or self.id==id:
    #         return self.name,self.id
    #     for subcat in self.subcategories_list:
    #         result=subcat.search_by_name_or_id(name,id)
    #         if result:
    #            return result
    #     return None

    def create_custom_category(self,parent_id,name,id):
        '''Add categories'''
        parent_category=self.search_by_id(parent_id)
        if parent_category:
            new_category=Category(name,id)
            parent_category.add_subcategory(new_category)
            print(f"Custom category '{name}' with ID {id} has been added to parent category '{parent_category.name}'")
        else:
            print('parent category not found!')

    def edit_category(self,id,new_name):
        '''edit category'''
        category1=self.search_by_id(id)
        if category1:
            category1.name=new_name
        else:
            print('category not found')
    
    def delete_category(self,id):
       '''delete category'''
       for subcat in self.subcategories_list[:]:
           if subcat.id==id:
               self.subcategories_list.remove(subcat)
               print(f'category with the id deleted successfully!')
               return True
           else:
               deleted=subcat.delete_category(id)
               if deleted:
                   return True
       return False
