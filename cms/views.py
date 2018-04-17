from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def slash(self):
    response = ''
    for Page in Pages.objects.get():
        redirection = "<a href=/" + str(Page.id) + ">" + Page.name + "</a>"
        response += (str(Page.id) + ' : ' + redirection + "/n"
    return(HttpResponse(response))


def number(self, num):
    try:
        Page = Pages.objects.get(id=str(num))
        return(HttpResponse(Page.page)


def notfound(self):
    return(HttpResponseNotFound("Resource not in database"))
