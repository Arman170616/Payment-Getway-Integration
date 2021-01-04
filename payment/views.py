from django.shortcuts import render, HttpResponseRedirect, redirect
import requests
from decimal import Decimal
import socket
from django.http import HttpResponse
from  sslcommerz_python.payment import SSLCSession

from django.contrib import messages

from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    
    return render(request, 'payment/pay.html', context={})



def payment(request):

    store_id = 'ehsan5fead69e8b4f9'
    API_key = 'ehsan5fead69e8b4f9@ssl'

    mypayment = SSLCSession(

        sslc_is_sandbox=True, 
        sslc_store_id=store_id, 
        sslc_store_pass=API_key
    
    )



    status_url = request.build_absolute_uri(reverse('payment:complete'))
    #print(status_url)

    mypayment.set_urls(
        success_url=status_url, 
        fail_url=status_url, 
        cancel_url=status_url,
        ipn_url=status_url
    )

   

    
    mypayment.set_product_integration(

        total_amount=Decimal(50), 
        currency='BDT', 
        product_category='Mixed', 
        product_name='demo', 
        num_of_item=2, 
        shipping_method='YES', 
        product_profile='None'
    )


    mypayment.set_customer_info(
        name='John Doe', 
        email='johndoe@email.com',
        address1='demo address', 
        address2='demo address 2', 
        city='Dhaka', 
        postcode='1207', 
        country='Bangladesh', 
        phone='01711111111'
        
    )


    mypayment.set_shipping_info(
    
        shipping_to='demo customer', 
        address='demo address', 
        city='Dhaka', 
        postcode='1209', 
        country='Bangladesh'
    )



    # If you want to post some additional values
    # mypayment.set_additional_values(
    
    #     value_a='cusotmer@email.com', 
    #     value_b='portalcustomerid', 
    #     value_c='1234', 
    #     value_d='uuid'
    # )
    
    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])

    return render(request, 'payment/pay.html',context={})
    

@csrf_exempt
def complete(request):
    if request.method == "POST" or request.method == "post":
        payment_data = request.POST
        status = payment_data['status']
    return render(request, 'payment/complete.html', context={})


   

