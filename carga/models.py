from django.db import models

# Create your models here.
class Project(models.Model):
    id_project = models.UniqueConstraint
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    description_short = models.CharField(max_length=1000, default="", blank=True, null=True)
    description_long = models.CharField(max_length=1000, default="", blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    registration_from = models.DateTimeField(null=True, blank=True)
    registration_to = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    parent_entity = models.CharField(max_length=1000, default="", blank=True, null=True)
    published_by = models.CharField(max_length=1000, default="", blank=True, null=True)
    project_budget = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    project_goal = models.CharField(max_length=1000, default="", blank=True, null=True)
    target_audience = models.CharField(max_length=1000, default="", blank=True, null=True)
    areas = models.CharField(max_length=1000, default="", blank=True, null=True)
    tags = models.CharField(max_length=1000, default="", blank=True, null=True)
    verified_account = models.BooleanField(default=False)
    project_type = models.CharField(max_length=1000, default="", blank=True, null=True)
    project_website = models.URLField(max_length=1000, default="", blank=True, null=True)
    project_facebook = models.URLField(max_length=1000, default="", blank=True, null=True)
    project_twitter = models.CharField(max_length=1000, default="", blank=True, null=True)
    project_google_plus = models.CharField(max_length=1000, default="", blank=True, null=True)
    project_instagram = models.CharField(max_length=1000, default="", blank=True, null=True)
    stamps = models.CharField(max_length=1000, default="", blank=True, null=True)
    opportunity_tab_name = models.CharField(max_length=1000, default="", blank=True, null=True)
    use_opportunity_tab = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {}".format(self.id_project, self.name, self.description_short)