from datetime import datetime
from .models import UserPageVisit  # Replace with your actual model


class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            page_visited = request.path  # Get the visited page URL
            user = request.user

            # Check if the user visited a specific page
            if page_visited in [
                "/discussions/",
                "/tournament/",
                "/marketplace/",
                "/connect/",
                "/beta-testing/",
            ]:
                # Log the user visit to the page in your database
                UserPageVisit.objects.create(
                    user=user, page_visited=page_visited, visit_timestamp=datetime.now()
                )

        return response
