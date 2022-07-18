# Generated by Django 4.0.6 on 2022-07-18 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('props', '0005_remove_furnituresinrooms_furnituresid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furnitures',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('furniture', models.TextField(blank=True, db_column='Furniture', null=True)),
            ],
            options={
                'db_table': 'Furnitures',
            },
        ),
        migrations.CreateModel(
            name='Furnituresinrooms',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('furnituresid', models.ForeignKey(db_column='FurnituresId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.furnitures')),
            ],
            options={
                'db_table': 'FurnituresInRooms',
            },
        ),
        migrations.CreateModel(
            name='Roomtypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('types', models.TextField(blank=True, db_column='Types', null=True)),
            ],
            options={
                'db_table': 'RoomTypes',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('roomtitle', models.TextField(blank=True, db_column='RoomTitle', null=True)),
                ('propertiesid', models.ForeignKey(db_column='PropertiesId', on_delete=django.db.models.deletion.DO_NOTHING, to='props.properties')),
                ('roomtypesid', models.ForeignKey(db_column='RoomTypesId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.roomtypes')),
            ],
            options={
                'db_table': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Roompictures',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('url', models.TextField(blank=True, db_column='URL', null=True)),
                ('roomsid', models.ForeignKey(db_column='RoomsId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.rooms')),
            ],
            options={
                'db_table': 'RoomPictures',
            },
        ),
        migrations.CreateModel(
            name='Furnituresinroomspictures',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('regdate', models.DateField(blank=True, db_column='RegDate', null=True)),
                ('url', models.TextField(blank=True, db_column='URL', null=True)),
                ('furnituresinroomsid', models.ForeignKey(db_column='FurnituresInRoomsId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.furnituresinrooms')),
            ],
            options={
                'db_table': 'FurnituresInRoomsPictures',
            },
        ),
        migrations.AddField(
            model_name='furnituresinrooms',
            name='roomsid',
            field=models.ForeignKey(db_column='RoomsId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.rooms'),
        ),
        migrations.AddField(
            model_name='furnitures',
            name='roomtypesid',
            field=models.ForeignKey(db_column='RoomTypesId', on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.roomtypes'),
        ),
    ]
