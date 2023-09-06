class NUMBER():
    #def __init__(self,num):
        #self.num = num

    def odd_even(self,num):
        try:
            if num%2 == 0:
                print("the given number is even")
            else:
                print("the given number is odd")
        except Exception as e:
            print(e)

obj = NUMBER()
obj.odd_even(6)