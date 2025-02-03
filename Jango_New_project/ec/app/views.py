from django.shortcuts import render, HttpResponse ,redirect,get_object_or_404
from django.http import HttpResponseNotFound
from django.views import View
from .models import product,Customer,Cart
from .forms import CustomerRegistrationForm,LoginForm,CustomerProfileForm,MyPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import  logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.http import Http404

# from django.db.models import Count



# Create your views here.
def home(request):
    return render(request,"app/home.html" )

def about(request):
    return render(request,"app/about.html" )

def contact(request):
    return render(request,"app/contact.html" )

class CategoryVies(View):
    def get(self,request,val): 
        Product = product.objects.filter(category = val ) # we filterd 
        title = product.objects.filter(category = val).values('title')
        return render(request,'app/category.html',locals())
    
class CategoryTitle(View):
    def get(self,request,val): 
        Product = product.objects.filter(title = val ) # we filterd 
        title = product.objects.filter(category =Product[0].category).values('title')
        return render(request,'app/category.html',locals())

class ProductDetail(View):
    def get(self,request,pk):
        Product = product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! User Registration Successfully")
        else:
            messages.warning(request, "invalid Inpute Data")
            return render(request,'app/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data["locality"]
            city = form.cleaned_data["city"]
            mobail = form.cleaned_data["mobail"]
            state = form.cleaned_data["state"]
            zipcode = form.cleaned_data["zipcode"]

            reg = Customer(user=user,name=name,locality=locality,mobail=mobail,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation ! Profile Save SuccessFully")
        else:
            messages.warning(request,"Invalid Inpute data")
        return render(request,'app/profile.html',locals())
    
def address (request):
    add = Customer.objects.filter(user = request.user)
    return render(request,"app/address.html",locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form =CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.user = request.user
            add.name = form.cleaned_data["name"]
            add.locality = form.cleaned_data["locality"]
            add.city = form.cleaned_data["city"]
            add.mobail = form.cleaned_data["mobail"]
            add.state = form.cleaned_data["state"]
            add.zipcode = form.cleaned_data["zipcode"]
            add.save()
            messages.success(request,"Congratulation ! Profile Update SuccessFully")
            return redirect('home')
        else:
            messages.warning(request,"Invalid Inpute data")
        return redirect('address')
    

def password_change(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            # Keep the user logged in after changing their password
            update_session_auth_hash(request,form.user)

            messages.success(request,"your password was successfully changed")
            return redirect('passwordchangedone')
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request,'app/changepassword.html',{'form': form})


def password_change_done(request):
    return render(request, 'app/passwordchangedone.html')

    
def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

    
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    prod  = product.objects.get(id=product_id)
    Cart(user=user,product=prod).save()
    return redirect("/cart")


def show_cart(request):
    user= request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity*p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request,"app/add_to_cart.html",locals())

# def increment_cart_item(request, cart_id):
#     """Increment the quantity of a product in the cart."""
#     try:
#         cart_item = Cart.objects.get(id=cart_id, user=request.user)
#         cart_item.quantity += 1
#         cart_item.save()
#         return redirect("/cart")
#     except Cart.DoesNotExist:
#         raise Http404("Cart item not found")
   


def increment_cart_item(request, cart_id):
    """Increment the quantity of a product in the cart."""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("/cart")


# def decrement_cart_item(request, cart_id):
#     """Decrement the quantity of a product in the cart."""
#     try:
#         cart_item = Cart.objects.get(id=cart_id, user=request.user)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()  # If quantity is 1, remove the item from the cart
#         return redirect("/cart")
#     except Cart.DoesNotExist:
#         raise Http404("Cart item not found")
    

# from django.shortcuts import get_object_or_404, redirect
# from .models import Cart

def decrement_cart_item(request, cart_id):
    """Decrement the quantity of a product in the cart."""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # If quantity is 1, remove the item from the cart
    return redirect("/cart")


def remove_from_cart(request, cart_id):
    """Remove a product from the cart."""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect("/cart")


# def checkout(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_price = sum(item.total_price() for item in cart_items)
    
#     # Placeholder for actual checkout logic
#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     }

#     # For now, we just display the cart on the checkout page
#     return render(request, 'app/checkout.html', context)

# def manage_cart(request):
#     user = request.user

#     if request.mothod == 'get':
#         action = request.GET.get('action')
#         cart_id =request.GET.get('cart_id')
#         product_id = request.GET.get('peod_id')

#         if action == 'add' and product_id:
#             prod = get_object_or_404(product, id = product_id)
#             Cart.objects.create(user= user,product=prod)

#         elif action == 'increment' and cart_id:
#             cart_item = get_object_or_404(Cart,id=cart_id,user=user)
#             cart_item.quantity += 1
#             cart_item.save()

#         elif action == 'decrement' and cart_id:
#             cart_item =get_object_or_404(Cart,id=cart_id, user=user)
#             if cart_item.quantity > 1:
#                 cart_item.quantity - = 1
#                 cart_item.save()
#             else:
#                 cart_item.delete() # If quantity is 1, remove the item from the cart
        
#         elif action == 'remove' and cart_id:
#             #Remove item form cart
#             cart_item=get_object_or_404(Cart, id=cart_id,user=user)
#             cart_item.delete()






