from django.db import models

# Create your models here.
# models.py

import time
import threading
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import transaction, IntegrityError

# Receiver function for the post_save signal
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
    
    # Simulate delay to showcase synchronous behavior
    if instance.username == "rollback":
        raise IntegrityError("Forcing rollback inside signal.")
    
    time.sleep(5)  # Simulating a long-running task
    print("Signal processed after delay.")


# Simulate saving a user instance inside a transaction
def save_user():
    try:
        with transaction.atomic():
            print(f"Saving user in thread: {threading.current_thread().name}")
            user = User.objects.create(username="rollback")  # Change this username for testing
            print("User saved. Committing transaction...")
    except IntegrityError:
        print("Transaction rolled back due to error in signal.")
