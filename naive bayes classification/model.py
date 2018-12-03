import sample_data
height_m = [5.85,5.75,5.6,6.2,6.0]
weight_m = [60,61,58,73,75]
complexion_m = [6,6,8,7,9]
eye_color_m = [6,5.92,5.58,5.92]
Waist_size_m = [30,28,30,32,31]
height_f = [5.3,5.5,5.7,5.4]
weigth_f = [50,58,65,55]
complexion_f = [5,3,52,2]
eye_color_f = [7,5,7,4,4]
Waist_size_f = [27,25,30,20]

#boys and girls instace of the sample_data module
boys = sample_data.Probability(height_m,weight_m,complexion_m,eye_color_m,Waist_size_m)
girls = sample_data.Probability(height_f,weight_m,complexion_f,eye_color_f,Waist_size_f)


x = boys.posterior_numerator()
y = girls.posterior_numerator()
evidence = x+y
print("\n\evidence = ", evidence)
posterior_boys = x/evidence
posterior_girls = y/evidence
print("\nposterior_boys = ",posterior_boys)
print("\nposterior_girls = ",posterior_girls)
if (y>x):
    print("\nthe Sample model is a girl")
else:
    print("\nthe sample model is a boy")

