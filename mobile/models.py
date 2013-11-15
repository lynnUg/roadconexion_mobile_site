from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin)
 
from django.db import models
# Create your models here.
TYPE_CHOICES=(
('Accident','Accident'),
('Traffic_Jam','Traffic_Jam'),
('Repair','Repair'),
('Status','Status'),

)
class myUserManager(BaseUserManager):
    def create_user(self, email,password, **extra_fields):
        now = datetime.now()
        user = self.model(email=email,is_active=True,is_staff=False,last_login=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password,**extra_fields):
        u= self.create_user(email,password,**extra_fields)
        u.is_staff= True
        u.is_active= True
        u.is_superuser=True
        u.save(using=self._db)
        return u
class myUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True)
    
    USERNAME_FIELD = 'email'
   
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    def get_full_name(self):
        full_name = '%s %s' % (self.email)
        return full_name.strip()
 
    def get_short_name(self):
        return self.email
 
    objects = myUserManager()

class Report(models.Model):
    road_name = models.CharField(max_length=128, unique=True)
    report= models.TextField(blank=False)
    type_report=models.CharField(max_length=200,choices=TYPE_CHOICES,blank=False)
    user = models.ForeignKey(myUser)
    def __unicode__(self):
        return self.road_name