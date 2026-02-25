import httpx
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.conf import settings


class AsyncProxyView(View):

    async def get(self, request):
        target_url = request.GET.get("url")

        if not target_url:
            return JsonResponse({"error": "Missing url parameter"}, status=400)

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(target_url)

            return HttpResponse(
                content=response.content,
                status=response.status_code,
                content_type=response.headers.get("content-type"),
            )

        except httpx.RequestError as exc:
            return JsonResponse(
                {"error": f"Request failed: {str(exc)}"},
                status=502
            )