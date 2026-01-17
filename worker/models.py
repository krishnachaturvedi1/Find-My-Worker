from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.

UP_CITIES = (
    ("Agra", "Agra"),
    ("Aligarh", "Aligarh"),
    ("Allahabad (Prayagraj)", "Allahabad (Prayagraj)"),
    ("Ambedkar Nagar", "Ambedkar Nagar"),
    ("Amethi", "Amethi"),
    ("Amroha", "Amroha"),
    ("Auraiya", "Auraiya"),
    ("Azamgarh", "Azamgarh"),
    ("Badaun", "Badaun"),
    ("Baghpat", "Baghpat"),
    ("Bahraich", "Bahraich"),
    ("Ballia", "Ballia"),
    ("Balrampur", "Balrampur"),
    ("Banda", "Banda"),
    ("Barabanki", "Barabanki"),
    ("Bareilly", "Bareilly"),
    ("Basti", "Basti"),
    ("Bhadohi (Sant Ravidas Nagar)", "Bhadohi (Sant Ravidas Nagar)"),
    ("Bijnor", "Bijnor"),
    ("Bulandshahr", "Bulandshahr"),
    ("Chandauli", "Chandauli"),
    ("Chitrakoot", "Chitrakoot"),
    ("Deoria", "Deoria"),
    ("Etah", "Etah"),
    ("Etawah", "Etawah"),
    ("Faizabad (Ayodhya)", "Faizabad (Ayodhya)"),
    ("Farrukhabad", "Farrukhabad"),
    ("Fatehpur", "Fatehpur"),
    ("Firozabad", "Firozabad"),
    ("Gautam Buddha Nagar (Noida)", "Gautam Buddha Nagar (Noida)"),
    ("Ghaziabad", "Ghaziabad"),
    ("Ghazipur", "Ghazipur"),
    ("Gonda", "Gonda"),
    ("Gorakhpur", "Gorakhpur"),
    ("Hamirpur", "Hamirpur"),
    ("Hapur", "Hapur"),
    ("Hardoi", "Hardoi"),
    ("Hathras", "Hathras"),
    ("Jalaun", "Jalaun"),
    ("Jaunpur", "Jaunpur"),
    ("Jhansi", "Jhansi"),
    ("Kannauj", "Kannauj"),
    ("Kanpur", "Kanpur"),
    ("Kasganj", "Kasganj"),
    ("Kaushambi", "Kaushambi"),
    ("Kushinagar", "Kushinagar"),
    ("Lakhimpur Kheri", "Lakhimpur Kheri"),
    ("Lalitpur", "Lalitpur"),
    ("Lucknow", "Lucknow"),
    ("Maharajganj", "Maharajganj"),
    ("Mahoba", "Mahoba"),
    ("Mainpuri", "Mainpuri"),
    ("Mathura", "Mathura"),
    ("Mau", "Mau"),
    ("Meerut", "Meerut"),
    ("Mirzapur", "Mirzapur"),
    ("Moradabad", "Moradabad"),
    ("Muzaffarnagar", "Muzaffarnagar"),
    ("Pilibhit", "Pilibhit"),
    ("Pratapgarh", "Pratapgarh"),
    ("Raebareli", "Raebareli"),
    ("Rampur", "Rampur"),
    ("Saharanpur", "Saharanpur"),
    ("Sambhal", "Sambhal"),
    ("Sant Kabir Nagar", "Sant Kabir Nagar"),
    ("Shahjahanpur", "Shahjahanpur"),
    ("Shamli", "Shamli"),
    ("Shravasti", "Shravasti"),
    ("Siddharthnagar", "Siddharthnagar"),
    ("Sitapur", "Sitapur"),
    ("Sonbhadra", "Sonbhadra"),
    ("Sultanpur", "Sultanpur"),
    ("Unnao", "Unnao"),
    ("Varanasi", "Varanasi"),
)

class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)  # e.g., plumber, electrician
    city = models.CharField(max_length=100, choices= UP_CITIES)
    landmark = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6, validators=[RegexValidator(regex=r'^\d{6}$', message="Pincode must be 6 digits.", code='invalid_pincode')])
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message="Contact number must be 10 digits.", code='invalid_contact_number')])
    experience = models.IntegerField()  # Years of experience
    availability = models.BooleanField(default=True)
    job_description = models.TextField(max_length=240) 
    photo = models.ImageField(upload_to='photos', blank=True, null=True, default='photos/Untitled.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
