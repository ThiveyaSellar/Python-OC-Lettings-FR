Description of Programming Interfaces
=====================================

Below are the main URLs of the application, all accessible via the GET method:

- `/` : Home page presenting an introduction or summary of the features.
- `/lettings/` : List of available rental properties.
- `/lettings/<int:letting_id>/` : Detail of a specific property identified by its integer ID `letting_id`.
- `/profiles/` : List of user profiles.
- `/profiles/<str:username>/` : Detail of the user profile corresponding to the username `username`.
- `/admin/` : Django administration interface (accessible only to authorized users).