import smtplib
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import smtplib
# Create your views here.

def homepage(request):
    return render(request,'newhome.html')



def order_post(request):

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    quantity = request.POST['quantity']

    amount = 500 * 100

    request.session.flush()

    return redirect('/raz_pay/' + str(amount))


def raz_pay(request, amount):

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(
        auth=(razorpay_api_key, razorpay_secret_key)
    )

    amount = float(amount)

    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',
    }

    order = razorpay_client.order.create(data=order_data)

    return render(request, 'pp.html', {

        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id']

    })



def userpayment_post(request):

    name = request.session['name']
    email = request.session['email']
    phone = request.session['phone']
    address = request.session['address']
    quantity = request.session['quantity']

    subject = "ECOMONKS Order Confirmation"

    message = f"""
Hello {name},

Your payment was successful.

Order Details:

Name: {name}
Phone: {phone}
Address: {address}
Quantity: {quantity}

Thank you for ordering Edible Karpooram from ECOMONKS.
"""
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("leagaladvisorteam@gmail.com", "eugnxtyylwtqwlav") 
    to = email
    subject = "Test Email"
    body = message
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("s@gmail.com", to, msg)  
    server.quit()


    return HttpResponse(
        "<script>alert('Payment Successful & Email Sent');window.location='/'</script>"
    )




def emailenquiry(request):

    if request.method == "POST":

        email = request.POST.get('email')

        subject = "ECOMONKS Subscription"

        message = f"""
Hello,

Thank you for subscribing to ECOMONKS.

You will now receive:
- Product updates
- Offers
- Latest notifications

Thank you for staying connected with us.
"""

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Gmail App Password
            server.login(
                "leagaladvisorteam@gmail.com",
                "eugnxtyylwtqwlav"
            )

            msg = f"Subject: {subject}\n\n{message}"

            server.sendmail(
                "yourgmail@gmail.com",
                email,
                msg
            )

            server.quit()

            return HttpResponse(
                "<script>alert('Subscribed Successfully');window.location='/'</script>"
            )

        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return HttpResponse("Invalid Request")