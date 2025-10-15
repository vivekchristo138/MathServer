# Ex.05 Design a Website for Server Side Processing
## Date:08/10/2025

## AIM:
 To design a website to calculate to the body mass index(BMI) in the server side. 


## FORMULA:
BMI=w/h<sup>2</sup>
<br> BMI -->Body Mass Index
<br> w --> weight
<br> h --> height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
bmi.html



<html>

<head>
    <title>BMI-CALCULATOR</title>

    <style>
        body {
            background: linear-gradient(135deg, #e0f7fa, #80deea);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .edge {
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .box {
            background-color: #ffffff;
            padding: 30px 40px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 350px;
        }

        h1 {
            color: #00796b;
            margin-bottom: 20px;
            font-size: 24px;
        }

        .formelt {
            margin: 10px 0;
        }

        input[type="text"] {
            padding: 8px;
            width: 60%;
            border: 1px solid #ccc;
            border-radius: 6px;
            margin-left: 5px;
        }

        input[type="submit"] {
            background-color: #00796b;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #004d40;
        }

        .formelt label {
            font-weight: bold;
            color: #333;
        }
    </style>
</head>

<body>
    
    <div class="edge">
        <div class="box">
            <h1 bgcolor="lime">BMI-CALCULATOR</h1>
            <h1>Vivek christo A</h1>
            <h3>   25013444    </h3>
            <form method="POST">
                {%csrf_token %}
                <div class="formelt">
                    weight:<input type="text" name="weight" value="{{w}}"></input>(in kg)<br />
                </div>
                <div class="formelt">
                    height:<input type="text" name="height" value="{{h}}"></input>(in cm)<br />
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input><br />
                </div>
                <div class="formelt">
                    bmi:<input type="text" name="bmi" value="{{bmi}}"></input><br />
                </div>
            </form>
        </div>
    </div>
</body>
</html>

urls.py

from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('calculate_bmi/',views.calculate_bmi,name="calculate_bmi"),
    path('',views.calculate_bmi,name="calculate_bmi")
]

views.py

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

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (56).png>)


## HOMEPAGE:
![alt text](<Screenshot (57).png>)



## RESULT:
The program for performing server side processing is completed successfully.
