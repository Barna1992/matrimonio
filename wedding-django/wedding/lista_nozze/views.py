from rest_framework import viewsets
from .models import Item, Friend, Food
from .serializers import ItemSerializer, FriendSerializer, FoodSerializer
from rest_framework.response import Response
from rest_framework import status

def send_email(destination, html):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "sportlerofferte@gmail.com"
    receiver_email = destination
    password = "ntthqirswdjxukrz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Matrimonio Andrea & Micol"
    message["From"] = sender_email
    message["To"] = receiver_email

    message.attach(MIMEText(html, "html"))

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )




def make_html(giftGiver, price):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ringraziamento</title>
        <!-- Add any additional styles or scripts as needed -->
        <style>
            /* Add your styling here */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }

            h1 {
                text-align: center;
                padding: 1rem;
            }
            p {
                text-align: center;
            }
            .container {
                padding: 4rem;
            }

        </style>
        <link rel="stylesheet" href="/static/css/cart-style.css">
    </head>
    <body class="cart-page">

        <div class="container">
        <h1>Grazie mille!</h1>
        <p>Grazie {} per il tuo contributo!</p>
        <p>Puoi completare il regalo, effettuando il pagamento di <strong> {} € </strong> tramite un bonifico bancario al seguente IBAN:</p>
        <p></p>
        <p>IBAN</p>
        </div>
    </body>
    </html>
    """.format(giftGiver, price)
    return html_content


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('string_ids', [])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for item in items:
                item_id, item_quantity = item.split('-')
                current = Item.objects.get(id=item_id)
                current.quantity -= int(item_quantity)
                current.save()
            html = make_html(request.data.get('name', ''),request.data.get('item_price', ''))
            send_email(request.data.get('email', ''), html)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

from django.shortcuts import render

def item_list(request):
    items = Item.objects.all()
    return render(request, 'lista_nozze/item_list.html', {'items': items})

def index(request):
    return render(request, 'lista_nozze/index.html')

def lista(request):
    return render(request, 'lista_nozze/lista_nozze.html')

def cart(request):
    return render(request, 'lista_nozze/cart-page.html')

def summary(request):
    return render(request, 'lista_nozze/summary-page.html')

def thanks(request):
    return render(request, 'lista_nozze/thanks.html')

def food(request):
    return render(request, 'food.html')