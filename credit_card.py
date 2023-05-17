
class CreditCard:
    def __init__(self,credit_card):
        self.credit_card = credit_card
        self.num = [z for z in str(self.credit_card)]

    def validate(self):
        if not self.extraction():
            print("False..")
            return "Either Hiphens are not used correctly or used non-digits"
        
        if not self.check_length():
            return "Invalid: Credit card number must be either consecutive 16 digits or every four digit separated by hiphens."
        
        if not self.check_fourtimes_repeat():
            return "Invalid: Credit card number should not have 4 or more consecutive repeated digits."
        
        if not self.starts_with():
            return "Credit card number must starts with 4,5 or 6."
        
        return "Valid Credit Card.."

    def extraction(self):
        index = 0
        hiphen = []
        un_want = []
        matching_list = [4,9,14]
        if len(self.num) == 19:
            for i in self.num:
                print("index: ",index)
                print("i: ",i)
                if self.num[index] == "-":
                    print("Index: ",index)
                    hiphen.append(index)
                    # self.num.pop(index)

                index = index + 1
            print("Self.Num: ",self.num)
            print("Hiphen List: ",hiphen)
            if hiphen == matching_list:
                while "-" in self.num:
                    self.num.remove("-")
            print("Self.Num: After removing Hiphens ",self.num)
            for ld in self.num:
                if not ld.isdigit():
                    un_want.append(ld)
            print("Un Wanted: ",un_want)       
            
            if not un_want and len(self.num) == 16:
                print("Lenght is : ",len(self.num))
                return True
            else:
                return False

        elif len(self.num) == 16:
            for w in self.num:
                if not w.isdigit():
                    return False
        
        elif len(self.num) < 16 or len(self.num) > 19:
            return False
                
        elif len(self.num) > 16 and len(self.num) < 19:
            return False
        
        return True

    def check_length(self):
        if len(self.num) > 19 or (len(self.num) < 19 and len(self.num) > 16):
            # print("checking False")
            return False
        
        elif len(self.num) == 16:
            for w in self.num:
                if not w.isdigit():
                    return False
        
        elif len(self.num) < 16:
            return False
        
        return True

    def starts_with(self):
        first_position = self.num[0]
        if first_position == "4" or first_position == "5" or first_position == "6":
            # print("If First Position: ",first_position)
            return True
        else:
            # print("Else First Position: ",first_position)
            return False

    def check_fourtimes_repeat(self):
        output = []
        current_count = 1
        for b in self.num:
            if not b.isdigit():
                self.num.remove(b)

        # print("Self.Num after POP: ",self.num)
        for i in range(1,len(self.num)):

            if self.num[i] == self.num[i-1]:
                # print("Num-i",self.num[i])
                # print("Num-i-1",self.num[i-1])
                # print("Current Count: ",current_count)
                current_count += 1
                
            else:
                output.append({self.num[i-1]:current_count})
                current_count = 1

            if i == len(self.num) - 1:
                output.append({self.num[i]:current_count})

        # print("Output: ",output)
        # print("Current Count: ",current_count)
        final = []
        for data in output:
            for v in data.values():
                # print("Value: ",v)
                if v >= 4:
                    # print("Data",data)
                    final.append(data)
                
        if final:
            return False
        else:
            return True
        
ob = "4134 6124 8111 2091"
obj = CreditCard(ob)

print(obj.validate())

