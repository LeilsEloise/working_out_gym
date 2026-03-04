from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

# Create your views here.
#ChatGPT Code
def home(request):

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)

            if request.user.is_authenticated:
                feedback.user = request.user

            feedback.save()

            messages.success(request, "Thanks! Your feedback has been sent.")

            return redirect("home")

        else:
            messages.error(request, "Please correct the errors in the form and try again.")

    else:
        form = FeedbackForm()

    return render(request, "home/index.html", {"feedback_form": form})