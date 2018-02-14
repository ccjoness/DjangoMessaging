from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)


class Cast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cast_assignments', blank=True, null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='cast_members')
    title = models.CharField(max_length=255)


class Crew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crew_assignments', blank=True, null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='crew_members')
    title = models.CharField(max_length=255)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='messages')
    cast = models.ForeignKey('Cast', on_delete=models.CASCADE, related_name='potential_cast', blank=True, null=True)
    crew = models.ForeignKey('Crew', on_delete=models.CASCADE, related_name='potential_crew', blank=True, null=True)
    body = models.TextField()
    read = models.BooleanField(default=False)

    def return_cast_or_crew(self):
        if not self.crew:
            return self.cast
        return self.crew