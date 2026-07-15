from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    """
    Yalnız 'Manager' qrupuna daxil olan istifadəçilərə icazə verir.
    """
    def has_permission(self, request, view):
        # İstifadəçi giriş edibsə və hər hansı bir qrupa daxildirsə
        if request.user and request.user.is_authenticated:
            # İstifadəçinin qruplarının içində 'Manager' adı varmı?
            return request.user.groups.filter(name='Manager').exists() or request.user.is_superuser
        return False