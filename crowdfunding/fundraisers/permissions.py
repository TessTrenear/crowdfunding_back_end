from rest_framework import permissions #responsible for all permissions. Build on top of default permissions logic

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user #PUT, PATCH, POST, DELETE > confirm if user is the owner. == VS =; = (assignment > overwrite the value), ==(comparison > are they the same?). #created own custom permission class to use
    
    #PROJECT = once someone has pledged > can they update pledge OR delete and then resumbit pledge?