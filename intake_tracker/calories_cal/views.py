from django.shortcuts import render, redirect
from .models import CaloriesIntake
from .forms import CalorieIntakeForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import DietPlanForm
from .models import DietPlan

def log_calorie_intake(request):
    today = timezone.now().date()
    calorie_intake = CaloriesIntake.objects.first()  # Fetches the first instance

    # if calorie_intake:
    #     print(calorie_intake)  # Prints the instance
    #     print(calorie_intake._meta)  # Accesses model metadata (if needed, for instance)

    # calorie_intake = CaloriesIntake.objects.all()
#     calorie_intake = CaloriesIntake.objects.all()

# # Iterate over each instance in the QuerySet and print the object or its fields
#     for intake in calorie_intake:
#         print(intake)  # This prints the __str__() representation of each object
#         print(intake.protein, intake.carbs, intake.fats, intake.fibers)  # Prints individual field values

    
    print(calorie_intake)

    # print(calorie_intake ,calorie_intake.protein)
    
    if request.method == "POST":
        form = CalorieIntakeForm(request.POST, instance=calorie_intake)
        if form.is_valid():  # Ensure form validation
            form.save()
            return redirect('calories_progress')
        else:
            print(form.errors)  # Print errors if form is invalid (for debugging)
    else:
        form = CalorieIntakeForm(instance=calorie_intake)

    return render(request, 'calorie_intake.html', {'form': form})


def calories_progress(request):
    today = timezone.now().date()
    print(today)
    calorie_intake = CaloriesIntake.objects.first()
    print("-----------",calorie_intake.protein)
    
    # if calorie_intake:
    #     protein_percentage = (calorie_intake.protein / calorie_intake.protein_goal) * 100
    #     print(protein_percentage)
    #     carbs_percentage = (calorie_intake.carbs/ calorie_intake.carbs_goal) * 100
    # else:
    #     percentage = 0

    # return render(request, 'calories_progress.html', {'protien_percentage': protein_percentage, 'carbs_percentage':carbs_percentage,'calorie_intake': calorie_intake})
    if calorie_intake:
        protien_percentage = (calorie_intake.protein / calorie_intake.protein_goal) * 100
        percentage_rounded = round(protien_percentage, 2)
        print(protien_percentage)
        carbs_percentage = (calorie_intake.carbs/ calorie_intake.carbs_goal) * 100
        fat_percentage = (calorie_intake.fats / calorie_intake.fats_goal) * 100
        fibers_percentage = (calorie_intake.fibers / calorie_intake.fibers_goal) * 100
    else:
        percentage = 0

    return render(request, 'calories_progress.html', 
                  {'protien_percentage': percentage_rounded,
                   'carbs_percentage':carbs_percentage,
                   'fat_percentage':fat_percentage,
                   'fibers_percentage':fibers_percentage,
                   'calorie_intake': calorie_intake})


def index(request):
    return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         usernumber = request.POST['usernumber']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2= request.POST['pass2']

#         try:
#             user = User.objects.create_user(usernumber=usernumber, email=email, pass1=pass1, pass2=pass2)
#             print(user)
#             user.save()
#             messages.success(request, 'Signup successful! You can now log in.')
#             return redirect('login')  # Redirect to login page or another page
#         except Exception as e:
#             messages.error(request, f'Error: {e}')
        
#     return render(request, 'signup.html')




def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/handlelogin')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        password=request.POST.get('pass1')
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect('/index')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/handlelogin')
        
    return render(request, 'handlelogin.html')



def handlelogout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('/index')



# views.py



def calculate_diet_plan(weight, height, age, gender, activity_level):
    # Calculate BMR
    if gender == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    # Activity level multiplier
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'extra': 1.9,
    }

    # Calculate calories based on activity level
    calories = bmr * activity_multipliers[activity_level]

    # Macronutrient calculations
    proteins = weight * 1.8  # 1.8g per kg of body weight
    carbs = (calories - (proteins * 4)) * 0.55 / 4
    fats = (calories - (proteins * 4) - (carbs * 4)) / 9

    # Water and fiber intake calculation
    water = weight * 0.035  # 35 ml per kg of body weight
    fibers = weight * 0.03  # 30 grams per kg (example)

    return calories, proteins, carbs, fats, fibers, water

def diet_plan_view(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        print("-----------------------")
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            activity_level = form.cleaned_data['activity_level']

            # Calculate diet details
            calories, proteins, carbs, fats, fibers, water = calculate_diet_plan(
                weight, height, age, gender, activity_level
            )

            # Save to the database
            diet_plan = form.save(commit=False)
            diet_plan.user = request.user
            diet_plan.calories = calories
            diet_plan.proteins = proteins
            diet_plan.carbs = carbs
            diet_plan.fats = fats
            diet_plan.fibers = fibers
            diet_plan.water = water
            diet_plan.save()

            # Redirect to a results page or render the result
            return render(request, 'index1.html', {
                'form': form,
                'calories': calories,
                'proteins': proteins,
                'carbs': carbs,
                'fats': fats,
                'fibers': fibers,
                'water': water,
            })
    else:
        form = DietPlanForm()

    return render(request, 'index1.html', {'form': form})

