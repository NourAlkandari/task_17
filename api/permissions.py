from rest_framework.permissions import BasePermission
class IsOwner(BasePermission):

	message = "only owner or staff can update the artical"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.owner == request.user):
			return True
		else:
			return False
