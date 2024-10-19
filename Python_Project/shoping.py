class ShopingCard:
    def __init__(self):

        self.total_item = []

    def Add_item(self):
        for i in range(1,5):
            item = input("\nEnter your faivret item "+str(i)+":")
            self.total_item.append(item)
        print("Total Item Is : ",self.total_item)
    
    def Remove_item(self,item):
        self.total_item.remove(item)
        print("Total Item Is : ",self.total_item)

    def Check_item(self):
        print("Total Item Is : ",self.total_item)




obj = ShopingCard()
obj.Add_item()
# obj.Check_item()
obj.Remove_item(input("\nEnter Item Which You To Remove : "))
# obj.Check_item()


