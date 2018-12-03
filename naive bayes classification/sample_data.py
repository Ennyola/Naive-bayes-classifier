import math
class Probability():
    def __init__(self,height,weight,complexion,eye_color,waist_size):
        self.height = height
        self.weight = weight
        self.complexion = complexion
        self.eye_color = eye_color
        self.waist_size = waist_size

    def prob_height(self):
        print("Enter the sample data you want to use for height")
        user_sample = eval(input())
        mean_bar= []
        mean_bar_square = []
        sum_prob = []
        mean = sum(self.height)/(len(self.height))
        #create the mean-mean bar table
        for i in self.height:
            i = i - mean
        mean_bar.append(i)
        #create the mean-mean bar square table
        for u in mean_bar:
            u = u **2
        mean_bar_square.append(u)
        varianc = sum(mean_bar_square)/(len(self.height)-1)
        numerator = -(user_sample-mean)**2
        denom = (2*varianc)
        ex = math.exp(numerator/denom)
        probability = ex/(math.sqrt(2*math.pi*varianc))
        print ("mean of =",mean ,"\nvariance =", varianc, "\n probability of height = ",probability)
        return probability

    def prob_weight(self):
        print("Enter the sample data you want to use for weight")
        user_sample = eval(input())
        mean_bar= []
        mean_bar_square = []
        sum_prob = []
        mean = sum(self.weight)/(len(self.weight))
        for i in self.weight:
            i = i - mean
        mean_bar.append(i)
        for u in mean_bar:
            u = u **2
        mean_bar_square.append(u) 
        varianc = sum(mean_bar_square)/(len(self.weight)-1)
        numerator = -(user_sample-mean)**2
        denom = (2*varianc)
        ex = math.exp(numerator/denom)
        probability = ex/(math.sqrt(2*math.pi*varianc))
        print ("mean of =",mean ,"\nvariance =", varianc, "\n probability of weight = ",probability)
        return probability
    
    def prob_eye_color(self):
        print("Enter the sample data you want to use for eye_color")
        user_sample = eval(input())
        mean_bar= []
        mean_bar_square = []
        sum_prob = []
        mean = sum(self.eye_color)/(len(self.eye_color))
        for i in self.eye_color:
            i = i - mean
        mean_bar.append(i)
        for u in mean_bar:
            u = u **2
        mean_bar_square.append(u) 
        varianc = sum(mean_bar_square)/(len(self.eye_color)-1)
        numerator = -(user_sample-mean)**2
        denom = (2*varianc)
        ex = math.exp(numerator/denom)
        probability = ex/(math.sqrt(2*math.pi*varianc))
        print ("mean of =",mean ,"\nvariance =", varianc, "\n probability of prob_eye_color = ",probability)
        return probability
    
    def prob_complexion(self):
        print("Enter the sample data you want to use for complexion")
        user_sample = eval(input())
        mean_bar= []
        mean_bar_square = []
        sum_prob = []
        mean = sum(self.complexion)/(len(self.complexion))
        for i in self.complexion:
            i = i - mean
        mean_bar.append(i)
        for u in mean_bar:
            u = u **2
        mean_bar_square.append(u) 
        varianc = sum(mean_bar_square)/(len(self.complexion)-1)
        numerator = -(user_sample-mean)**2
        denom = (2*varianc)
        ex = math.exp(numerator/denom)
        probability = ex/(math.sqrt(2*math.pi*varianc))
        print ("mean of =",mean ,"\nvariance =", varianc, "\n probability of prob_complexion = ",probability)
        return probability
    
    def prob_waist_size(self):
        print("Enter the sample data you want to use for waist size")
        user_sample = eval(input())
        mean_bar= []
        mean_bar_square = []
        sum_prob = []
        mean = sum(self.waist_size)/(len(self.waist_size))
        for i in self.waist_size:
            i = i - mean
        mean_bar.append(i)
        for u in mean_bar:
            u = u **2
        mean_bar_square.append(u) 
        varianc = sum(mean_bar_square)/(len(self.waist_size)-1)
        numerator = -(user_sample-mean)**2
        denom = (2*varianc)
        ex = math.exp(numerator/denom)
        probability = ex/(math.sqrt(2*math.pi*varianc))
        print ("mean of =",mean ,"\nvariance =", varianc, "\n probability of waist_size = ",probability)
        return probability
    def posterior_numerator(self):
        post = self.prob_height() * self.prob_weight()* self.prob_eye_color() * self.prob_complexion() * self.prob_waist_size()
        print ("\nposterior _numerator = ", post)
        return post
        
    
                
           
          

            
        
        


        
 

