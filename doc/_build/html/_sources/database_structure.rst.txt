==============================
Database Structure and Data Models
==============================

The core data handled by the application is organized through three main models.
These models represent the fundamental entities for the system: properties available for rent, their addresses, and user profiles.
Using Django’s ORM, these models define the structure and relationships of the data stored in the database.
For this project, the application uses SQLite as a database.

There are three models:
- Address and Letting in the ``lettings`` app.
- Profile in the ``profiles`` app.

Address Model
=============

Represents the address of a property.

Fields
------

- **number**: The street number
- **street**: The name of the street
- **city**: The city
- **state**: The state
- **country_iso_code**: The country ISO code (International Standard for Country Codes)

Letting Model
=============

Represents a property for rent.

Fields
------

- **title**: The name of the property
- **address**: A foreign key linking to the ``Address`` model

Profile Model
=============

Extends Django’s ``User`` model.

Fields
------

- **user**: One-to-one link to Django ``User``
- **favorite_city**: A user's favorite city
