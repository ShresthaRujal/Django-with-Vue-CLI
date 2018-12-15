from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """permission for users to edit their own profile."""

    def has_object_permission(self,request,view,obj):
        """this function will be called in evry request in the api. 
        This checks if user has or does not has a permission to perform a action."""

        ##SAFE_METHODS is http method that is safe, non-destrictive(GET method)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        ##if method is not safe methods, check if the request is making changes to their own profile
        return obj.id == request.user.id
