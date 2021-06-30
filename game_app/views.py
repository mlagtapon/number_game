from django.shortcuts import render, random
def index(request):
    return render(request,'index.html')

def guessedNum(request):
    num_from_form = request.POST[int('num')]
    num = num_from_form
    randomNum = random.randint(1, 100)

    if randomNum == num:  
        print(num, " was the number!")
    if randomNum > num:
        print("Too low!")
    if randomNum < num:
        print("Too high!")

    context = {
        'random': randomNum,
        'num': num
    }

    return render(request, "index.html", context)