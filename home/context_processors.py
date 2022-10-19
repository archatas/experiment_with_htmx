def login_dialog(request):
    from .forms import LoginForm

    if not request.user.is_authenticated:
        form = LoginForm(request=request)
        if hasattr(request, "combined_media"):
            request.combined_media += form.media
        else:
            request.combined_media = form.media
    return {}