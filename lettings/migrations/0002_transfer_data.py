from django.db import migrations

def transfer_data_forward(apps, schema_editor):
    # Récupérer les anciens modèles
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')

    # Récupérer les nouveaux modèles
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Transférer les adresses
    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    # Transférer les lettings
    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id,
        )

def transfer_data_reverse(apps, schema_editor):
# Récupérer les modèles
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Transférer les données en sens inverse
    for new_address in NewAddress.objects.all():
        OldAddress.objects.create(
            id=new_address.id,
            number=new_address.number,
            street=new_address.street,
            city=new_address.city,
            state=new_address.state,
            zip_code=new_address.zip_code,
            country_iso_code=new_address.country_iso_code,
        )

    for new_letting in NewLetting.objects.all():
        OldLetting.objects.create(
            id=new_letting.id,
            title=new_letting.title,
            address_id=new_letting.address_id,
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings','0001_initial'),
        ('oc_lettings_site','0001_initial'),

    ]

    operations = [
        migrations.RunPython(transfer_data_forward, transfer_data_reverse),
    ]
