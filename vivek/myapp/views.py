from django.shortcuts import render 
def calculate_bmi(request): 
    context={} 
    context['bmi'] = "0" 
    context['w'] = "0" 
    context['h'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        w = request.POST.get('weight','0')
        h = request.POST.get('height','0')
        print('request=',request) 
        print('weight=',w) 
        print('height=',h) 
        bmi = round(int(w)/((int(h)/100)**2),2)
        context['bmi'] = bmi 
        context['w'] = w
        context['h'] = h 
        print('bmi=',bmi) 
    return render(request,'myapp/bmi.html',context)

