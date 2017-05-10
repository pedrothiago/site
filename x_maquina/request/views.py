from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages
from request.forms import RequestForm
from request.models import Request
import traceback


def request_list(request):
    reqs = None
    if request.user.is_superuser:
        pending_requests = Request.objects.filter(
            status=Request.RECEIVED).order_by('sent_at')
        other_requests = Request.objects.exclude(status=Request.RECEIVED).order_by('sent_at')
    else:
        try:
            pending_requests = Request.objects.filter(
                owner=request.user, status=Request.RECEIVED).order_by('sent_at')
            other_requests = Request.objects.filter(
                owner=request.user).exclude(status=Request.RECEIVED).order_by('sent_at')
        except BaseException:
            raise PermissionDenied
    return render(request,
                  'request/requests.html',
                  {'pending_requests': pending_requests,
                   'other_requests': other_requests})


def request_new(request):
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)
        if request_form.is_valid():
            try:
                req = request_form.save(commit=False)
                req.owner = request.user
                req.save()
                messages.success(request, "Solicitação recebida!")
                return redirect('Home')
            except Exception as e:
                messages.error(request, "Falha ao salvar solicitação!")
                print(e)
                traceback.print_exc()
    else:
        request_form = RequestForm()
    return render(request, 'request/request_form.html', {
        'form': request_form})
