from django.shortcuts import render

# Create your views here.


def show_user_info(request):
    """
    A django view to show user's Information
    """
    print("request type: ", request.method)
    print("request data", request.POST)
    if request.method == 'POST':
        user_name_value = request.POST["user_name"]
        print("Your name is: ", user_name_value)

        context = {"name": user_name_value}
        return render(request, 'user_info/user_info.html', context)
    return render(request, 'user_info/user_info.html')

