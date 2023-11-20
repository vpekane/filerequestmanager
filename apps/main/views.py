from django.shortcuts import render, redirect
from dropboxcommand.filerequest import (
    open_file_requests as file_request_list,
    file_request_objects,
    get_list_of_folders
    )
from .forms import FileRequestEmailForm
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import fileSerializer

# Create your views here.
# TODO: Add 'save edit' buttons
# TODO: Create update button functionality
# TODO: Better UI experience
# TODO: Find all available folders


@api_view(["GET"])
def getRoutes(request) -> Response:
    routes = [
        {
            "name": "file-requests",
            "method": "GET",
            "desc": "gets open file requests"
        },
        {
            "name": "edit-file-request",
            "method": "GET",
            "desc": "edits a file request"
        }
    ]

    return Response(routes)


@api_view(["GET"])
def open_file_requests(request) -> Response:
    file_requests = file_request_list()
    context = {
        "files": file_requests
    }
    serializer = fileSerializer(context)
    # return Response(serializer.data)
    return Response(context)


@api_view(["GET"])
def file_request_item(request, id: str) -> render:
    file_requests = file_request_objects()
    folders = get_list_of_folders()
    context = {
        'id': id,
        'title': '',
        'description': '',
        'location': '',
    }

    for item in file_requests:
        if id == item.id:
            context['title'] = item.title
            context['description'] = item.description
            context['location'] = folders
    
    return Response(context)
    # return render(request, "edit_file_request.html", context)


def send_file_request_email(request, id: str) -> render:
    if request.method == "POST":
        email_form = FileRequestEmailForm(request.POST)

        if email_form.is_valid():
            send_mail(
                email_form['subject'].value(),
                email_form['body'].value(),
                # email here
                [email_form['email'].value()]
            )
            return redirect('file-requests')

    else:
        email_form = FileRequestEmailForm()

    file_requests = file_request_objects()
    context = {
        'form': email_form,
        'id': '',
        'title': '',
        'body': ''
    }

    for item in file_requests:
        if id == item.id:
            context['title'] = item.title
            context['body'] = item.description
            context['id'] = item.id

    return render(request, "file_request_email.html", context)