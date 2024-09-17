# Question 3: By default, do Django signals run in the same database transaction as the caller?
# Answer: Yes, by default, Django signals run in the same database transaction as the caller. This is particularly true for signals like post_save and post_delete, which are emitted after the transaction completes successfully.


# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    if created:
        if transaction.get_connection().in_atomic_block:
            print("Inside a transaction")
        else:
            print("Not in a transaction")

# views.py
from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    with transaction.atomic():
        user = User.objects.create(username="test_user")
        print("User created inside transaction.")
    return HttpResponse("User created successfully!")


# When create_user is called, the signal handler will print "Inside a transaction" because both the view and the signal handler are executed within the same transaction block.
