# signals.py

import time
import threading
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import IntegrityError

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
    
    if instance.username == "rollback":
        raise IntegrityError("Forcing rollback inside signal.")
    
    time.sleep(5)
    print("Signal processed after delay.")
