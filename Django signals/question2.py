# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, by default, Django signals run in the same thread as the caller.


# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Signal thread: {threading.current_thread().name}")
        
# views.py
import threading
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    print(f"View thread: {threading.current_thread().name}")
    user = User.objects.create(username="test_user")
    return HttpResponse("User created successfully!")


# When you access the create_user view, you will see that both the view and the signal handler print the same thread name, confirming that they run in the same thread.