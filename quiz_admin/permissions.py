from rest_framework.permissions import BasePermission

class IsQuizCreator(BasePermission): 
    """
    Só admins (is_staff) podem criar quizze via POST
    """
    def has_permision(self, request, view): 
        if request.method == "POST": 
            return request.user.is_authenticated and request.user.is_staff
        return True