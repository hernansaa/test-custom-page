from unfold.sites import UnfoldAdminSite

class NewUnfoldAdminSite(UnfoldAdminSite):
    pass

# You can route to new admin by "gs-admin:index"
new_admin_site = NewUnfoldAdminSite(name="gs-admin")