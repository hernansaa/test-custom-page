from unfold.sites import UnfoldAdminSite

class NewUnfoldAdminSite(UnfoldAdminSite):
    pass

# You can route to new admin by "original-name-here-not-admin:index"
new_admin_site = NewUnfoldAdminSite(name="original-name-here-not-admin")