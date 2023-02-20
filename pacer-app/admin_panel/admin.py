from django.contrib import admin

class PacerAdminSite(admin.AdminSite):
    site_header = "Pacer Administration"

admin_site = PacerAdminSite(name="pacer_admin")