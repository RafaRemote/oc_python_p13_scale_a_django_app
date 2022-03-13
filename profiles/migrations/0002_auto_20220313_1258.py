from django.db import migrations

def move_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    objs = list()


    for old_object in OldProfile.objects.all():
        old_favorite_city = old_object.favorite_city
        old_user_id = old_object.user_id

        new_profile = NewProfile(
            favorite_city = old_favorite_city, 
            user_id = old_user_id
            )
        objs.append(new_profile)

    NewProfile.objects.bulk_create(objs)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('lettings', '0002_auto_20220313_1215')
    ]
    
    run_before = [
        ('oc_lettings_site', '0003_delete_profile'),
    ]
    

    operations = [
        migrations.RunPython(move_profiles, migrations.RunPython.noop),
    ]
