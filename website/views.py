from django.shortcuts import render, get_object_or_404
from .models import *
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.style import Style
import re

def index(request):
    return render(request, "website/index.html")

def article(request, title):
    article = get_object_or_404(Article, title=title)
    content = article.content  # Assuming your article content is stored in the 'content' field

    # Define a regular expression pattern to find code snippets
    code_pattern = r'<pre><code class="language-(\w+)">([\s\S]*?)</code></pre>'

    def highlight_code(match):
        language, code = match.groups()
        lexer = get_lexer_by_name(language, stripall=True)
        formatter = HtmlFormatter(style="default")  # Use the "default" Pygments style
        return highlight(code, lexer, formatter)

    # Use re.sub to replace code snippets with highlighted code
    highlighted_content = re.sub(code_pattern, highlight_code, content)

    return render(request, 'website/article.html', {'article': article, 'highlighted_content': highlighted_content})

def articles(request):
    contents = Article.objects.all().order_by('-pub_date')
    return render(request, "website/all_articles.html", {"all_articles": contents})

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

def full_stack_course(request):
    return render(request, 'website/full_stack.html')

def cs50p(request):
    return render(request, "website/cs50p.html")
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
