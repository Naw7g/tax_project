from django.shortcuts import render

from django.http import HttpResponse

tax_rate = 0.15

def index(request):
    return HttpResponse("<html><body><p>This is a site to calculate tax.</p></body></html>")

def calculate_tax(request, number):
    total_price = number * (1 + tax_rate)
    return HttpResponse(f"<html><body><p>Total price after tax: {total_price:.2f}</p></body></html>")

def tax_rate_view(request):
    return HttpResponse(f"<html><body><h1>{tax_rate * 100}%</h1></body></html>")

