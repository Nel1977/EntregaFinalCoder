from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

# crear object manager
class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

    objects = ThreadManager()

# definimos una señal
def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None) # hilo al que estamos intentando añadir mensajes
    action = kwargs.pop("action", None) # acción que se está ejecutando
    pk_set = kwargs.pop("pk_set", None) # conjunto que almacena los identificadores de los mensajes
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print(f"Ups, ({msg.user}) no forma parte del hilo")
                false_pk_set.add(msg_pk)

    # buscar los mensajes de false_pk_set que están en pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set) # difference_update es un método de los conjuntos resta lo que está entre()

# conectamos la señal con cualquier cambio en el campo ManyToMany messages del modelo Thread
m2m_changed.connect(messages_changed, sender=Thread.messages.through)