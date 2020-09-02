from django.db import models

# Create your models here.
class Project(models.Model):
    id_project = models.UniqueConstraint
    name = models.CharField(max_length=1000)
    description_short = models.CharField(max_length=500)
    description_long = models.CharField
    registration_from = models.DateTimeField()
    registration_to = models.DateTimeField()
    created_at = models.DateTimeField()
    parent_entity = models.CharField(max_length=500)
    published_by = models.CharField(max_length=500)
    project_budget = models.DecimalField(max_digits=6, decimal_places=2)
    project_goal = models.CharField
    target_audience = models.CharField
    areas = models.CharField
    tags = models.CharField
    verified_account = models.BooleanField(default=False)
    project_type = models.CharField
    project_website = models.URLField
    project_facebook = models.URLField
    project_twitter = models.CharField
    project_google_plus = models.CharField
    project_instagram = models.CharField
    stamps = models.CharField
    opportunity_tab_name = models.CharField
    use_opportunity_tab = models.BooleanField(default=False)