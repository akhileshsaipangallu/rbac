# Role Based Access Control

The feature comes out of the box in django. Django creates user, permissions, role(group) and mapping tables for each other.

By default django creates a table `django_content_type`. This table has `app_label` and `model` as two columns, which basically represents the table.
The `auth_permission` table has a `content_type_id` as FK and `codename` which is basically `read`, `write`, `delete` or `update`.

Django provides in-built functions with which we can determine permission for a given/requesting user.

This project has an admin panel where you can `create`/`update`/`delete` groups or users and assign it with permissions. I have created a `Task` model to which you can assign `read`, `write`, `delete` or/and `update` permission for a `user`/`role`.    

**Important files:**
1. [Task Table](task/models.py)
1. [Task Table admin panel registration](task/admin.py)

