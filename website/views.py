from django.shortcuts import render
from .models import NewMessage

def index(request):
    return render(request, "website/index.html")

def python_course(request):
    currencies = [
        "AED", "ARS", "AUD", "BRL", "CAD", "CHF", "CZK", "ETB", "EUR", "GBP",
        "GHS", "ILS", "INR", "JPY", "KES", "MAD", "MUR", "MYR", "NGN", "NOK",
        "NZD", "PEN", "PLN", "RUB", "RWF", "SAR", "SEK", "SGD", "SLL", "TZS",
        "UGX", "USD", "XAF", "XOF", "ZAR", "ZMK", "ZMW", "MWK"
    ]
    return render(request, "website/student_pay.html", {
        "flutterwaveCurrencies": currencies
    })

def pay(request, tx_ref):
    trans_ref = request.GET.get("tx_ref")
    tx_ref = trans_ref


        # Display a success message to the user
    success_message = "Payment made successfully"

    # Redirect the user to the listing page
    return render(request, "website/pay_success.html", {
        "success_message": success_message,

    })

def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_message = NewMessage(name=name, email=email, message=message)

        new_message.save()

        return render(request, "website/index.html", {"message": "Message Sent Successfully"})
