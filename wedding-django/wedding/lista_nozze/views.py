from rest_framework import viewsets, status, generics
from .models import Item, Friend, Food, Survey
from .serializers import ItemSerializer, FriendSerializer, FoodSerializer, SurveySerializer
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework import permissions

class FriendPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated



def send_email(destination, html):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    sender_email = "matrimonioandreamicol@gmail.com"
    receiver_email = destination
    password = "niczbjdpbtuhxkdi"
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
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ringraziamento</title>
        <style>
            body {{
                margin: 0;
                padding: 20px;
            }}

            h1 {{
                text-align: center;
                padding: 1rem;
            }}
            p {{
                text-align: center;
            }}
            .container {{
                padding: 4rem;
            }}

        </style>
    </head>
    <body class="cart-page">

        <div class="container" style="background-color: #abd0f0 !important">
        <h1>Grazie mille!</h1>
        <p>Grazie {0} per il tuo contributo!</p>
        <p>Puoi completare il regalo, effettuando il pagamento di <strong> {1} € </strong> tramite un bonifico bancario al seguente IBAN:</p>
        <p></p>
        <p style="font-size: 2rem">IT10W0851161230000000033059</p>
        </div>
    </body>
    </html>
    """.format(giftGiver, price)
    return html_content

class SurveyCreateView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyListView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [FriendPermission]

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

def survey(request):
    return render(request, 'lista_nozze/survey.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, or a specific URL
                return redirect('dashboard')  # Assuming 'dashboard' is the name of the URL pattern for the dashboard page
            else:
                # Invalid login
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to a page after logout, or a specific URL
    return redirect('login')


@login_required
def dashboard_view(request):
    food_list = Food.objects.all()
    survey_list = Survey.objects.all()
    friend_list = Friend.objects.all()
    
    context = {
        'food_list': food_list,
        'survey_list': survey_list,
        'friend_list': friend_list,
    }
    return render(request, 'dashboard.html', context)
