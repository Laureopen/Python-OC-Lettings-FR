from django.db import migrations

def transfer_data_forward(apps, schema_editor):
    # Récupérer les modèles
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    # Transférer les profils
    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
        id=old_profile.id,
        user_id=old_profile.user_id,
        favorite_city=old_profile.favorite_city,
        )

def transfer_data_reverse(apps, schema_editor):
    # Récupérer les modèles
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    # Transférer en sens inverse
    for new_profile in NewProfile.objects.all():
        OldProfile.objects.create(
        id=new_profile.id,
        user_id=new_profile.user_id,
        favorite_city=new_profile.favorite_city,
        )

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(transfer_data_forward, transfer_data_reverse),
    ]