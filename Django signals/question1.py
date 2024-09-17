# Question 1: By default, are Django signals executed synchronously or asynchronously?
# Answer: By default, Django signals are executed synchronously. This means that the signal handlers are called immediately within the same thread and process as the event that triggered them.
# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    if created:
        print("Signal received. Processing...")
        time.sleep(5)  # Simulating a delay in signal handling
        print("Signal processed!")

# views.py
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_user(request):
    user = User.objects.create(username="test_user")
    return HttpResponse("User created successfully!")


# When you access the create_user view, you will notice that the response is delayed by 5 seconds due to the time.sleep(5) call in the signal handler.
# This indicates that the signal is executed synchronously.