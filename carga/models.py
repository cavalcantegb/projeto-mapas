from django.db import models
from .types import account_type, location_type, edital_type
from unidecode import unidecode

# Create your models here.
class Project(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    description_short = models.CharField(max_length=1000, default="", blank=True, null=True)
    description_long = models.TextField(default="", blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)
    registration_from = models.DateTimeField(null=True, blank=True)
    registration_to = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    parent_entity = models.CharField(max_length=1000, default="", blank=True, null=True)
    published_by = models.CharField(max_length=1000, default="", blank=True, null=True)
    project_budget = models.TextField(default="", blank=True, null=True)
    project_goal = models.TextField(default="", blank=True, null=True)
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
        return "{} {} {}".format(self.code, self.name, self.description_short)


class Agent(models.Model):
    agent_identifier = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default="", blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    description_short = models.TextField(max_length=1000, default="", blank=True, null=True)
    description_long = models.TextField(max_length=10000, default="", blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    parent_entity = models.CharField(max_length=200, default="", blank=True, null=True)
    children_number =  models.IntegerField(default=0, blank=True, null=True)
    public_email = models.EmailField(max_length=200, default="", blank=True, null=True)
    phone = models.CharField(max_length=80, default="", blank=True, null=True)
    address = models.TextField(default="", blank=True, null=True)
    zip_code = models.CharField(max_length=100, default="", blank=True, null=True)
    state = models.CharField(max_length=100, default="", blank=True, null=True)
    neighbourhood = models.TextField(default="", blank=True, null=True)
    public_place = models.TextField(default="", blank=True, null=True)
    address_number = models.CharField(max_length=200, default="", blank=True, null=True)
    address_other_info = models.CharField(max_length=1000, default="", blank=True, null=True)
    fields_of_art = models.TextField(default="", blank=True, null=True)
    tags = models.TextField(default="", blank=True, null=True)
    verified_account = models.BooleanField(default=False)
    account_type = models.CharField(max_length=60, choices=account_type, blank=True, null=True)
    social_name = models.CharField(max_length=200, default="", blank=True, null=True)
    work_name = models.CharField(max_length=200, default="", blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=60, default="", blank=True, null=True)
    ethnic_type = models.CharField(max_length=60, default="", blank=True, null=True)
    sexual_orientation = models.CharField(max_length=40, default="", blank=True, null=True)
    civil_status = models.CharField(max_length=200, default="", blank=True, null=True)
    studies = models.CharField(max_length=200, default="", blank=True, null=True)
    cpf = models.CharField(max_length=20, default="", blank=True, null=True)
    rg = models.CharField(max_length=20, default="", blank=True, null=True)
    rg_date = models.DateTimeField(null=True, blank=True)
    rg_orgao_expedidor = models.CharField(max_length=20, default="", blank=True, null=True)
    nationality = models.CharField(max_length=60, default="", blank=True, null=True)
    natural_from = models.CharField(max_length=60, default="", blank=True, null=True)
    has_disability = models.BooleanField(default=False, blank=True, null=True)
    disability = models.CharField(max_length=200, default="", blank=True, null=True)
    main_email = models.EmailField(max_length=200, default="", blank=True, null=True)
    cell_phone = models.CharField(max_length=80, default="", blank=True, null=True)
    location = models.CharField(max_length=200, default="", blank=True, null=True)
    website = models.URLField(max_length=1000, default="", blank=True, null=True)
    has_website = models.BooleanField(default=False, blank=True, null=True)
    facebook = models.URLField(max_length=1000, default="", blank=True, null=True)
    has_facebook = models.BooleanField(default=False, blank=True, null=True)
    twitter = models.CharField(max_length=1000, default="", blank=True, null=True)
    has_twitter = models.BooleanField(default=False, blank=True, null=True)
    google_plus = models.CharField(max_length=1000, default="", blank=True, null=True)
    has_google_plus = models.BooleanField(default=False, blank=True, null=True)
    instagram = models.CharField(max_length=1000, default="", blank=True, null=True)
    has_instagram = models.BooleanField(default=False, blank=True, null=True)
    company_name = models.CharField(max_length=500, default="", blank=True, null=True)
    cnpj = models.CharField(max_length=30, default="", blank=True, null=True)
    main_activity = models.CharField(max_length=80, default="", blank=True, null=True)
    corporate_name = models.CharField(max_length=500, default="", blank=True, null=True)
    foundation = models.DateTimeField(null=True, blank=True)
    codigo_natureza_juridica = models.CharField(max_length=30, default="", blank=True, null=True)
    mesoregion = models.CharField(max_length=80, default="", blank=True, null=True)
    microregion = models.CharField(max_length=80, default="", blank=True, null=True)
    city = models.CharField(max_length=80, default="", blank=True, null=True)
    opportunity_tab_name = models.CharField(max_length=1000, default="", blank=True, null=True)
    use_opportunity_tab = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.website is not None:
            self.has_website = True
        if self.facebook is not None:
            self.has_facebook = True
        if self.twitter is not None:
            self.has_twitter = True
        if self.google_plus is not None:
            self.has_google_plus = True
        if self.instagram is not None:
            self.has_instagram = True
        if self.name is not None:
            self.name = unidecode(self.name.upper().strip())
        if self.city is not None:
            self.city = unidecode(self.city.upper().strip())
        if self.state is not None:
            self.state = unidecode(self.state.upper().strip())
        if self.neighbourhood is not None:
            self.neighbourhood = unidecode(self.neighbourhood.upper().strip())
        super(Agent, self).save(*args, **kwargs)


    def __str__(self):
        return "{} {} {}".format(self.agent_identifier, self.name, self.description_short)


class AgentData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, default="", blank=True, null=True)
    createTimestamp = models.DateTimeField()
    updateTimestamp = models.DateTimeField()
    parent = models.IntegerField()
    geoMunicipio = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return "{} {}, {}, {}.".format(self.id, self.name, self.createTimestamp)

class Edital(models.Model):
    number = models.IntegerField()
    subscription_number = models.CharField(max_length=80, default="", blank=True, null=True)
    project_name = models.TextField()
    user_name = models.TextField()
    points = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    status = models.CharField(max_length=40, default="", blank=True, null=True)
    location_type = models.CharField(max_length=60, choices=location_type, blank=True, null=True)
    city = models.CharField(max_length=200, default="", blank=True, null=True)
    neighbourhood = models.CharField(max_length=200, default="", blank=True, null=True)
    edital_type = models.CharField(max_length=80, default="",choices=edital_type, blank=True, null=True)

class Bairro(models.Model):
    name = models.CharField(max_length=100, default="", blank=True, null=True)
    idh = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)