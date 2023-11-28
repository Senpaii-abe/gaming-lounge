from account.models import UserVisit
from datetime import date


class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Get the path of the visited page
        visited_path = request.path

        # Check if the visited path is one of the pages you want to track
        if visited_path in [
            "/",
            "/marketplace_posts/",
            "/connect_posts/",
            "/tournament_posts/",
        ]:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Get or create a UserVisit object for the user and visited page
                user_visit, created = UserVisit.objects.get_or_create(
                    user=request.user, visited_page=visited_path
                )

        return response
